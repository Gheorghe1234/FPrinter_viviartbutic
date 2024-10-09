# -*- coding: utf-8 -*-
# Created by Nicolae Gaidarji at 15.04.2022
import logging
import os
import sys
import re
import zpl
import socket

from CONSTANT import *
from uis.Form_GoDex_simple import *
from DB.conn import DB_Method
from datetime import datetime, timedelta
from UNA_Support.config_util import * 


def get_conf_env(p_env, p_env_default):
    try:
        v_result = config.conf.get(p_env[0], p_env[1])
    except Exception:
        v_default = p_env[0]
        logg_main.info(f'Set Default ENV {v_default}')
        print(f'Set Default ENV {v_default}')
        print(p_env_default)
        v_result = p_env_default

    return v_result


def format_text_new_line(p_text, p_width=70):
    v_text = p_text.replace(', ', ',')
    v_text = v_text.replace(',', ', ')

    v_step = 0
    v_counter = 0
    v_text2 = ''
    v_text_temp = ''

    for row in v_text:
        v_step += 1
        v_counter += 1

        v_text_temp = v_text_temp + row
        if len(v_text_temp) == p_width and row == ' ':
            v_step = 0
            v_text2 = v_text2 + v_text_temp + '\n'
            v_text_temp = ''
        if row == '\n':
            v_step = 0
            v_text2 = v_text2 + v_text_temp
            v_text_temp = ''
        if len(v_text_temp) == p_width and row != ' ':
            v_pos_space = v_text_temp.rfind(' ')
            v_text2 = v_text2 + v_text_temp[:v_pos_space] + '\n'
            v_text_temp = v_text_temp[v_pos_space + 1:]
            v_step = 0

    return v_text2


def format_text_new_line2(p_text, p_width=70):
    v_text = p_text.replace('\n', ' ')

    v_text2 = ''

    v_step = p_width
    v_len_t = int(len(v_text) / v_step) + 1

    for x in range(0, v_len_t):
        v_start = x * v_step
        v_end = (1 + x) * v_step
        v_text2 += v_text[v_start:v_end] + '\n'

    return v_text2


def format_text_new_line3(p_text, p_width=70):
    v_text = p_text.replace(', ', ',')
    v_text = v_text.replace(',', ', ')

    v_step = 0
    v_counter = 0
    v_text2 = ''
    v_text_temp = ''

    for row in v_text:
        v_step += 1
        v_counter += 1

        v_text_temp = v_text_temp + row
        v_is_upper = sum(map(str.isupper, v_text_temp))
        v_is_lower = len(v_text_temp) - v_is_upper
        v_len_row = v_is_lower + (v_is_upper * 2.3)
        # print(v_len_row)
        if (p_width - 1.5 < v_len_row < p_width + 1.5) and row == ' ':
            print(1, v_len_row)
            print(v_text_temp)
            v_step = 0
            v_text2 = v_text2 + v_text_temp + '\n'
            v_text_temp = ''
        if row == '\n':
            print(2, v_len_row)
            print(v_text_temp)
            v_step = 0
            v_text2 = v_text2 + v_text_temp
            v_text_temp = ''
        if (p_width - 0.5 < v_len_row < p_width + 1.5) and row != ' ':
            print(3, v_len_row)
            print(v_text_temp)
            v_pos_space = v_text_temp.rfind(' ')
            v_text2 = v_text2 + v_text_temp[:v_pos_space] + '\n'
            v_text_temp = v_text_temp[v_pos_space + 1:]
            v_step = 0

    return v_text2


class _mainFrame(mainForm):
    def __init__(self, arg, p_ip_fp="192.168.0.75"):
        logg_main.info(f'Form init _mainFrame, [{p_ip_fp}]')
        mainForm.__init__(self, arg)

        #self.cb_format_sticker.AppendItems(['56x127', '56x90', '58x40'])
        self.cb_format_sticker.AppendItems(['viviartbutic'])
        self.cb_format_sticker.SetSelection(v_default_template_id)

        self.et_ip.Value = p_ip_fp
        self.et_port.Value = '9100'
        self.sp_qnt_prn.Value = 1

        self.setting_format = False

        self.sticker = zpl.Label(90, 57)  # default sticker size

        self.name_p = ''
        self.ingrediente = ''
        self.fabricat = ''
        self.proteine = ''
        self.grasimi = ''
        self.glucide = ''
        self.valoarea_energetica = ''
        self.termen_de_valabilitate = ''
        self.barcode_p = ''
        self.price_p = ''
        self.masa_p = ''
        self.total_p = ''
        self.free_text = ''
        self.grasimi_2 = ''
        self.grasimi_3 = ''
        self.glucide_2 = ''
        self.fibre = ''
        self.sare = ''
        self.temperatura = ''
        self.data_fabricarii = ''
        self.data_expirarii = ''
        self.termen_de_valabilitate_ore = 0
        self.eda_saturated_fatty_acids = 0
        self.eda_unsaturated_fatty_acids = 0
        self.eda_sugar = 0
        self.eda_fiber = 0
        self.eda_salt = 0
        self.proc_energycost = 0
        self.proc_protein = 0
        self.proc_jir = 0
        self.proc_saturated_fatty_acids = 0
        self.proc_unsaturated_fatty_acids = 0
        self.proc_uglevod = 0
        self.proc_sugar = 0
        self.proc_fiber = 0
        self.proc_salt = 0
        self.frozen = 0
        self.vesovoi = 0
                    #viviartbutic
        self.vivi_name = ''
        self.vivi_barcode = 0
        self.vivi_price = 0
        self.vivi_size = ''

        if v_db_name == "viviartbutic":
            self.fill_date_vivi()
        else:
            self.fill_date_from_db()

        self.is_preview = True
        self.text_template = ''

        logg_main.info(f'Name SC: {self.name_p.upper()}')
        self.st_name_tvr.Label = self.name_p.upper()[:50]

        self.set_ip_from_selected_template()

    def set_ip_from_selected_template(self):
        if self.cb_format_sticker.GetSelection() == 0:
            #self.et_ip.Value = v_fp_ip_56x127
        #elif self.cb_format_sticker.GetSelection() == 1:
            #self.et_ip.Value = v_fp_ip_58x90
        #elif self.cb_format_sticker.GetSelection() == 2:
            self.et_ip.Value = v_fp_ip_vivi
        else:
            self.et_ip.Value = v_fp_ip

    def fill_date_vivi(self):
        logg_main.info(f'call fill_date_vivi')
        date_from_sc = DB_CONNECTOR.get_date_product(g_sc)
        print(date_from_sc)
        date_from_sc = date_from_sc[0]

        logg_main.info(f'date_from_sc: {date_from_sc}')
        self.vivi_barcode = date_from_sc[3]
        self.vivi_name = date_from_sc[0]
        self.vivi_size = date_from_sc[1]
        self.vivi_price = date_from_sc[2]

    def fill_date_from_db(self):
        logg_main.info(f'call fill_date_from_db')
        date_from_sc = DB_CONNECTOR.get_date_product(g_sc)
        #print(date_from_sc)
        date_from_sc = date_from_sc[0]

        logg_main.info(f'date_from_sc: {date_from_sc}')

        self.name_p = date_from_sc[0]
        self.ingrediente = f'{date_from_sc[1]}\n'
        self.fabricat = date_from_sc[2]
        self.proteine = date_from_sc[3]
        self.grasimi = date_from_sc[4]
        self.glucide = date_from_sc[5]
        self.valoarea_energetica = date_from_sc[6]
        self.termen_de_valabilitate = str(date_from_sc[7])
        self.barcode_p = date_from_sc[8]
        self.price_p = date_from_sc[16]
        self.masa_p = f'{date_from_sc[15]} kg'
        self.total_p = float(date_from_sc[16]) * float(date_from_sc[15])
        # self.total_p = 0
        self.free_text = ''
        self.grasimi_2 = date_from_sc[9]
        self.grasimi_3 = date_from_sc[10]
        self.glucide_2 = date_from_sc[11]
        self.fibre = date_from_sc[12]
        self.sare = date_from_sc[13]
        self.temperatura = date_from_sc[14]

        self.termen_de_valabilitate_ore = re.findall(r'\d+', self.termen_de_valabilitate)

        self.termen_de_valabilitate_ore = int(self.termen_de_valabilitate_ore[0])

        if self.termen_de_valabilitate.lower().find('ore'):
            self.termen_de_valabilitate_ore = self.termen_de_valabilitate_ore
        elif self.termen_de_valabilitate.lower().find('zile'):
            self.termen_de_valabilitate_ore = self.termen_de_valabilitate_ore * 24
        elif self.termen_de_valabilitate.lower().find('luni') or self.termen_de_valabilitate.lower().find('luna'):
            self.termen_de_valabilitate_ore = (self.termen_de_valabilitate_ore + 30) * 24
        else:
            self.termen_de_valabilitate_ore = self.termen_de_valabilitate_ore

        v_now = datetime.now()
        # v_data_fabricarii = v_now.strftime(DATETIME_FORMAT)
        v_data = str(self.dp_date.Value)[:10]
        v_timp = str(self.tp_time.Value)[11:]
        v_data_fabricarii = v_data + ' ' + v_timp[:5]

        if len(v_timp) == 7:
            v_timp = f'0{v_timp}'

        dt_tuple = tuple([int(v_data[6:10]), int(v_data[3:5]), int(v_data[:2]), int(v_timp[:2]), int(v_timp[3:5])])
        v_data_fabricarii_2 = datetime(*dt_tuple)

        # v_data_expirarii = datetime.strptime(v_data_fabricarii, DATETIME_FORMAT)
        v_data_expirarii = v_data_fabricarii_2
        v_data_expirarii = v_data_expirarii + timedelta(hours=self.termen_de_valabilitate_ore)
        v_data_expirarii = v_data_expirarii.strftime(DATETIME_FORMAT)
        self.data_fabricarii = v_data_fabricarii
        self.data_expirarii = v_data_expirarii

        self.eda_saturated_fatty_acids = date_from_sc[17]
        self.eda_unsaturated_fatty_acids = date_from_sc[18]
        self.eda_sugar = date_from_sc[19]
        self.eda_fiber = date_from_sc[20]
        self.eda_salt = date_from_sc[21]
        self.proc_energycost = date_from_sc[22]
        self.proc_protein = date_from_sc[23]
        self.proc_jir = date_from_sc[24]
        self.proc_saturated_fatty_acids = date_from_sc[25]
        self.proc_unsaturated_fatty_acids = date_from_sc[26]
        self.proc_uglevod = date_from_sc[27]
        self.proc_sugar = date_from_sc[28]
        self.proc_fiber = date_from_sc[29]
        self.proc_salt = date_from_sc[30]
        self.frozen = date_from_sc[31]
        self.vesovoi = date_from_sc[32]

    def get_zpl_sticker(self):
        v_sticker_format = self.cb_format_sticker.GetItems()[self.cb_format_sticker.GetSelection()]
        if v_db_name == "viviartbutic":
            self.fill_date_vivi()
        else:
            self.fill_date_from_db()

        logg_main.info(f'v_sticker_format: {v_sticker_format}')
        if v_sticker_format == 'viviartbutic':
            self.create_label_viviartbutic()
            self.setting_format =True
        """
        if v_sticker_format == '56x127':
            self.create_label_56x127()
            self.setting_format = True
        elif v_sticker_format == '58x40':
            self.create_label_58x40_viviartbutic()
            self.setting_format = True
        elif v_sticker_format == '56x90':
            self.create_label_56x90()
            self.setting_format = True"""

        self.get_setting_format(v_sticker_format)

    def create_label_56x127(self):
        logg_main.info(f'create_label_56x127 ')
        self.sticker = zpl.Label(90, 57)
        v_free_text = str(self.free_text)
        v_print_qnt = int(self.sp_qnt_prn.Value)

        v_max_len = 41
        v_name_len = len(self.name_p)
        v_name_p = str(self.name_p)[:v_max_len]
        v_diff_name_len = v_max_len - v_name_len
        if v_diff_name_len > 0:
            print(v_diff_name_len)
            v_len = v_diff_name_len / 2
            v_pref = ' ' * int(v_len)
            v_suf = ' ' * int(v_len + 1)
            v_name_p = v_pref + v_name_p + v_suf

        v_data_expirarii = '{:0>4}'.format(self.termen_de_valabilitate_ore / 24)
        v_barcode = self.barcode_p

        if len(v_barcode) <= 5:
            v_barcode = '22' + '{:0>5}'.format(v_barcode) + '00000'

        if self.vesovoi == 0:
            v_total_txt = ''
            v_price_txt = ''
        else:
            v_total_txt = f"""VA,304,316,1,1,0,3E,Total
VA,331,336,1,1,0,3E,{self.total_p} Lei"""
            v_price_txt = f'AA,263,481,1,1,0,3E,Pret:             {self.price_p}'

        v_ingrediente_txt = ''
        if len(self.ingrediente) < 1800:
            pair_list = format_text_new_line3(self.ingrediente, 81).split("\n")
            # pair_list = format_text_new_line(self.ingrediente, 72).split("\n")
        else:
            pair_list = format_text_new_line2(self.ingrediente, 74).split("\n")

        v_i = 0
        for pair in pair_list:
            v_x = 28 + (v_i * 15)
            v_ingrediente_txt += f'AA,{v_x},{v_x_cord_ingred},1,1,0,3E,{pair}\n'
            v_i += 1

        # verificarea daca produsul este congelat,
        # in dependenta de tip produs printam text termen de valabilitate diferit
        if self.temperatura is not None:
            self.temperatura = self.temperatura.replace('±', '+/-').replace('°', ' ')
        else:
            self.temperatura = self.temperatura

        if self.frozen == 0:
            v_frozen = f'''AA,25,203,1,1,0,3,Durata si conditii de 
AA,44,203,1,1,0,3,pastrare: {self.termen_de_valabilitate}  
AA,63,203,1,1,0,3,la temperatura  {self.temperatura}
'''
        else:
            v_frozen = f'''AA,25,203,1,1,0,3,Durata si conditii de pastrare:
AA,44,203,1,1,0,3,{self.termen_de_valabilitate} la temperatura -18 
AA,63,203,1,1,0,3,grade C, umiditatea relativa a 
AA,82,203,1,1,0,3,aerului 85%. A se consuma 
AA,101,203,1,1,0,3,dupa decongelare, a se 
AA,120,203,1,1,0,3,decongela la temperatura 
AA,139,203,1,1,0,3,camerei. Dupa decongelare 
AA,158,203,1,1,0,3,a se pastra la frigider 48 ore 
AA,177,203,1,1,0,3,la temperatura de {self.temperatura}
AA,196,203,1,1,0,3,Produsul nu se recongeleaza.'''

        self.text_template = f"""
^Q{v_template_q}
^W{v_template_w}
^H8
^P{v_print_qnt}
^S4
^AD
^C1
^R0
~Q+0
^O0
^D0
^E18
~R255
^L
Dmnddy4
Th:m:s
R55,141,244,425,1,1
AA,95,423,1,1,0,3E,Proteine:                          {self.proteine}            {self.proc_protein}
AA,114,423,1,1,0,3E,Grasimi:                         {self.grasimi}          {self.proc_jir}
AA,133,423,1,1,0,3E,din care acizi grasi          {self.eda_saturated_fatty_acids}          {self.proc_saturated_fatty_acids}
AA,152,423,1,1,0,3E,acizi grasi trans                {self.eda_unsaturated_fatty_acids}
AA,171,423,1,1,0,3E,Glucide:                             {self.glucide}         {self.proc_uglevod}
AA,190,423,1,1,0,3E,din care zaharuri               {self.eda_sugar}        {self.proc_sugar}
AA,209,423,1,1,0,3E,Fibre alimentare:               {self.eda_fiber}           {self.proc_fiber}
AA,228,423,1,1,0,3E,Sare:                                 {self.eda_salt}          {self.proc_salt}
AA,60,422,1,1,0,3E,Declaratia nutritionala: per 100gr    CR%
AA,79,422,1,1,0,3E,Valoarea Energetica:  {self.valoarea_energetica}Kcal     {self.proc_energycost}
BE,376,138,3,10,100,2,3,{v_barcode}
{v_ingrediente_txt}
AA,290,429,1,1,0,3,Conditii de pastrare: {self.temperatura}
AA,309,428,1,1,0,3E,Masa neta:   {self.masa_p}
AA,252,428,1,1,0,3E,Data fabricarii:
AA,269,428,1,1,0,3E,Data expirarii:
Ddd/me/y4
Th:m:s
AA,251,319,1,1,0,3E,{self.data_fabricarii}
Ddd/me/y4
Th:m:s
AA,270,319,1,1,0,3E,{self.data_expirarii}
AA,329,428,1,1,0,3E,Lot Nr.
Lo,57,272,246,272
Y0,48,Image10
Lo,57,196,246,196


Lo,113,142,113,425
Lo,96,142,96,425
Lo,78,142,78,425
Lo,169,141,169,424
Lo,206,141,206,424
Lo,226,140,226,423
Dmnddy4
AA,329,351,1,1,0,3E,^D
AC,2,1010,1,1,0,3E,{v_name_p}
Y361,111,WindowText13
E

"""
        logg_main.info(f'text_template {self.text_template}')

    def create_label_58x40(self):
        logg_main.info(f'create_label_58x40 ')
        v_print_qnt = int(self.sp_qnt_prn.Value)

        v_max_len = 35
        v_name_len = len(self.name_p)
        v_name_p = str(self.name_p)[:v_max_len]
        v_diff_name_len = v_max_len - v_name_len
        if v_diff_name_len > 0:
            print(v_diff_name_len)
            v_len = v_diff_name_len / 2
            v_pref = ' ' * int(v_len)
            v_suf = ' ' * int(v_len + 1)
            v_name_p = v_pref + v_name_p + v_suf

        v_barcode = self.barcode_p

        if len(v_barcode) <= 5:
            v_barcode = '22' + '{:0>5}'.format(v_barcode) + '00000'

        self.text_template = f'''

^Q40,3
^W58
^H8
^P{v_print_qnt}
^S4
^AD
^C1
^R0
~Q+0
^O0
^D0
^E18
~R255
^XSET,ROTATION,0
^L
Ddd/me/y4
Th:m:s
Ddd/me/y4
Th:m:s
BE,70,90,3,7,42,0,1,{v_barcode}
Lo,0,162,463,165
AA,109,53,1,1,0,0,Data fabricarii:
AA,109,70,1,1,0,0,Data expirarii:
Ddd/me/y4
Th:m:s
AA,218,52,1,1,0,0,{self.data_fabricarii}
Ddd/me/y4
Th:m:s
AA,218,71,1,1,0,0,{self.data_expirarii}
Y152,169,{v_img_name_58x40}
AA,106,213,1,1,0,0,Data fabricarii:
AA,106,230,1,1,0,0,Data expirarii:
Ddd/me/y4
Th:m:s
AA,215,212,1,1,0,0,{self.data_fabricarii}
Ddd/me/y4
Th:m:s
AA,215,231,1,1,0,0,{self.data_expirarii}
BE,70,250,3,7,42,0,1,{v_barcode}
Y152,9,{v_img_name_58x40}
AT,1,20,31,31,0,0,0,0,{v_name_p}
AT,1,182,31,31,0,0,0,0,{v_name_p}
E

        '''
        logg_main.info(f'text_template {self.text_template}')
#############################################################################################################
    def create_label_viviartbutic(self):
        logg_main.info(f'create_label_viviartbutic')

        vivi_print_qnt = int(self.sp_qnt_prn.Value)

        if len(self.vivi_name) > 23:
            vivi_name_line1 = self.vivi_name[:23]
            vivi_name_line2 = self.vivi_name[23:]
            name_template = f"AD,5,130,1,1,0,0,{vivi_name_line1}\nAD,5,170,1,1,0,0,{vivi_name_line2}"
        else:
            name_template = f"AD,5,130,1,1,0,0,{self.vivi_name}"
        self.text_template = f'''
^Q60,3
^W57
^H5
^P{vivi_print_qnt}
^S2
^AD
^C1
^R0
~Q+0
^O0
^D0
^E40
~R255
^XSET,ROTATION,0
^L
Dy2-me-dd
Th:m:s
Dy2-me-dd
Th:m:s
AD,43,75,1,1,0,0,Vivi Art Boutique Fashion
{name_template}
AD,114,217,1,1,0,0,Marimea: {self.vivi_size}
AD,105,260,2,2,0,0,{self.vivi_price} Lei
BA3,15,339,2,6,80,0,1,{self.vivi_barcode}
E
'''


        logg_main.info(f'text_template {self.text_template}')

#############################################################################################################
    def create_label_56x90(self):
        logg_main.info(f'create_label_56x90 ')
        v_print_qnt = int(self.sp_qnt_prn.Value)

        v_max_len = 32
        v_name_len = len(self.name_p)
        v_name_p = str(self.name_p)[:v_max_len]
        v_diff_name_len = v_max_len - v_name_len
        if v_diff_name_len > 0:
            print(v_diff_name_len)
            v_len = v_diff_name_len / 2
            v_pref = ' ' * int(v_len)
            v_suf = ' ' * int(v_len + 1)
            v_name_p = v_pref + v_name_p + v_suf

        v_barcode = self.barcode_p
        if len(v_barcode) <= 5:
            v_barcode = '22' + '{:0>5}'.format(v_barcode) + '00000'

        v_ingrediente_txt = ''
        if len(self.ingrediente) < 1800:
            # pair_list = format_text_new_line3(self.ingrediente, 81).split("\n")
            pair_list = format_text_new_line(self.ingrediente, 67).split("\n")
        else:
            pair_list = format_text_new_line2(self.ingrediente, 67).split("\n")

        v_i = 0
        for pair in pair_list:
            v_x = 72 + (v_i * 16)
            v_ingrediente_txt += f'AT,{v_x_cord_ingred_56x90},{v_x},16,14,0,0,0,0,{pair}\n'
            v_i += 1

        self.text_template = f'''
^Q90
^W56
^H8
^P{v_print_qnt}
^S4
^AD
^C1
^R0
~Q+0
^O0
^D0
^E18
~R255
^XSET,ROTATION,0
^L
Ddd/me/y4
Th:m:s
Y121,10,{v_img_name_56x90}
Dy2-me-dd
Th:m:s
AA,95,540,1,1,0,0,Data fabricarii:
AA,95,555,1,1,0,0,Data expirarii:
Ddd/me/y4
Th:m:s
AA,205,540,1,1,0,0,{self.data_fabricarii}
Ddd/me/y4
Th:m:s
AA,206,555,1,1,0,0,{self.data_expirarii}
BE,55,580,3,8,44,0,1,{v_barcode}
{v_ingrediente_txt}
AT,18,32,34,34,0,0,0,0,{v_name_p}
AA,84,650,1,1,0,0,Produs si ambalat: SC Dulcinella SRL,
AA,84,665,1,1,0,0,RM, mun. Chisinau, str.Albisoara 68
AA,84,680,1,1,0,0,                 +373 22 02 58 58
AA,84,695,1,1,0,0,                 www.dulcinella.md
E

 '''
        logg_main.info(f'text_template {self.text_template}')

    def onclick_bt_preview(self, event):
        wait = wx.BusyCursor()
        print(wait)

        wx.MessageBox(f'Nu este setat Preview', LOG_CONST.Error, wx.OK | wx.ICON_ERROR)

    def onclick_bt_print(self, event):
        logg_main.info(f'onclick_bt_print')
        self.is_preview = False
        self.get_zpl_sticker()

        if self.setting_format:
            wait = wx.BusyCursor()
            logg_main.info(wait)

            mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = self.et_ip.Value
            port = int(self.et_port.Value)
            v_print_qnt = 1

            logg_main.info(f'host/port: {host}/{port}')

            try:
                # NG
                mysocket.connect((host, port))  # connecting to host
                for i in range(0, v_print_qnt):
                    # NG
                    mysocket.send(self.text_template.encode())  # using bytes
                    # print(self.text_template)
                mysocket.close()  # closing connection

                del wait
            except Exception as err:
                del wait
                logg_main.error(f'Error with the connection. \n{err}')
                wx.MessageBox(f'Error with the connection. \n{err}', LOG_CONST.Error, wx.OK | wx.ICON_ERROR)
            finally:
                sys.exit()

    def get_setting_format(self, p_sticker_format):
        logg_main.info('get_setting_format')
        if not self.setting_format:
            logg_main.warning(f'Tempoplate pentru formatul {p_sticker_format} nu este setat')
            wx.MessageBox(f'Tempoplate pentru formatul {p_sticker_format} nu este setat',
                          LOG_CONST.Info, wx.OK | wx.ICON_INFORMATION)

    def OnChoice_cb_format_sticker(self, event):
        self.set_ip_from_selected_template()
        if self.cb_format_sticker.GetSelection() == 1:
            self.bt_print.Enable(False)
        else:
            self.bt_print.Enable(True)


class _mainFrameMat(mainForm_mat):
    def __init__(self, arg, p_ip_fp="192.168.0.75"):
        logg_main.info(f'Form init _mainFrameMat, [{p_ip_fp}]')
        mainForm_mat.__init__(self, arg)

        self.cb_format_sticker_mat.AppendItems(['127x56'])
        self.cb_format_sticker_mat.SetSelection(0)

        self.cb_sc_um_mat.AppendItems(v_list_um_sc.split(','))
        self.cb_sc_um_mat.SetSelection(0)

        self.name_p = ''
        self.setting_format = False
        self.is_preview = False
        self.text_template = ''

        self.fill_date_from_db()

        self.st_name_tvr_mat.Label = self.name_p

        self.et_ip_mat.Label = v_ip_materiale_127x56
        self.et_port_mat.Label = '9100'
        self.sp_sc_cant.Label = '1'

    def fill_date_from_db(self):
        logg_main.info(f'call fill_date_from_db')
        date_from_sc = DB_CONNECTOR.get_date_product_mat(g_sc)
        date_from_sc = date_from_sc[0]

        logg_main.info(f'date_from_sc: {date_from_sc}')

        self.name_p = date_from_sc[2]

    def get_zpl_sticker(self):
        v_sticker_format = self.cb_format_sticker_mat.GetItems()[self.cb_format_sticker_mat.GetSelection()]
        self.fill_date_from_db()

        logg_main.info(f'v_sticker_format: {v_sticker_format}')

        if v_sticker_format == '127x56':
            self.create_label_127x56()
            self.setting_format = True

        self.get_setting_format(v_sticker_format)

    def create_label_127x56(self):
        logg_main.info(f'create_label_56x90 ')
        v_print_qnt = int(self.sp_qnt_prn_mat.Value)

        v_data_primit = str(self.dp_date_primit_mat.Value)[:10]
        v_data_predat = str(self.dp_date_predat_mat.Value)[:10]
        v_data_valabil = str(self.dp_date_valabilitate_mat.Value)[:10]

        v_sc_cant = self.sp_sc_cant.Value
        v_sc_um = self.cb_sc_um_mat.GetItems()[self.cb_sc_um_mat.GetSelection()]

        self.text_template = f'''
^Q127,3
^W56
^H5
^P{v_print_qnt}
^S2
^AD
^C1
^R0
~Q+0
^O0
^D0
^E12
~R0
^XSET,ROTATION,0
^L
Dy2-me-dd
Th:m:s
Y0,2,{v_img_name_material_127x56}
AD,129,670,1,1,0,3E,{self.name_p}
Dy2-me-dd
AD,236,670,1,1,0,3E,{v_data_predat}
Dy2-me-dd
AD,270,670,1,1,0,3E,{v_data_valabil}
Dy2-me-dd
AB,60,134,1,1,0,3E,{v_data_primit}
Dy2-me-dd
AD,202,670,1,1,0,3E,{v_data_primit}
AD,164,670,1,1,0,3E,{v_sc_cant}  {v_sc_um}
E

'''
        logg_main.info(f'text_template {self.text_template}')

    def onclick_bt_print_mat(self, event):
        logg_main.info(f'onclick_bt_print')
        self.is_preview = False
        self.get_zpl_sticker()

        if self.setting_format:
            wait = wx.BusyCursor()
            logg_main.info(wait)

            mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = self.et_ip_mat.Value
            port = int(self.et_port_mat.Value)
            v_print_qnt = 1

            logg_main.info(f'host/port: {host}/{port}')

            try:
                # NG
                mysocket.connect((host, port))  # connecting to host
                for i in range(0, v_print_qnt):
                    # NG
                    mysocket.send(self.text_template.encode())  # using bytes
                    # print(1)
                mysocket.close()  # closing connection

                del wait
            except Exception as err:
                del wait
                logg_main.error(f'Error with the connection. \n{err}')
                wx.MessageBox(f'Error with the connection. \n{err}', LOG_CONST.Error, wx.OK | wx.ICON_ERROR)
            finally:
                sys.exit()

    def get_setting_format(self, p_sticker_format):
        logg_main.info('get_setting_format')
        if not self.setting_format:
            logg_main.warning(f'Tempoplate pentru formatul {p_sticker_format} nu este setat')
            wx.MessageBox(f'Tempoplate pentru formatul {p_sticker_format} nu este setat',
                          LOG_CONST.Info, wx.OK | wx.ICON_INFORMATION)


def show_form(p_ip_fp):
    logg_main.info(f'[{p_ip_fp}]')
    app = wx.App()
    form_main = _mainFrame(None, p_ip_fp)
    form_main.Show()
    app.MainLoop()


def show_form_mat(p_ip_fp):
    logg_main.info(f'[{p_ip_fp}]')
    app = wx.App()
    form_main = _mainFrameMat(None, p_ip_fp)
    form_main.Show()
    app.MainLoop()


# setarea afisarii logurilor 'logging'
date_now = datetime.now().strftime("%Y%m%d")

try:
    os.makedirs(LOG_CONST.LOGSavePath)
except Exception as ex:
    pass

logging_level = 'DEBUG'

logFormatter = logging.Formatter("%(asctime)s [%(name)-27.27s] [%(levelname)-8.8s] "
                                 "F:[%(lineno)d: %(funcName)-20.20s] %(message)s",
                                 '%m-%d-%y %H:%M:%S')
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler(LOG_CONST.LOGSavePath + date_now + '_GoDex_win.log')
fileHandler.setFormatter(logFormatter)
fileHandler.setLevel(logging_level)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
rootLogger.setLevel(logging_level)

logging.getLogger('urllib3').setLevel('CRITICAL')
logging.getLogger('future_stdlib').setLevel('CRITICAL')
logging.getLogger('PIL').setLevel('CRITICAL')

logg_main = rootLogger
# ========================================================

if __name__ == '__main__':
    logg_main.info(LOG_CONST.START_APP)
    logg_main.info(version_app)

    config = CFG('setup_godex.ini')
    config.conf.add_section('Connection')
    config.conf.set('Connection', 'ip', '192.168.200.21')
    config.conf.set('Connection', 'ip_58x40', '10.124.11.66')
    #config.conf.set('Connection', 'ip_58x90', '10.124.13.66')
    #config.conf.set('Connection', 'ip_56x127', '10.124.11.66')
    config.conf.set('Connection', 'ip', '192.168.200.21')
    config.conf.set('Connection', 'oracle_dir', r'C:\oracle\instantclient_12_2')
    config.conf.set('Connection', 'template_q', '127')
    config.conf.set('Connection', 'template_w', '56')
    config.conf.set('Connection', 'x_cord_ingred', '1008')
    config.conf.set('Connection', 'img_name_58x40', 'Image0')
    config.conf.set('Connection', 'img_name_56x90', 'Image7')
    config.conf.set('Connection', 'x_cord_ingred_56x90', '10')
    config.conf.set('Connection', ';Template default: 0 - 56x127, 1 - 56x90, 2 - 58x40', '')
    config.conf.set('Connection', 'default_template_id', '0')

    config.conf.set('Connection', ';Setari pentru Forma materiale', '')
    config.conf.set('Connection', 'ip_materiale_127x56', '10.0.0.0')
    config.conf.set('Connection', 'img_name_material_127x56', 'Image10')
    config.conf.set('Connection', 'list_um_sc', 'KG,BUC,Litri')
    config.create_cfg_file()

    try:
        g_oracle_dir = r'' + config.conf.get('Connection', 'oracle_dir')
    except Exception as err:
        logg_main.error(f'eroare citire parametru oracle_dir din *.ini: {err}')
        g_oracle_dir = r'C:\oracle\instantclient_12_2'

    try:
        NAME_HOST = sys.argv[1]
        SERVER = sys.argv[2]
        ORACLE_DIR_ = sys.argv[3]
        SC = sys.argv[4]
        try:
            TYPE = sys.argv[5]
        except IndexError:
            TYPE = 'plu'

        ORACLE_DIR = g_oracle_dir
        logg_main.info(f'DB_CONNECTOR: {ORACLE_DIR}')

        v_db_name = NAME_HOST
        v_db_pass = NAME_HOST
        v_db_server = SERVER
        v_oracle_dir = ORACLE_DIR
        g_sc = SC

        logg_main.info(f'{NAME_HOST} {SERVER} {ORACLE_DIR} {SC} {TYPE}')

        DB_CONNECTOR = DB_Method(v_db_name, v_db_pass, v_db_server, v_oracle_dir)
    except Exception as err:
        logg_main.error(f' {err}')
    else:
        logg_main.info('Connect db successful')

        v_fp_ip = get_conf_env(['Connection', 'ip'], '10.124.11.01')
        v_fp_ip_vivi = '192.168.0.249'
        v_fp_ip_58x40 = get_conf_env(['Connection', 'ip_58x40'], v_fp_ip)
        #v_fp_ip_58x90 = get_conf_env(['Connection', 'ip_58x90'], v_fp_ip)
        #v_fp_ip_56x127 = get_conf_env(['Connection', 'ip_56x127'], v_fp_ip)
        v_default_template_id = int(get_conf_env(['Connection', 'default_template_id'], '0'))

        v_template_q = get_conf_env(['Connection', 'template_q'], '127')

        v_template_w = get_conf_env(['Connection', 'template_w'], '56')

        v_x_cord_ingred = get_conf_env(['Connection', 'x_cord_ingred'], '1008')

        v_x_cord_ingred_56x90 = get_conf_env(['Connection', 'x_cord_ingred_56x90'], '11')

        v_img_name_58x40 = get_conf_env(['Connection', 'img_name_58x40'], 'Image0')

        v_img_name_56x90 = get_conf_env(['Connection', 'img_name_56x90'], 'Image7')

        v_img_name_material_127x56 = get_conf_env(['Connection', 'img_name_material_127x56'], 'Image11')
        v_list_um_sc = get_conf_env(['Connection', 'list_um_sc'], 'KG,Litri,BUC')
        v_ip_materiale_127x56 = get_conf_env(['Connection', 'ip_materiale_127x56'], '10.0.0.0')

        if TYPE == 'material':
            show_form_mat(v_ip_materiale_127x56)
        elif TYPE == 'plu':
            show_form(v_fp_ip)
        else:
            logg_main.info(f'Pentru tipul indicat "{TYPE}" nu este setat operatiunea')
