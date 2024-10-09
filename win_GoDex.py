# -*- coding: utf-8 -*-
# Created by Nicolae Gaidarji at 15.04.2022
import zpl
import socket

from CONSTANT import *
from uis.Form_GoDex import *


v_text2 = """^XA^FO0,0^GB420,800,1,B,0^FS^FO0,240^GB420,0,1,B,0^FS^FO0,612^GB420,0,1,B,0^FS^FO0,252^A0N,30,18^FB420,1,0,C,0^FDTest produs 123456789012345678901234567890123^FS^FO0,300^APN,9,1^FB408,10,0,C,0^FDFabricat in R.^FS^FO48,468^APN,9,1^FB60,10,0,C,0^FDPret: 558,87^FS^FO108,468^APN,9,1^FB60,10,0,C,0^FDMasa: ^FS^FO204,471^A0N,30,18^FB420,1,0,L,0^FDTotal:    ^FS^FO120,510^BEN,40,Y,N^FD07000002198^FS^FO0,582^ALN,14,6^FB408,10,0,C,0^FDData Fabricarii: 27.04.2022 15:22^FS^FO0,600^ALN,15,7^FB408,10,0,C,0^FDData expirarii: 30.04.2022 15:22^FS^XZ
"""


class _mainFrame(mainForm):
    def __init__(self, arg):
        mainForm.__init__(self, arg)

        self.cb_format_sticker.AppendItems(['57x90', '58x40', '101x101'])
        self.cb_format_sticker.SetSelection(0)

        self.et_nume_produs.Value = 'Test produs 123456789012345678901234567890123'
        self.et_pret.Value = '558,87'
        self.et_barcod.Value = '07000002198'
        # self.rt_ingrediente.Value = 'Fabricat in R. Moldova. SM 238.2019 Ingrediente: Faina de griu, oua de gaina, zahar,margarin,miere,artif,bicarbonat de sodiu,smintina,frisca vegetaala miez de nuca,fulgi de cioc.,acid Valoarea nutritiva'
        self.rt_ingrediente.Value = 'faina de GRAU c/s,LAPTE pasteurizat de vaca,margarina,uleiuri vegetale rafinate si partial hidrogenate(palmier,rapita,floarea soarelui),apa,emulsifiant:(E471,lectina de SOIA),sare iodata,acidifiant(acid citric), conservant(acid sorbic,sorbat de potasiu) antioxidant (extract bogat in tocoferol,palmitat de L-asorbic),aroma,colorant(caroteni),ciocolata alba (zahar,unt de cacao,LAPTE praf,emulsifiant:lectina de SOIA,arome: vanilie naturala),frisca vegetala,apa potabila,grasime vegetala nehidrogenata(ulei de samburi de palmier,ulei de palmier),zahar,LACTOZA, proteina din LAPTE,emulgator:E420ii,E472e,E322,stabilizatori:E463, E401,aromatizator,acidifiant: fosfat monopotasic,sare alimentara,colorant beta carotene,ciocolata cu lapte (zahar,unt de cacao,LAPTE praf,masa de cacao,emulsifiant:lectina de SOIA,aroma,vanilie naturala),OUA de gaina,mere proaspete,zahar cristal,ananas conservat in sirop(ananas,apa, zahar),biscuiti(zahar,faina de GRAU,grasimi vegetale de palmier si floarea soarelui,cacao cu continut redus de grasime,amidon de porumb faina de orez,emulsifianti:lectina de SOIA,E476,aromatizatori identici celor naturali de ciocolata neagra si vanilie,amidon de cartofi,sare afanator: bicarbonat de sodiu),apa potabila,LAPTE concentrat cu zahar (LAPTE semidegresat,zahar,grasime vegetala,LACTOZA),UNT din SMANTANA dulce,amidon de cartofi,vin spumant(1%),divin(0.2%),gelifiant(amidon  modificat,dextroza),ulei de floarea soarelui,mergeluse de zahar,acidifiant: acid acetic,zahar pudra corativa,sare,aroma,vanilina'
        self.et_ip.Value = "192.168.0.75"
        self.et_port.Value = '9100'

        self.setting_format = False

        self.sticker = zpl.Label(90, 57)  # default sticker size

        self.name_p = ''
        self.price_p = ''
        self.masa_p = ''
        self.total_p = ''
        self.barcode_p = ''
        self.free_text = ''

        self.is_preview = True

    def get_zpl_sticker(self):
        v_sticker_format = self.cb_format_sticker.GetItems()[self.cb_format_sticker.GetSelection()]
        self.name_p = self.et_nume_produs.Value
        self.price_p = self.et_pret.Value
        self.masa_p = self.et_masa.Value
        self.total_p = self.et_total.Value
        self.barcode_p = self.et_barcod.Value
        self.free_text = self.rt_ingrediente.Value

        if v_sticker_format == '57x90':
            self.create_label_57x90()
            self.setting_format = True
        elif v_sticker_format == '58x40':
            pass
        elif v_sticker_format == '101x101':
            pass

        self.get_setting_format(v_sticker_format)

    def create_label_57x90(self):
        self.sticker = zpl.Label(90, 55)
        v_line1 = 5
        v_free_text = str(self.free_text)

        v_name_p = str(self.name_p)

        if self.is_preview:
            self.sticker.origin(0, 0)
            self.sticker.draw_box(420, 800)
            self.sticker.endorigin()

            # self.sticker.origin(0, 20)
            # self.sticker.draw_box(420, 0)
            # self.sticker.endorigin()

            # self.sticker.origin(0, 51)
            # self.sticker.draw_box(420, 0)
            # self.sticker.endorigin()

        self.sticker.origin(0, v_line1)
        self.sticker.write_text(v_name_p, char_height=2.5, char_width=2, max_line=2, line_width=38,
                                justification='C')  # line_width=40,
        self.sticker.endorigin()

        # self.sticker.origin(1, v_line1+5)
        # self.sticker.write_text(v_free_text, char_height=0.65, char_width=0.1, max_line=60, line_width=34,
        #                         justification='L', font='P')  # line_width=40,
        # self.sticker.endorigin()

        # v_price_suffix = self.price_p
        # v_price = f'Pret: {v_price_suffix}'
        # self.sticker.origin(4, 39)
        # self.sticker.write_text(v_price, char_height=0.75, char_width=0.1, max_line=10, line_width=5,
        #                         justification='C', font='P')  # line_width=40,
        # self.sticker.endorigin()
        #
        # v_masa_suffix = self.masa_p
        # v_masa = f'Masa: {v_masa_suffix}'
        # self.sticker.origin(9, 39)
        # self.sticker.write_text(v_masa, char_height=0.75, char_width=0.1, max_line=10, line_width=5,
        #                         justification='C', font='P')  # line_width=40,
        # self.sticker.endorigin()
        #

        # self.sticker.origin(5, 2)
        # self.sticker.write_graphic('logo2.Bmp', 4)
        # self.sticker.endorigin()
        # ================
        # self.sticker.origin(0, 54)
        # self.sticker.write_text('Data Fabricarii: 27.04.2022 15:22', char_height=1.2, char_width=0.5, max_line=10,
        #                         line_width=34,
        #                         justification='C', font='L')  # line_width=40,
        # self.sticker.endorigin()
        #
        # self.sticker.origin(0, 55)
        # self.sticker.write_text('Data expirarii: 30.04.2022 15:22', char_height=1.3, char_width=0.6, max_line=10,
        #                         line_width=34,
        #                         justification='C', font='L')  # line_width=40,
        # self.sticker.endorigin()
        #
        # self.sticker.origin(10, 56.5)
        # self.sticker.write_barcode(height=40, barcode_type='E')
        # self.sticker.write_text(self.barcode_p)
        # self.sticker.endorigin()
        #
        # self.sticker.origin(0, 62)
        # self.sticker.write_text('Produs si ambalat: SC Dulcinella SRL,',
        #                         char_height=1.2, char_width=0.5, max_line=4, line_width=34,
        #                         justification='C', font='L')  # line_width=40,
        # self.sticker.endorigin()
        #
        # self.sticker.origin(0, 63)
        # self.sticker.write_text('RM, mun. Chisinau, str.Albisoara 68',
        #                         char_height=1.2, char_width=0.5, max_line=4, line_width=34,
        #                         justification='C', font='L')  # line_width=40,
        # self.sticker.endorigin()
        #
        # self.sticker.origin(0, 64)
        # self.sticker.write_text('+373 22 02 58 58',
        #                         char_height=1.2, char_width=0.5, max_line=4, line_width=34,
        #                         justification='C', font='L')  # line_width=40,
        # self.sticker.endorigin()
        #
        # self.sticker.origin(0, 65)
        # self.sticker.write_text('www.dulcinella.md',
        #                         char_height=1.2, char_width=0.5, max_line=4, line_width=34,
        #                         justification='C', font='L')  # line_width=40,
        # self.sticker.endorigin()

    def onclick_bt_preview(self, event):
        wait = wx.BusyCursor()
        print(wait)

        self.get_zpl_sticker()

        if self.setting_format:
            # self.sticker.code = v_text2
            self.sticker.preview()
            self.write_zpl_code_result()

        del wait

    def onclick_bt_print(self, event):
        self.is_preview = False
        self.get_zpl_sticker()
        if self.setting_format:
            wait = wx.BusyCursor()
            print(wait)
            self.write_zpl_code_result()

            mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = self.et_ip.Value
            port = int(self.et_port.Value)
            try:
                mysocket.connect((host, port))  # connecting to host
                mysocket.send(self.sticker.dumpZPL())  # using bytes
                mysocket.close()  # closing connection

                del wait
            # except Exception as err:
            except KeyboardInterrupt as err:
                del wait
                wx.MessageBox(f'Error with the connection. \n{err}', LOG_CONST.Error, wx.OK | wx.ICON_ERROR)
                print("Error with the connection")

    def write_zpl_code_result(self):
        self.rt_result.Value = self.sticker.dumpZPL()

    def get_setting_format(self, p_sticker_format):
        if not self.setting_format:
            wx.MessageBox(f'Tempoplate pentru formatul {p_sticker_format} nu este setat',
                          LOG_CONST.Info, wx.OK | wx.ICON_INFORMATION)


def show_form():
    app = wx.App()
    form_main = _mainFrame(None)
    form_main.Show()
    app.MainLoop()


show_form()
