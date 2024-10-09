# -*- coding: utf-8 -*-
import pickle
import random


def send_fp(p_id, p_cmd, p_param, p_c):
    v_res = None
    v_set_nr_check = 0

    if p_cmd == 124:
        v_res = (True, '0\t21-06-23 00:00:00 DST\t21-06-23 23:00:00 DST\t0\t3857\t0\t3860\t')
    elif p_cmd == 125:
        v_param = p_param.split('\t')

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


# print(str(send_fp(1, 125, '0,3858')[1]).find('\t'))
# print(send_fp(1, 125, '1'))
# print(send_fp(1, 125, '1'))


