AnsiString __fastcall TDTM::PrintPosFP550
(int PositionType, int ASc, AnsiString AClcsct, double APrice, double AQty,
 int ANrDepTva, int ATipPay, AnsiString AStr0, int bFirst, int bNotFiscal, int ACheckNr )
{
  AnsiString vResult;
  AnsiString asErrMes;
  int nPauseAfterZX = UAParams.ReadInteger("PauseAfterZX",1000);
    //int rez;
  switch( PositionType )
  {
   case 0  : asErrMes = Lng("Tiparirea pozitiei","Печать позиции"); break;
   case 1  : asErrMes = Lng("Inhidere bon de casa","Закрытие чека"); break;
   case 2  : asErrMes = Lng("Tiparire text","Печать текста"); break;
   case 3  : asErrMes = Lng("Deschidere bon de casa","Открытие чека"); break;
   case 4  : asErrMes = Lng("Tiparire suma totala","Печать итоговой суммы"); break;
   case 5  : asErrMes = Lng("Tiparire informatie de diagnostic","Печать диагностической информации"); break;
   case 6  : asErrMes = Lng("Tiparire raport Z/X","Печать Z/X отчета"); break;
   case 7  : asErrMes = Lng("Deschidere cutie","Открытие ящика"); break;
   case 8  : asErrMes = Lng("SubTotal","SubTotal"); break;
   case 9  : asErrMes = Lng("Intrare/extragere numerar","Служебное внесение/изъятие денег"); break;
   case 10 : asErrMes = Lng("Curatarea ecranului","Очистка дисплея"); break;
   case 11 : asErrMes = Lng("Editarea partii de sus a display-ului","Печать на верхней строке дисплея"); break;
   case 12 : asErrMes = Lng("Editarea partii de jos a display-ului","Печать на нижней строке дисплея"); break;
   case 13 : asErrMes = Lng("Editarea textului pe display","Печать текста на дисплее"); break;
   case 14 : asErrMes = Lng("Setare data/ora","Установка даты/времени"); break;
   case 15 : asErrMes = Lng("Citire data/ora","Считывание даты/времени"); break;
   case 16 : asErrMes = Lng("Citire informatii vanzari pe zi","Считывание информации о накоплениях за день"); break;
  }

  //rez = FpAtl.Exec(Function("Send") << 488839203 << 48 << as0 << vResult);
  AnsiString as0 = "1,0000,1";
  AnsiString as1;// = Product1\\nPricolinii\\tA0.01*1"
  AnsiString as2;
  AnsiString asMsg;

  bool res;
  int key = 488839203;

  /*
  for (int i = 0;i <= 100;i++)
  {
   if (i==100)
    {
     return;
    }
   if (GetInformBeforePrint()!=1)
    continue;
   else
    break;
  }
  */
   //TO DO: Добавить PaperCut команда 2DH	(45)
   switch (PositionType)
   {
     case 3 : // Открытие фискального чека
       {
        int nPauseAfterOpen = UAParams.ReadInteger("PauseAfterOpen",1000);
        if( bNotFiscal )
        {
          asMsg = Lng("Deschidere bon de casa nefiscal ","Открытие нефискального чека ")+as0;
          WriteLog(asMsg);
          if (ReadBoolParam(rpmIniFirst,"FP550EmptyNFComand", false))
            as0 = "";
          if( !VirtFP550 )
            res = FpAtl.Exec(Function("Send") << key << 38 << as0 << vResult);
          Sleep(nPauseAfterOpen);
          AnaliseResultFP550(38,asMsg,res,true);
        }
        else
        {
          if( DatecsFPModel == "DP25" )
            as0 = "1\t1\t1\t\t";
          asMsg = Lng("Deschidere bon de casa fiscal ","Открытие фискального чека ")+as0;
          WriteLog(asMsg);
          if( !VirtFP550 )
            res = FpAtl.Exec(Function("Send") << key << 48 << as0 << vResult);
          Sleep(nPauseAfterOpen);
          AnaliseResultFP550(48,asMsg,res,true);
        }
       }
       break;
     case 0 : // Напечатить позицию
       {
        //as1 = Product1\\nPricolinii\\tA0.01*1";
         AnsiString Ltva="";
         if( !ReadBoolParam(rpmIniFirst,"FPCyrillicTVALetters",false) )
         {
           switch (ANrDepTva)
           {
             case 1 : Ltva = "A"; break;
             case 2 : Ltva = "B"; break;
             case 3 : Ltva = "C"; break;
             case 4 : Ltva = "D";   // нулевая ставка в FP550 аппарате
           }
         }
         else
         {
           switch (ANrDepTva)
           {
             case 1 : Ltva = "А"; break;
             case 2 : Ltva = "Б"; break;
             case 3 : Ltva = "В"; break;
             case 4 : Ltva = "Г";   // нулевая ставка в FP550 аппарате
           }
         }

         AnsiString TvrName, Trv1p, Trv2p;
         int maxlen = 39, maxlen1 = 18, maxlen2 = 22;
         if( bNotFiscal )
           { maxlen = 60; maxlen1 = 30; maxlen2 = 30; }
         if( ReadIniBoolean("WordWrap",false) )
         {
          TvrName = AClcsct.SubString(1,maxlen);
          Trv1p = TvrName.SubString(1,maxlen1);
          if (TvrName.Length() > maxlen1 )
             Trv2p = TvrName.SubString(maxlen1 + 1,225);
          else Trv2p = " ";
         }
         else
         {
          Trv1p=" ";
          Trv2p = AClcsct.SubString(1,maxlen2);
         }
         //as1 = AClcsct+"\\n"+"\\t"+Ltva+FloatToStr(APrice)+"*"+FloatToStr(AQty);
          int nPausePos = UAParams.ReadInteger("PauseAfterPos",60);
          if( bNotFiscal )
          {
           //linella probleme cu deblocarea
           if( APrice == 0 )
             return "";
           //linella probleme cu deblocarea
           as1 = Trv1p+"\\n";
           if( DatecsFPModel == "DP25" )
             as1 += AnsiString("\t"); 
           if( !VirtFP550 )
             res = FpAtl.Exec(Function("Send") << key << 42 << as1 << vResult);
           Sleep(nPausePos);
           asMsg = Lng("Tiparire pozitie ","Напечатать позицию ")+as1;
           AnaliseResultFP550(42,asMsg,res);
           if( Trv2p != " " )
           {
             as1 = Trv2p+"\\n";
             if( DatecsFPModel == "DP25" )
               as1 += AnsiString("\t");
             asMsg = Lng("Tiparire pozitie ","Напечатать позицию ")+as1;
             if( !VirtFP550 )
               res = FpAtl.Exec(Function("Send") << key << 42 << as1 << vResult);
             Sleep(nPausePos);
             AnaliseResultFP550(42,asMsg,res);
           }
           as1 = Ltva+" "+FloatToStr(APrice)+" x "+FloatToStr(AQty)+" = "+FloatToStr(APrice*AQty)+"\\n";
           if( DatecsFPModel == "DP25" )
             as1 += AnsiString("\t"); 
           asMsg = Lng("Tiparire pozitie ","Напечатать позицию ")+as1;
           if( !VirtFP550 )
             res = FpAtl.Exec(Function("Send") << key << 42 << as1 << vResult);
           Sleep(nPausePos);
           AnaliseResultFP550(42,asMsg,res);
          }
          else
          {
            if( APrice || ReadBoolParam(rpmDBFirst,"CanPrintZeroPosition", false) )
            {
               AnsiString asSep = "\t";
               if( DatecsFPModel == "DP25" )
               {
                  // PLU Name (TO DO: up to 32 characters), TaxCode, Price, Qnt,
                  // DiscType (TO DO: Test), DiscValue (TO DO: Test), Dep
                  Trv1p = AClcsct.SubString(1,32);

                  //as1 = Trv1p+"\\n"+Trv2p + asSep + IntToStr(ANrDepTva) + asSep + FloatToStr(APrice) +
                  as1 = Trv1p+ asSep + IntToStr(ANrDepTva) + asSep + FloatToStr(APrice) +
                        asSep + FloatToStr(AQty) + asSep + asSep + asSep + AnsiString("0") + asSep;
               }
               else if( DatecsFPModel == "700KLMD" )
               {
                  if( AQty > 0 )
                    as1 = Trv1p+"\\n"+Trv2p+"\\t"+Ltva+FloatToStr(APrice)+"*"+FloatToStr(AQty);
                  else
                    as1 = Trv1p+"\\n"+Trv2p+"\\t"+Ltva+FloatToStr(APrice*(-1))+"*"+FloatToStr(AQty*(-1));
               }
               else as1 = Trv1p+"\\n"+Trv2p+"\\t"+Ltva+FloatToStr(APrice)+"*"+FloatToStr(AQty);
               //as1 = "A\\n\\tA1*1"; test
               asMsg = Lng("Tiparire pozitie ","Напечатать позицию ")+as1;
               WriteLog(asMsg);
               if( !VirtFP550 )
                 res = FpAtl.Exec(Function("Send") << key << 49 << as1 << vResult);
               Sleep(nPausePos);
               AnaliseResultFP550(49,asMsg,res,true);
               if( ReadBoolParam(rpmIniFirst,"FP550BreakAfterOpenFiscal", false) )
                 throw Exception("FP550BreakAfterOpenFiscal");
            }
          }
       }  break;
     case 4 :  // напечатать итоговую сумму
       {
       int nPauseAfterItog = UAParams.ReadInteger("PauseAfterItog",1500);
       WriteLog("ACheckNr =" + IntToStr(ACheckNr));
       if (bNotFiscal)
       {
        as2 = "----------------------------";
        if( DatecsFPModel == "DP25" )
           as2 += AnsiString("\t");
        if( !VirtFP550 )
          res = FpAtl.Exec(Function("Send") << key << 42 << as2 << vResult);
        Sleep(nPauseAfterItog);
        AnaliseResultFP550(42,Lng("Tiparire suma totala ","Напечатать итоговую сумму ")+as2,res);
        as2 = "TOTAL  " + FloatToStr(APrice);
        if( DatecsFPModel == "DP25" )
           as2 += AnsiString("\t");
        if( !VirtFP550 )
          res = FpAtl.Exec(Function("Send") << key << 42 << as2 << vResult);
        Sleep(nPauseAfterItog);
        AnaliseResultFP550(42,Lng("Tiparire suma totala ","Напечатать итоговую сумму ")+as2,res);
       }
       else
       {
         //test
     if( MultiPaymentEnabled && ACheckNr )
		 {
           double sum_cash , sum_card, sum_ctf, sum_tme, sum_tmh, sum_gift;

           int iOpenComand;

           if( GlobalType == "UNIREST" )
             iOpenComand = DTM->vmdb_comenz_restaurantNR_COMAND->AsInteger;
           else
             iOpenComand = OpenComand;


           GetPayAmounts(iOpenComand, sum_cash, sum_card, sum_ctf, sum_tme, sum_tmh, sum_gift);
           bool bCanPayZeroBon = ReadBoolParam(rpmDBFirst,"CanPayZeroBon", false) && (sum_cash + sum_card + sum_ctf == 0);
           if ( sum_card ) {
             if( DatecsFPModel == "DP25" )
               as2 = "1\t";
             else as2 = "\\t" + FDatecsFPCardLetter;
             if( APrice ) as2 += FloatToStr( sum_card );
             if( DatecsFPModel == "DP25" )
               as2 += AnsiString("\t");
             asMsg = Lng("Tiparire suma totala card","Напечатать итоговую сумму карточка")+as2;
             WriteLog(asMsg);
             if( !VirtFP550 )
               res = FpAtl.Exec(Function("Send") << key << 53 << as2 << vResult);
             Sleep(nPauseAfterItog);
             AnaliseResultFP550(53,asMsg,res);
           }
           if ( sum_ctf ) {
             if( DatecsFPModel == "DP25" )
               as2 = "3\t";
             else as2 = "\\t" + FDatecsFPCertLetter;
             if( APrice ) as2 += FloatToStr( sum_ctf );
             if( DatecsFPModel == "DP25" )
               as2 += AnsiString("\t");
             asMsg = Lng("Tiparire suma totala certificat","Напечатать итоговую сумму сертификат")+as2;
             WriteLog(asMsg);
             if( !VirtFP550 )
               res = FpAtl.Exec(Function("Send") << key << 53 << as2 << vResult);
             Sleep(nPauseAfterItog);
             AnaliseResultFP550(53,asMsg,res);
           }
           if ( sum_tme ) {
             if( DatecsFPModel == "DP25" )
               as2 = FDatecsFPTMELetter + "\t";
             else as2 = "\\t" + FDatecsFPTMELetter;
             if( APrice ) as2 += FloatToStr( sum_tme );
             if( DatecsFPModel == "DP25" )
               as2 += AnsiString("\t");
             asMsg = Lng("Tiparire suma totala TME","Напечатать итоговую сумму TME")+as2;
             WriteLog(asMsg);
             if( !VirtFP550 )
               res = FpAtl.Exec(Function("Send") << key << 53 << as2 << vResult);
             Sleep(nPauseAfterItog);
             AnaliseResultFP550(53,asMsg,res);
           }
           if ( sum_tmh ) {
             if( DatecsFPModel == "DP25" )
               as2 = FDatecsFPTMHLetter + "\t";
             else as2 = "\\t" + FDatecsFPTMHLetter;
             if( APrice ) as2 += FloatToStr( sum_tmh );
             if( DatecsFPModel == "DP25" )
               as2 += AnsiString("\t");
             asMsg = Lng("Tiparire suma totala TMH","Напечатать итоговую сумму TMH")+as2;
             WriteLog(asMsg);
             if( !VirtFP550 )
               res = FpAtl.Exec(Function("Send") << key << 53 << as2 << vResult);
             Sleep(nPauseAfterItog);
             AnaliseResultFP550(53,asMsg,res);
           }
           if ( sum_gift ) {
             if( DatecsFPModel == "DP25" )
               as2 = FDatecsFPGiftLetter + "\t";
             else as2 = "\\t" + FDatecsFPGiftLetter;
             if( APrice ) as2 += FloatToStr( sum_gift );
             if( DatecsFPModel == "DP25" )
               as2 += AnsiString("\t");
             asMsg = Lng("Tiparire suma totala Gift","Напечатать итоговую сумму Gift")+as2;
             WriteLog(asMsg);
             if( !VirtFP550 )
               res = FpAtl.Exec(Function("Send") << key << 53 << as2 << vResult);
             Sleep(nPauseAfterItog);
             AnaliseResultFP550(53,asMsg,res);
           }
           if ( (sum_cash || bCanPayZeroBon && (!sum_tme && !sum_tmh && !sum_gift) ) ) {
             if( DatecsFPModel == "DP25" )
               as2 = "0\t";
             else as2 = "\\t";
             if( APrice ) as2 += FloatToStr( sum_cash );
             if( DatecsFPModel == "DP25" )
               as2 += AnsiString("\t");
             asMsg = Lng("Tiparire suma totala cash","Напечатать итоговую сумму наличные")+as2;
             WriteLog(asMsg);
             if( !VirtFP550 )
               res = FpAtl.Exec(Function("Send") << key << 53 << as2 << vResult);
             Sleep(nPauseAfterItog);
             AnaliseResultFP550(53,asMsg,res);
           }
         }
         else
         {
          //end test
           if( DatecsFPModel == "DP25" )
           {
             if( ATipPay ) as2 = "1\t";
             else as2 = "0\t";
           }
           else
           {
             as2 = "\\t";
             // ATipPay=1 - оплата карточкой (0-наличными)
             if( ATipPay ) as2 += "N";
           }
           if( APrice )
           {
             as2 += FloatToStr(APrice);
             if( DatecsFPModel == "DP25" )
             {
               as2 += "\t";
             }
           }
           else
           {
             if( DatecsFPModel == "DP25" )
             {
               as2 += "0\t";
             }
           }
           asMsg = Lng("Tiparire suma totala ","Напечатать итоговую сумму ")+as2;
           WriteLog(asMsg);
           if( !VirtFP550 )
             res = FpAtl.Exec(Function("Send") << key << 53 << as2 << vResult);
           Sleep(nPauseAfterItog);
           AnaliseResultFP550(53,asMsg,res);
         }
        }
       }
       break;
     case 2 : // Напечать  Техт
       {
         int nPausePos = UAParams.ReadInteger("PauseAfterPos",60);
         int Cod = bNotFiscal ? 42 : 54;
         AnsiString asText = AStr0;
         if( DatecsFPModel == "DP25" )
           asText += AnsiString("\t");
         WriteLog("Напечать Техт "+asText);

         if( !VirtFP550 )
           res = FpAtl.Exec(Function("Send") << key << Cod << asText << vResult);
         Sleep(nPausePos);
         AnaliseResultFP550(Cod,asMsg,res);
       }
       break;
     case 1 : // Закрыть чек
       {
        int nPauseAfterOpen = UAParams.ReadInteger("PauseAfterOpen",1000);
        if (bNotFiscal)
        {
         if( !VirtFP550 )
           res = FpAtl.Exec(Function("Send") << key << 39 << "" << vResult);
         Sleep(nPauseAfterOpen);
         AnaliseResultFP550(39,Lng("Inchide bonul de casa ","Закрыть чек "),res,true);
        }
        else
        {
         asMsg = Lng("Inchide bonul de casa ","Закрыть чек ");
         WriteLog(asMsg);
         if( !VirtFP550 )
           res = FpAtl.Exec(Function("Send") << key << 56 << "" << vResult);
         Sleep(nPauseAfterOpen);
         AnaliseResultFP550(56,asMsg,res,true);
        }
       }
       break;
     case 5 : // Печать диагностической информации
       {
        asMsg = Lng("Tiparire informatie de diagnostic ","Печать диагностической информации ");
        WriteLog(asMsg);
        if( !VirtFP550 )
          res = FpAtl.Exec(Function("Send") << key << 71 << "" << vResult);
        Sleep(nPauseAfterZX);
        AnaliseResultFP550(71,asMsg,res,true);
       }
       break;
     case 6 : // Печать Z отчета
       {
        AnsiString asRep = "";
        if( ASc )
         asRep = IntToStr(ASc);

        if( DatecsFPModel == "DP25" )
        {
          if( (ASc == Z_MODE0) || (ASc == Z_MODE1) )
            asRep = "Z\t";
          else
            asRep = "X\t";
        }

        asMsg = "Печать Z/X отчета "+asRep;
        WriteLog(asMsg);
        if( !VirtFP550 )
          res = FpAtl.Exec(Function("Send") << key << 69 << asRep << vResult);
        Sleep(nPauseAfterZX);
        AnaliseResultFP550(69,asMsg,res,true);
       }
       break;
     case 7 : // Открытие ящика
       {
        AnsiString as = "";
        if (ASc)
         as = ASc;
       if( DatecsFPModel == "DP25" )
       {
         as += AnsiString("\t");
       }
        asMsg = "Открытие денежного ящика "+as;
        WriteLog(asMsg);
        if( !VirtFP550 )
          res = FpAtl.Exec(Function("Send") << key << 106 << as << vResult);
        Sleep(nPauseAfterZX);
        AnaliseResultFP550(106,asMsg,res,true);
       }
      break;
     case 8 : // SubTotal
     {
       AnsiString as = "";
       if( DatecsFPModel == "DP25" )
       {
         as = "0\t0\t0\t"; // No print, no display, no DiscType
       }
       else
       {
        if (ASc)
         as = IntToStr(ASc);
       }
       asMsg = "SubTotal" + as;
       WriteLog(asMsg);
       if( !VirtFP550 )
         //res = FpAtl.Exec(Function("Send") << key << 51 << (short)ASc << vResult);
         //res = FpAtl.Exec(Function("Send") << key << 51 << "00" << vResult);  TO DO: проверить для какого ФП нужны 00
         res = FpAtl.Exec(Function("Send") << key << 51 << as << vResult);
       int anres = AnaliseResultFP550(51,asMsg,res);
       if (anres == 1)
       {
         AnsiString asRes;
         if( !VirtFP550 )
           asRes = FpAtl.Exec(Function("GetLastResult") << 855147354);
         return asRes;
       }
     }
     break;
     case 9: // Служебное внесение/изъятие денег. AQty > 0 - внесение, AQty < 0 - изъятие
     {
       AnsiString as;
       if( DatecsFPModel == "DP25" )
       {
         if( AQty >= 0 ) as = "0";
         else as = "1";
         as += AnsiString("\t") + FloatToStr(fabs(AQty)) + AnsiString("\t"); 
       }
       else as = FloatToStr(AQty);
       asMsg = asErrMes + " " + as;
       WriteLog(asMsg);
       if( !VirtFP550 )
         res = FpAtl.Exec(Function("Send") << key << 70 << as << vResult);
       AnaliseResultFP550(70,asMsg,res,true);
     }
     break;
     case 10: // Очистка дисплея
     {
       WriteLog(asErrMes);
       if( !VirtFP550 )
         res = FpAtl.Exec(Function("Send") << key << 33 << "" << vResult);
       AnaliseResultFP550(33,asErrMes,res);
     }
     break;
     case 11: // Печать на верхней строке дисплея
     {
       WriteLog(asErrMes + AStr0);
       if( !VirtFP550 )
         res = FpAtl.Exec(Function("Send") << key << 47 << AStr0 << vResult);
       AnaliseResultFP550(47,asErrMes + AStr0,res);
     }
     break;
     case 12: // Печать на нижней строке дисплея
     {
       WriteLog(asErrMes + AStr0);
       if( !VirtFP550 )
         res = FpAtl.Exec(Function("Send") << key << 35 << AStr0 << vResult);
       AnaliseResultFP550(35,asErrMes + AStr0,res);
     }
     break;
     case 13: // Печать текста на дисплее
     {
       WriteLog(asErrMes + AStr0);
       if( !VirtFP550 )
         res = FpAtl.Exec(Function("Send") << key << 100 << AStr0 << vResult);
       AnaliseResultFP550(100,asErrMes + AStr0,res);
     }
     break;
     case 14 : // Установка даты/времени
     {
       WriteLog(asErrMes + AStr0);
       if( !VirtFP550 )
         res = FpAtl.Exec(Function("Send") << key << 61 << AStr0 << vResult);
       AnaliseResultFP550(61,asErrMes + AStr0,res);
     }
     break;
     case 15 : // Считывание даты/времени
     {
       WriteLog(asErrMes);
       if( !VirtFP550 )
         res = FpAtl.Exec(Function("Send") << key << 62 << "" << vResult);
       if( AnaliseResultFP550(62,asErrMes,res) == 1)
         return FpAtl.Exec(Function("GetLastResult") << 855147354);
     }
     break;
     case 16 : // Считывание информации о накоплениях за день
     {
       WriteLog(asErrMes);
       int iFP550DailySumsCode = ReadIntParam(rpmIniFirst,"FP550DailySumsCode",67);
       AnsiString asOption;
       if( DatecsFPModel == "DP25" ) asOption = "0\t";
       if( !VirtFP550 )
         res = FpAtl.Exec(Function("Send") << key << iFP550DailySumsCode << asOption << vResult);
       if( AnaliseResultFP550(iFP550DailySumsCode,asErrMes,res) == 1)
         return FpAtl.Exec(Function("GetLastResult") << 855147354);
     }
     break;
   }
  return "";
}