# -*- coding: utf-8 -*-
import pickle
import random
import os
from CONSTANT import *
from datetime import datetime


def create_unique_file(path):
    # Verificăm dacă calea specificată există ca director
    if not os.path.isdir(path):
        # Dacă calea nu există, o creăm
        os.makedirs(path)

    # Obțineți data curentă în formatul dorit
    current_date = datetime.now().strftime("%Y%m%d")

    # Verificăm dacă fișierul cu data curentă există deja în calea specificată
    file_exists = True
    file_count = 0
    new_file_name = f"{current_date}.txt"

    while file_exists:
        if os.path.exists(os.path.join(path, new_file_name)):
            file_count += 1
            new_file_name = f"{current_date}-{file_count}.txt"
        else:
            file_exists = False

    # Creați fișierul în calea specificată
    file_path = os.path.join(path, new_file_name)
    with open(file_path, 'w') as file:
        pass
        # Doar creăm fișierul, nu scriem nimic în el aici

    return f'{path}\\{new_file_name}'


def append_text_to_file(file_name, text):
    with open(file_name, 'a') as file:
        file.write(f'{text}\n')


class Emulator:
    def __init__(self, p_current_path):
        self.TypeProtocol = 0
        self.TypeModel = 0

        self.nr_fp_check = 1000
        self.fiscal_check_open = False
        self.non_fiscal_check_open = False

        self.file_check_name = create_unique_file(f'{p_current_path}\\VCHECK')

        self.check_sum_total = 0
        self.check_sum_pay_type = 0
        self.start_total = True

        self.pay_type_list = {
            0: 'NUMERAR',
            1: 'CARD',
            2: 'CREDIT',
            3: 'TICHETE MASA',
            4: 'TICHETE VALORICE',
            5: 'VOUCHER',
            6: 'PLATA MODERNA',
            7: 'CARD + AVANS IN NUMERAR',
            8: 'ALTE METODE',
            9: 'Foreign currency'
        }

    def OpenPortL(self, p_id, p_com, p_baudrate):
        v_res = True
        return v_res

    def Send(self, p_id, p_cmd, p_prm, p_rsp):
        v_res = (False, '-100105\t')

        if p_cmd == 74:
            v_res = (True, f'0\t-------\t')

        return v_res

    def SendEx(self, p_id, p_cmd, p_prm, p_rsp):
        v_res = (False, '-100105\t')

        if p_cmd == 33:
            v_res = (True, '0\t33\t')
        elif p_cmd == 35:
            v_res = (True, '0\t35\t')
        elif p_cmd == 38:
            if not self.non_fiscal_check_open:
                self.non_fiscal_check_open = True
                v_res = (True, f'0\t{self.nr_fp_check}\t')
                append_text_to_file(self.file_check_name, '===============================')
                append_text_to_file(self.file_check_name, 'Bon de serviciu Virtual')
                append_text_to_file(self.file_check_name, f'\t\tNr Bon {self.nr_fp_check}')
                append_text_to_file(self.file_check_name, f'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            else:
                v_res = (False, '-111046\t')
        elif p_cmd == 39:
            if self.non_fiscal_check_open:
                self.non_fiscal_check_open = False
                v_res = (True, f'0\t{self.nr_fp_check}\t')
                self.nr_fp_check += 1
                append_text_to_file(self.file_check_name, f'\t\tBON SERVICIU')
                append_text_to_file(self.file_check_name, f'===============================\n')
            else:
                v_res = (False, '-111046\t')
        elif p_cmd == 42:
            v_res = (True, '0\t')
            v_param = str(p_prm).split('\t')
            v_param = v_param[0].replace('\\t', '')
            append_text_to_file(self.file_check_name, f'{v_param}')
        elif p_cmd == 44:
            v_res = (True, '0\t')
        elif p_cmd == 45:
            v_res = (True, '0\t')
        elif p_cmd == 46:
            append_text_to_file(self.file_check_name, '1111111')
            v_res = (True, '0\t')
        elif p_cmd == 47:
            v_res = (True, '0\t')
        elif p_cmd == 48:
            if not self.fiscal_check_open:
                self.fiscal_check_open = True
                v_res = (True, f'0\t{self.nr_fp_check}\t29\t7\t')
                append_text_to_file(self.file_check_name, '===============================')
                append_text_to_file(self.file_check_name, 'Bon Fiscal Virtual')
                append_text_to_file(self.file_check_name, f'Nr Bon {self.nr_fp_check}')
                append_text_to_file(self.file_check_name, f'\n------------------------------')
            else:
                v_res = (False, '-111047\t')
        elif p_cmd == 49:
            if self.fiscal_check_open:
                v_res = (True, f'0\t{self.nr_fp_check}\t29\t7\t')
                v_param = str(p_prm).split('\t')
                print(v_param)
                self.check_sum_total += float(v_param[2])*float(v_param[3])
                append_text_to_file(self.file_check_name, f'{v_param[0]}')
                append_text_to_file(self.file_check_name, f'\t\t\t{v_param[3]}{v_param[7]} '
                                                          f'x {v_param[2]} = {float(v_param[2])*float(v_param[3])}')
            else:
                v_res = (False, '-111016\t')
        elif p_cmd == 53:
            if self.fiscal_check_open:
                v_res = (True, '0\tD\t0.00\t')
                v_param = str(p_prm).split('\t')
                if self.start_total:
                    append_text_to_file(self.file_check_name, f'TOTAL: \t\t {self.check_sum_total}')
                    self.start_total = False
                append_text_to_file(self.file_check_name, f'  {self.pay_type_list[int(v_param[0])]}\t\t{v_param[1]}')
            else:
                v_res = (False, '-111016\t')
        elif p_cmd == 54:
            if self.fiscal_check_open:
                v_res = (True, '0\t')
                v_param = str(p_prm).split('\t')
                v_param = v_param[0].replace('\\t', '')
                append_text_to_file(self.file_check_name, f'{v_param}')
            else:
                v_res = (False, '-111016\t')
        elif p_cmd == 56:
            if self.fiscal_check_open:
                self.fiscal_check_open = False
                v_res = (True, f'0\t{self.nr_fp_check}\t29\t7\t')
                self.nr_fp_check += 1
                append_text_to_file(self.file_check_name, f'\t\tBON FISCAL')
                append_text_to_file(self.file_check_name, f'===============================\n')
            else:
                v_res = (False, '-111016\t')
        elif p_cmd == 60:
            if self.fiscal_check_open:
                v_res = (True, '0\t')
            else:
                v_res = (False, '-111016\t')
        elif p_cmd in (61, 62):
            v_res = (True, '0\t04-07-23 07:36:03 DST\t')
        elif p_cmd == 65:
            v_res = (True, '0\t29\t0.00\t0.00\t0.00\t0.00\t0.00\t0.00\t0.00\t')
        elif p_cmd == 69:
            v_res = (True, '0\t')
        elif p_cmd == 70:
            v_res = (True, f'0\t{p_prm}\t{p_prm}\t0.00\t')
        elif p_cmd == 74:
            v_res = (True, '0\t74\t')
        elif p_cmd == 84:
            v_res = (True, '0\t')
        elif p_cmd == 100:
            v_param = str(p_prm).replace("\t", "")
            v_res = (True, f'{LIST_ERR[v_param]}\t')
        elif p_cmd == 106:
            v_res = (True, '0\t1\t')
        elif p_cmd == 117:
            v_res = (True, '0\t')
        elif p_cmd == 124:
            v_res = (True, '0\t21-06-23 00:00:00 DST\t21-06-23 23:00:00 DST\t0\t3857\t0\t3860\t')
        elif p_cmd == 125:
            v_param = p_prm.split('\t')

            if int(v_param[0]) == 0:
                if int(v_param[1]) == 3857:
                    v_res = (True, '0\t3857\t0\t3857\t21-06-23 07:56:44 DST\t5\t17\t')
                if int(v_param[1]) == 3858:
                    v_res = (True, '-100100\t3858\t0\t3858\t21-06-23 07:56:44 DST\t5\t10\t')
                if int(v_param[1]) == 3859:
                    v_res = (True, '0\t3859\t0\t3859\t21-06-23 07:56:44 DST\t5\t13\t')
                if int(v_param[1]) == 3860:
                    v_res = (True, '0\t3860\t0\t3860\t21-06-23 07:56:44 DST\t5\t9\t')

                with open("variabila.pkl", "wb") as f:
                    pickle.dump(int(v_param[1]), f)
            elif int(v_param[0]) == 1:
                with open("variabila.pkl", "rb") as f:
                    v_nrc = pickle.load(f)
                g_check = {
                    0: (True, f'0\t0== 26°C {v_nrc}\t'),
                    1: (True, f'0\t1=== ппп о {v_nrc}\t'),
                    2: (True, f'0\tC0H : DFH АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ {v_nrc}\t'),
                    3: (True, f'0\t3==== {v_nrc}\t'),
                    4: (True, f'0\t4==== {v_nrc}\t'),
                    5: (True, f'0\t5==== {v_nrc}\t'),
                    6: (True, f'0\t6==== {v_nrc}\t'),
                    7: (True, f'0\t7==== {v_nrc}\t'),
                    8: (True, f'0\t8==== {v_nrc}\t'),
                    9: (True, f'0\t9==== {v_nrc}\t'),
                    10: (True, f'0\t10==== {v_nrc}\t'),
                    11: (True, '-100003\t')
                }
                v_res = g_check[random.randint(0, 11)]
            elif int(v_param[0]) == 3:
                v_res = (True, '0\t')

        return v_res

    def ClosePort(self):
        pass

