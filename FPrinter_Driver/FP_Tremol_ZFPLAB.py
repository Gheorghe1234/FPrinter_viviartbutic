import logging

from Tremol_ZFPLAB.FP_core import ServerException, SErrorType
from Tremol_ZFPLAB.FP import FP, Enums
# from UNA_Support.Utility import *


logger = logging.getLogger(__name__)


class FP_Tremol:
    def __init__(self, isForm=False):
        self.zfp = FP()
        logger.info(f'ZFP Version: {self.zfp._timestamp}')

        self.comm_port = 'COM10'
        self.baud = 115200

        self.TCP_IP = '192.168.200.22'
        self.TCP_PORT = 8000
        self.TCP_PASS ='1234'
        self.sumFiscalBon = 0.0
        self.sumPaymentNonReg = 0.0
        self.errorCode = 0
        self.error_text = ''
        self.response_text = ''
        self.isForm = isForm

    def OpenPort(self, TCP = False):
        logger.info('Open comport: [{comm_port}]'.format(comm_port=self.comm_port))
        res = -1
        try:
            if TCP: self.zfp.serverSetDeviceTcpSettings(self.TCP_IP, self.TCP_PORT, self.TCP_PASS)
            else: self.zfp.serverSetDeviceSerialSettings(self.comm_port, int(self.baud))

            version = self.zfp.ReadVersion()
            res = 0
            self.response_text = None
            self.error_text = version

        except Exception as fpe:
            self.handle_exception(fpe)
            res = self.error_text

        return res

    def ClosePort(self):
        pass

    def FindPort(self):
        try:
            val = self.zfp.serverFindDevice()
            self.comm_port = val.serial_port
            self.baud = val.baud_rate
            self.response_text = None
        except Exception as fpe:
            self.handle_exception(fpe)

    def OpenFiscalBon(self, OpCode, OpPwd):
        res = -1
        try:
            self.zfp.OpenReceipt(OpCode, OpPwd, Enums.OptionReceipType.Standard_fiscal_receipt, Enums.OptionFiscalRcpPrintType.Step_by_step_printing)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)
        return res

    def OpenBon(self):
        res = -1
        try:
            self.zfp.OpenNonFiscalReceipt(1, '0000')
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)
        return res

    def SellFreeEx(self, Tab, TaxCd, Price, Qwan = 1):
        Tab = Tab.decode()
        logger.info(f'SELL,  param: [{Tab}], [{TaxCd}], [{Price}], [{Qwan}]')
        res = -1
        if TaxCd == 'A':
            TaxCd = Enums.OptionVATClass.VAT_class_A
        elif TaxCd == 'B':
            TaxCd = Enums.OptionVATClass.VAT_class_B
        elif TaxCd == 'C':
            TaxCd = Enums.OptionVATClass.VAT_class_C
        elif TaxCd == 'D':
            TaxCd = Enums.OptionVATClass.VAT_class_D
        elif TaxCd == 'E':
            TaxCd = Enums.OptionVATClass.VAT_class_E
        elif TaxCd == 'F':
            TaxCd = Enums.OptionVATClass.VAT_class_F
        elif TaxCd == 'G':
            TaxCd = Enums.OptionVATClass.VAT_class_G
        elif TaxCd == 'H':
            TaxCd = Enums.OptionVATClass.VAT_class_H
        elif TaxCd == 'I':
            TaxCd = Enums.OptionVATClass.VAT_class_I

        try:
            self.zfp.SellPLUwithSpecifiedVAT(Tab, TaxCd, Price, Qwan)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def SellDepartamentEx(self, NamePLU, DepNum, Price, Qwan = 1):
        res = -1
        try:
            self.zfp.SellPLUFromDep(NamePLU, DepNum, Price, Qwan)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def CloseFiscalBon(self):
        res = -1
        try:
            self.zfp.CashPayCloseReceipt()
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def CloseBon(self):
        res = -1
        try:
            self.zfp.CloseNonFiscalReceipt()
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def PaymentEx(self, Amount, PaidMode):
        res = -1
        if PaidMode == '0':
            PaidMode = Enums.OptionPaymentType.Payment_0
        elif PaidMode == '1':
            PaidMode = Enums.OptionPaymentType.Payment_1
        elif PaidMode == '3':
            PaidMode = Enums.OptionPaymentType.Payment_3

        try:
            self.zfp.Payment(PaidMode, Enums.OptionInitiatedPayment.initiated_payment, Amount, Enums.OptionFinalizedPayment.finalized_payment)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ReportDaily(self, type):
        res = -1
        if type == 2:
            type = Enums.OptionZeroing.Without_zeroing
        elif type == 0:
            type = Enums.OptionZeroing.Zeroing

        try:
            self.zfp.PrintDailyReport(type)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def PrintText(self, text):
        res = -1
        try:
            self.zfp.PrintText(text)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def PaperCut(self):
        res = -1
        try:
            self.zfp.CutPaper()
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ReadHeader(self, line):
        res = -1
        try:
            st = self.zfp.ReadHeader(line)
            self.response_text = st.HeaderText
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ReadFooter(self):
        res = -1
        try:
            st = self.zfp.ReadFooter()
            self.response_text = str(st)
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def PrintDiagnostics(self):
        res = -1
        try:
            self.zfp.PrintDiagnostics()
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ReadDateTime(self):
        res = -1
        try:
            st = self.zfp.ReadDateTime()
            self.response_text = str(st)
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ReadStatus(self):
        res = -1
        try:
            st = self.zfp.ReadStatus()
            self.response_text = st
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ReadParameters(self):
        res = -1
        try:
            st = self.zfp.ReadParameters()
            OptionPrintLogo = 'Yes' if int(st.OptionPrintLogo) == 1 else 'No'
            OptionAutoOpenDrawer = 'Yes' if int(st.OptionAutoOpenDrawer) == 1 else 'No'
            OptionAutoCut = 'Yes' if int(st.OptionAutoCut) == 1 else 'No'
            OptionExternalDispManagement = 'Manual' if int(st.OptionExternalDispManagement) == 1 else 'Auto'
            OptionArticleReportType = 'Detailed' if int(st.OptionArticleReportType) == 1 else 'Brief'
            OptionCurrency  = 'Enabled ' if int(st.OptionCurrency) == 1 else 'Disabled'
            OptionEJFontType   = 'Low Font ' if int(st.OptionEJFontType) == 1 else 'Normal Font'
            newLine = '<br>' if self.isForm == True else '\n'
            self.response_text =  newLine + ''\
                                 'POSNum:                       ' + str(st.POSNum) + newLine + '' \
                                 'OptionPrintLogo:              ' + OptionPrintLogo + newLine + '' \
                                 'OptionAutoOpenDrawer:         ' + OptionAutoOpenDrawer + newLine + '' \
                                 'OptionAutoCut:                ' + OptionAutoCut + newLine + '' \
                                 'OptionExternalDispManagement: ' + OptionExternalDispManagement + newLine + '' \
                                 'OptionArticleReportType:      ' + OptionArticleReportType + newLine + '' \
                                 'OptionCurrency:               ' + OptionCurrency + newLine + '' \
                                 'OptionEJFontType:             ' + OptionEJFontType + newLine
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def PaperFeed(self, line):
        res = -1
        line = int(line)
        try:
            for i in range(0, line):
                self.zfp.PaperFeed()
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def OfficialSumsEx(self, sum):
        res = -1
        sum = float(sum)
        try:
            st = self.zfp.ReceivedOnAccount_PaidOut(1, '0000', Enums.OptionPaymentType.Payment_0, sum)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def PrintBarcode(self, value, type):
        res = -1
        try:
            st = self.zfp.PrintBarcode(type, 10, value)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def PrintArticleReport(self, Option):
        res = -1
        try:
            st = self.zfp.PrintArticleReport(Option)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def PrintDepartmentReport(self, Option):
        res = -1
        try:
            st = self.zfp.PrintDepartmentReport(Option)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def SafeBoxOpen(self):
        res = -1
        try:
            st = self.zfp.SafeBoxOpen()
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ClearDisplay(self):
        res = -1
        try:
            st = self.zfp.ClearDisplay()
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ReadDepartment(self, DepNum):
        res = -1
        try:
            st = self.zfp.ReadDepartment(DepNum)
            newLine = '<br>' if self.isForm == True else '\n'
            self.response_text = newLine + '' \
                                 'Departament Name:         ' + st.DepName + newLine + '' \
                                 'Departament Number:       ' + st.DepNum + newLine + '' \
                                 'Last Z Report Date:       ' + str(st.LastZReportDate) + newLine + '' \
                                 'Last Z Report Number:     ' + str(st.LastZReportNumber) + newLine + '' \
                                 'Option VAT Class:         ' + st.OptionVATClass + newLine + '' \
                                 'Price:                    ' + str(st.Price) + newLine + ''
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ProgDepartment(self, Number, Name, VATClass):
        res = -1
        try:
            st = self.zfp.ProgDepartment(Number, Name, VATClass)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ProgHeader(self, Line, Text):
        res = -1
        try:
            st = self.zfp.ProgHeader(Line, Text)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ProgFooter(self, Text):
        res = -1
        try:
            st = self.zfp.ProgFooter(Text)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ProgOperator(self, Number, Name, Password):
        res = -1
        try:
            st = self.zfp.ProgOperator(Number, Name, Password)
            self.response_text = None
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def ReadOperatorNameAndPassword(self, Number):
        res = -1
        try:
            st = self.zfp.ReadOperatorNameAndPassword(Number)
            newLine = '<br>' if self.isForm == True else '\n'
            self.response_text = newLine + '' \
                                 'Number: ' + str(int(st.Number)) + newLine + '' \
                                 'Name: ' + st.Name + newLine + '' \
                                 'Password: ' + st.Password + newLine + ''
            res = 0
        except Exception as fpe:
            self.handle_exception(fpe)

        return res

    def CodeConv(self, code, params):
        logger.info('code conve. : [{code}, {params}]'.format(code=code, params=params))
        params = str(params)
        # paymentMode = {
        #     'N': 0,
        #     'P': 1,
        #     'C': 3
        # }
        paymentMode = {
            'P': 0,
            'N': 1,
            'C': 3
        }
        try:
            if code == 33:  res = self.ClearDisplay()
            elif code == 38:  res = self.OpenBon()
            elif code == 39:    res = self.CloseBon()
            elif code == 42 or code == 54:    res = self.PrintText(params)
            elif code == 43:
                if params == '':
                    res = "Nu ati indicat parametrii"
                    self.errorCode = 2
                else:
                    Line = int(params[0:1])
                    if Line < 6:
                        Text = self.AlignStrCenter(32, params[1:])
                        res = self.ProgHeader(Line, Text)
                    else:
                        Text = self.AlignStrCenter(32, params[1:])
                        res = self.ProgFooter(Text)
            elif code == 44:
                if params == '':
                    params = 1
                res = self.PaperFeed(params)
            elif code == 45:    res = self.PaperCut()
            elif code == 49:
                res = 'n'
                try:
                    pos_Tab = params.find('\\t')
                    Tab = bytes(params[0:pos_Tab].encode())
                    params = params[pos_Tab+2:]
                    pos_Tab = params.find('\\t')
                    if pos_Tab != - 1:
                        DepNum = params[0:pos_Tab]
                        params = params[pos_Tab + 2:]
                        pos_Qwan = params.find('*')
                        print(pos_Qwan)
                        Price = float(params[0:]) if pos_Qwan == -1 else float(params[0:pos_Qwan])
                        if pos_Qwan == -1:
                            Qwan = 1
                            self.sumFiscalBon += Price
                        else:
                            Qwan = float(params[pos_Qwan + 1:])
                            self.sumFiscalBon += (Price * Qwan)
                        res = self.SellFreeEx(Tab, DepNum, Price, Qwan)
                    else:
                        TaxCd = params[0:1]
                        params = params[1:]
                        pos_Qwan = params.find('*')
                        Price = float(params[0:]) if pos_Qwan == -1 else float(params[0:pos_Qwan])
                        if pos_Qwan == -1:
                            Qwan = 1
                            self.sumFiscalBon += Price
                        else:
                            Qwan = float(params[pos_Qwan + 1:])
                            self.sumFiscalBon += (Price * Qwan)
                        res = self.SellFreeEx(Tab, TaxCd, Price, Qwan)
                except KeyError:
                    res = 'Nu ati indicat parametrii'
                    self.errorCode = 2
            elif code == 48:
                try:
                    OpCode = int(params[0:1])
                    OpPwd = params[2:6]
                    # OpPwd = '0'
                    TillNmb = params[7:8]
                    res = self.OpenFiscalBon(OpCode, OpPwd)
                except ValueError:
                    res = 'Nu ati indicat parametrii'
                    self.errorCode = 2
            elif code == 53:
                if params == '':
                    res = "Nu ati indicat parametrii"
                    self.errorCode = 2
                else:
                    pos_Amount = params.find('.')
                    Tab = params[2:3]
                    # Amount = params[3:pos_Amount + 3]
                    Amount = params[3:]
                    print(Amount)
                    if Amount == '':
                        Amount = format(self.sumFiscalBon - self.sumPaymentNonReg, '.2f')
                    else:
                        # Amount = float(params[3:pos_Amount + 3])
                        Amount = float(params[3:])
                        self.sumPaymentNonReg += Amount
                    if Tab == '':
                        PaidMode = 0
                    else:
                        PaidMode = paymentMode[Tab]
                    res = self.PaymentEx(Amount, PaidMode)
                    self.sumFiscalBon = 0
            elif code == 56:    res = self.CloseFiscalBon()
            elif code == 69:
                if params == '':
                    params = 0
                res = self.ReportDaily(int(params))
            elif code == 70:
                params = float(params)
                res = self.OfficialSumsEx(params)
            elif code == 71:
                res = self.ReadStatus()
                self.response_text = Status.AllStatus
            elif code == 84:
                if params == '':
                    res = "Nu ati indicat parametrii"
                    self.errorCode = 2
                else:
                    pos_type = params.find(',')
                    barcode_type = params[0:pos_type]
                    barcode_value = params[pos_type + 1:]
                    res = self.PrintBarcode(barcode_value, barcode_type)
            elif code == 87:
                if params == '':
                    res = "Nu ati indicat parametrii"
                    self.errorCode = 2
                else:
                    pos_number = params.find(',')
                    Number = params[0:pos_number]
                    VATClass = params[pos_number+1:pos_number+2]
                    Name = params[pos_number+3:]
                    res = self.ProgDepartment(Number, Name, VATClass)
            elif code == 102:
                if params == '':
                    res = "Nu ati indicat parametrii"
                    self.errorCode = 2
                else:
                    pos_number = params.find(',')
                    Number = params[0:pos_number]
                    params = params[pos_number + 1:]
                    pos_pws = params.find(',')
                    Password = params[0:pos_pws]
                    Name = params[pos_pws+1:]
                    res = self.ProgOperator(Number, Name, Password)
            elif code == 106:
                res = self.SafeBoxOpen()
            elif code == 117:
                params = 'Z' if params == '' else params
                res = self.PrintDepartmentReport(params)
            elif code == 201:
                params = 1 if params == '' else params
                res = self.ReadHeader(params)
            elif code == 202:   res = self.ReadFooter()
            elif code == 203:   res = self.ReadDateTime()
            elif code == 204:   res = self.ReadParameters()
            elif code == 206:
                params = 'Z' if params == '' else params
                res = self.PrintArticleReport(params)
            elif code == 207:
                params = 1 if params == '' else params
                res = self.ReadDepartment(params)
            elif code == 208:
                params = 1 if params == '' else params
                res = self.ReadOperatorNameAndPassword(params)
            else:
                res = "nu este asa cod"
        except Exception as ex:
            res = f'-2\tEroare in sintaxa comanda: {code}'
            logger.error(f'{res}')
            logger.error(f'{ex}')

        return str(code) + ': ' + str(res)

    def AlignStrCenter(self, lenght, string):
        res = string
        len_string = len(string)
        left = (32 - len_string) / 2
        string = ' ' * left + string
        return string

    def fiscal_receipt(self, code, type):
        res = ''
        code = self.read_code(code)
        for row in code:
            rsp = self.CodeConv(int(row['comand']), str(row['param']))
            try:
                err = int(rsp[rsp.find(':')+2:rsp.find(':')+3])
            except ValueError:
                err = -1

            if type == 'form':
                if err == 0:
                    text = ' Succes comand' if self.response_text == None else ' ' + self.response_text
                    res += "<FONT COLOR='#00CC00'>"+ rsp + text + "<br>"
                elif err == -1:
                    res += "<FONT COLOR='#ff0000'>"+ rsp[0:rsp.find(':') + 2]  + self.error_text + "<br>"
            elif type == 'server':
                if err == 0:
                    res = "OK"
                else:
                    res += str(rsp) + str(self.error_text) + "\n"
                    # res += str(rsp) + str(self.error_text)
                    break
        return res

    def read_code(self, code):
        res = []
        code = code.split('\n')
        for row in code:
            row = str(row)
            item = row.find(',')
            if item == -1:
                line = {
                    'comand': row[0:],
                    'param': ''
                }
            else:
                line = {
                    'comand': row[0:item],
                    'param': row[item + 1:]
                }
            res.append(line)

        return res

    def handle_exception(self, sx):
        msg = sx
        if hasattr(sx, 'message'):
            msg = sx.message

        if isinstance(sx, ServerException):
            self.error_text = f"ZfpLab library exception!\n"
            if sx.isFiscalPrinterError:
                # Possible reasons:
                # sx.STE1 =                                       sx.STE2 =
                #       0x30 OK                                          0x30 OK
                #       0x31 Out of paper, printer failure               0x31 Invalid command
                #       0x32 Registers overflow                          0x32 Illegal command
                #       0x33 Clock failure or incorrect date&time        0x33 Z daily report is not zero
                #       0x34 Opened fiscal receipt                       0x34 Syntax error
                #       0x35 Payment residue account                     0x35 Input registers overflow
                #       0x36 Opened non-fiscal receipt                   0x36 Zero input registers
                #       0x37 Payment is done but receipt is not closed   0x37 Unavailable transaction for correction
                #       0x38 Fiscal memory failure                       0x38 Insufficient amount on hand
                #       0x39 Incorrect password                          0x3A No access
                #       0x3a Missing external display
                #       0x3b 24hours block - missing Z report
                #       0x3c Overheated printer thermal head.
                #       0x3d Interrupt power supply in fiscal receipt (one time until status is read)
                #       0x3e Overflow EJ
                #       0x3f Insufficient conditions
                #
                if sx.ste1 == 0x30 and sx.ste2 == 0x32:
                    self.error_text  += f"sx.STE1 == 0x30 - command is OK AND sx.STE2 == 0x32 - command is Illegal in current context\n"
                elif sx.ste1 == 0x30 and sx.ste2 == 0x33:
                    self.error_text  += f"sx.STE1 == 0x30 - command is OK AND sx.STE2 == 0x33 - make Z report\n"
                elif sx.ste1 == 0x34 and sx.ste2 == 0x32:
                    self.error_text  += f"sx.STE1 == 0x34 - Opened fiscal receipt AND sx.STE2 == 0x32 - command Illegal in current context\n"
                else:
                    # self.error_text  += (sx.message + " STE1=" + str(sx.ste1) + " STE2=" + str(sx.ste2) + '\n')
                    self.error_text  += f"{sx} STE1= {sx.ste1} STE2= {sx.ste2}\n"
            elif sx.code == SErrorType.ServerDefsMismatch:
                self.error_text  += f"The current library version and server definitions version do not match\n"
            elif sx.code == SErrorType.ServMismatchBetweenDefinitionAndFPResult:
                self.error_text  += f"The current library version and the fiscal device firmware is not matching\n"
            elif sx.code == SErrorType.ServerAddressNotSet:
                self.error_text  += f"Specify server ServerAddress property\n"
            elif sx.code == SErrorType.ServerConnectionError:
                self.error_text  += f"Connection from this app to the server is not established\n"
            elif sx.code == SErrorType.ServSockConnectionFailed:
                self.error_text  += f"When the server can not connect to the fiscal device\n"
            elif sx.code == SErrorType.ServTCPAuth:
                self.error_text  += f"Wrong device TCP password\n"
            elif sx.code == SErrorType.ServWaitOtherClientCmdProcessingTimeOut:
                self.error_text  += f"Processing of other clients command is taking too long\n"
            else:
                self.error_text  += f'{msg}'
        else:
            self.error_text  += f'{msg} \n'
        print(self.error_text)

StartAPP = False
class Status:
    if StartAPP:
        StartAPP = True
    else:
        try:
            fp = FP_Tremol()
            fp.ReadStatus()
            """
                - FM_Read_only - FM Read only  ( ST3.0 or ST3.1 or ST3.2 )
                - Power_down_in_opened_fiscal_receipt - Power down in opened fiscal receipt
                - Printer_not_ready_or_overheated - Printer not ready or overheated
                - Incorrect_time - Incorrect time
                - Incorrect_date - Incorrect date
                - RAM_reset - RAM reset
                - Date_and_time_hardware_error - Date and time hardware error
                - Printer_not_ready_or_no_paper - Printer not ready or no paper
                - Reports_registers_overflow - Reports registers overflow
                - Blocking_after_24_hours - Blocking after 24 hours
                - Non_zero_daily_report - Non-zero daily report
                - Non_zero_article_report - Non-zero article report
                - Non_zero_operator_report - Non-zero operator report
                - Non_printed_copy - Non-printed copy
                - Opened_Non_fiscal_Receipt - Opened Non-fiscal Receipt
                - Opened_Fiscal_Receipt - Opened Fiscal Receipt
                - Standard_Cash_Receipt - Standard Cash Receipt
                - VAT_included_in_the_receipt - VAT included in the receipt
                - Invoice - Invoice
                - EJ_near_full - EJ near full
                - EJ_full - EJ full
                - No_FM_module - No FM module
                - FM_error - FM error
                - FM_full - FM full
                - FM_near_full - FM near full
                - Decimal_point - Decimal point (1=fract, 0=whole)
                - FM_fiscalized - FM fiscalized
                - FM_produced - FM produced
                - Printer_automatic_cutting - Printer: automatic cutting
                - External_Display_Management - External Display Management
                - Brief_or_Detailed_EJ - Brief or Detailed EJ
                - Drawer_automatic_opening - Drawer: automatic opening
                - Customer_logo_included_in_the_receipt - Customer logo included in the receipt
            """

            FM_Read_only = fp.response_text.FM_Read_only
            Power_down_in_opened_fiscal_receipt = fp.response_text.Power_down_in_opened_fiscal_receipt
            Printer_not_ready_or_overheated = fp.response_text.Printer_not_ready_or_overheated
            Incorrect_time = fp.response_text.Incorrect_date
            Incorrect_date = fp.response_text.Incorrect_date
            RAM_reset = fp.response_text.RAM_reset
            Date_and_time_hardware_error = fp.response_text.Date_and_time_hardware_error
            Printer_not_ready_or_no_paper = fp.response_text.Printer_not_ready_or_no_paper
            Reports_registers_overflow = fp.response_text.Reports_registers_overflow
            Blocking_after_24_hours = fp.response_text.Blocking_after_24_hours
            Non_zero_daily_report = fp.response_text.Non_zero_daily_report
            Non_zero_article_report = fp.response_text.Non_zero_article_report
            Non_zero_operator_report = fp.response_text.Non_zero_operator_report
            Non_printed_copy = fp.response_text.Non_printed_copy
            Opened_Non_fiscal_Receipt = fp.response_text.Opened_Non_fiscal_Receipt
            Opened_Fiscal_Receipt = fp.response_text.Opened_Fiscal_Receipt
            Standard_Cash_Receipt = fp.response_text.Standard_Cash_Receipt
            VAT_included_in_the_receipt = fp.response_text.VAT_included_in_the_receipt
            Invoice = fp.response_text.Invoice
            EJ_near_full = fp.response_text.EJ_near_full
            EJ_full = fp.response_text.EJ_full
            No_FM_module = fp.response_text.No_FM_module
            FM_error = fp.response_text.FM_error
            FM_full = fp.response_text.FM_full
            FM_near_full = fp.response_text.FM_near_full
            Decimal_point = fp.response_text.Decimal_point
            FM_fiscalized = fp.response_text.FM_fiscalized
            FM_produced = fp.response_text.FM_produced
            Printer_automatic_cutting = fp.response_text.Printer_automatic_cutting
            External_Display_Management = fp.response_text.External_Display_Management
            Brief_or_Detailed_EJ = fp.response_text.Brief_or_Detailed_EJ
            Drawer_automatic_opening = fp.response_text.Drawer_automatic_opening
            Customer_logo_included_in_the_receipt = fp.response_text.Customer_logo_included_in_the_receipt

            newLine = '<br>' if fp.isForm == True else '\n'
            AllStatus = newLine + ''\
                        'FM_Read_only:                              ' + str('FM_Read_only') + newLine + ''\
                        'Power_down_in_opened_fiscal_receipt:       ' + str(Power_down_in_opened_fiscal_receipt) + newLine + ''\
                        'Printer_not_ready_or_overheated:           ' + str(Printer_not_ready_or_overheated ) + newLine + ''\
                        'Incorrect_time:                            ' + str(Incorrect_time ) + newLine + ''\
                        'Incorrect_date:                            ' + str(Incorrect_date) + newLine + ''\
                        'RAM_reset:                                 ' + str(RAM_reset) + newLine + ''\
                        'Date_and_time_hardware_error:              ' + str(Date_and_time_hardware_error) + newLine + ''\
                        'Printer_not_ready_or_no_paper:             ' + str(Printer_not_ready_or_no_paper) + newLine + ''\
                        'Reports_registers_overflow:                ' + str(Reports_registers_overflow) + newLine + ''\
                        'Blocking_after_24_hours:                   ' + str(Blocking_after_24_hours) + newLine + ''\
                        'Non_zero_daily_report:                     ' + str(Non_zero_daily_report) + newLine + ''\
                        'Non_zero_article_report:                   ' + str(Non_zero_article_report) + newLine + ''\
                        'Non_zero_operator_report:                  ' + str(Non_zero_operator_report) + newLine + ''\
                        'Non_printed_copy:                          ' + str(Non_printed_copy) + newLine + ''\
                        'Opened_Non_fiscal_Receipt:                 ' + str(Opened_Non_fiscal_Receipt) + newLine + ''\
                        'Opened_Fiscal_Receipt:                     ' + str(Opened_Fiscal_Receipt) + newLine + ''\
                        'Standard_Cash_Receipt:                     ' + str(Standard_Cash_Receipt) + newLine + ''\
                        'VAT_included_in_the_receipt:               ' + str(VAT_included_in_the_receipt) + newLine + ''\
                        'Invoice:                                   ' + str(Invoice) + newLine + ''\
                        'EJ_near_full:                              ' + str(EJ_near_full) + newLine + ''\
                        'EJ_full:                                   ' + str(EJ_full) + newLine + ''\
                        'No_FM_module:                              ' + str(No_FM_module) + newLine + ''\
                        'FM_error:                                  ' + str(FM_error) + newLine + ''\
                        'FM_full:                                   ' + str(FM_full) + newLine + ''\
                        'FM_near_full:                              ' + str(FM_near_full) + newLine + ''\
                        'Decimal_point:                             ' + str(Decimal_point) + newLine + ''\
                        'FM_fiscalized:                             ' + str(FM_fiscalized) + newLine + ''\
                        'FM_produced:                               ' + str(FM_produced) + newLine + ''\
                        'Printer_automatic_cutting:                 ' + str(Printer_automatic_cutting) + newLine + ''\
                        'External_Display_Management:               ' + str(External_Display_Management) + newLine + ''\
                        'Brief_or_Detailed_EJ:                      ' + str(Brief_or_Detailed_EJ) + newLine + ''\
                        'Drawer_automatic_opening:                  ' + str(Drawer_automatic_opening) + newLine + ''\
                        'Customer_logo_included_in_the_receipt:     ' + str(Customer_logo_included_in_the_receipt) + newLine
        except Exception as ex:
            print(ex)

