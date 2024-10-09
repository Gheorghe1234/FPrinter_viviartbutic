# -*- coding: utf-8 -*-
# Created by Nicolae Gaidarji at 31.10.2022
import sys
import logging

from CONSTANT import *
from DB.conn import DB_Method
from FPrinter_Driver.FP_Datex_v167 import DATEX_Comm as Dt_v167
from FPrinter_Driver.FP_Tremol_ZFPLAB import FP_Tremol as Fpd
from FPrinter_Driver.FP_Datex import FP_Datex as DtHttp
from FP_Shtih_Driver.utils import FpUtil as Shtrih
from datetime import *
from UNA_Support.Utility import *
from UNA_Support.config_util import *


def print_check(p_object):
    global g_res
    v_object = p_object[0][5] if v_is_pos else p_object[0][2]
    # logg_main.info(f'Type read MSG UNA {v_object}')
    tt = f'Type read MSG UNA {v_object}'
    logg_main.info(tt)
    data1 = str(v_object)
    logg_main.info(f'DATA: {data1}')
    data = data1.replace('\\n', '\n')

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
    l_msg_1 = '{1} Date now: ' + dt_string
    logg_main.info(l_msg_1)
    msg_client = '{2} Mesaj client: ' + str(data)
    logg_main.info(msg_client)

    start_code = msg_client.find('/c')
    # baud_rate, err_extract = extract_str(msg_client, '/br')
    baud_rate = config.conf.get('Connection', 'boudrate')
    # comm_port, err_extract = extract_str(msg_client, '/port')
    comm_port = config.conf.get('Connection', 'port')
    fp_type, err_extract = extract_str(msg_client, '/t')
    send_code = msg_client[start_code + 2:]

    try:
        if fp_type == 'TREMOL' or fp_type == 'TREMOL_TCP':
            tremol = Fpd()

            tremol_tcp = True if fp_type == 'TREMOL_TCP' else False
            if tremol_tcp:
                tremol.TCP_IP = config.conf.get('Connection', 'ip')
                tremol.TCP_PORT = config.conf.get('Connection', 'port')
                tremol.TCP_PASS = config.conf.get('Connection', 'pass')

                l_msg_3 = '{3} Fiscal Printer: ' + str(fp_type) + ' ' + str(tremol.TCP_IP)
                logg_main.info(l_msg_3)
            else:
                l_msg_3 = '{3} Fiscal Printer: ' + str(fp_type) + ' ' + str(comm_port) + ' ' + str(baud_rate)
                logg_main.info(l_msg_3)
                tremol.baud = int(baud_rate)
                tremol.comm_port = 'COM' + str(comm_port)

            tremol.isForm = False
            result_conn = tremol.OpenPort(tremol_tcp)
            if result_conn == 0:
                res = tremol.fiscal_receipt(send_code, 'server')
            else:
                res = result_conn
            logg_main.info(tremol.response_text)
        elif fp_type == 'DATECS':
            datecs = Dt_v167()
            try:
                l_msg_3 = ' {3} Fiscal Printer: ' + str(fp_type) + ' ' + comm_port + ' ' + baud_rate
                logg_main.info(l_msg_3)
                err_datecs = datecs.open_port(int(comm_port), int(baud_rate))
                logg_main.info(datecs.msg_res)
                datecs.msg_res = ''
                if err_datecs == 0:
                    res = datecs.fiscal_receipt(send_code, 'server')
                    if res == 0 or res == -1:
                        clos_r = datecs.close_port()
                        clos_r = 'Close connection Printer '.format(clos_r)
                        logg_main.info(clos_r)
                    send_msg = datecs.msg_res
                    res = send_msg
                else:
                    res = str(err_datecs) + ': Eroare conexiune FP'
            except KeyboardInterrupt as e_datecs:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                lmsg_e_datecs = '{exc_type}, {f_name}, {exc_tb} \n{e}' \
                    .format(exc_type=exc_type, f_name=f_name, exc_tb=exc_tb.tb_lineno, e=e_datecs)
                logg_main.error(lmsg_e_datecs)
                res = lmsg_e_datecs
            finally:
                clos_r = datecs.close_port()
                clos_r = 'finally Close connection Printer '.format(clos_r)
                logg_main.info(clos_r)
                pass
        elif fp_type == 'HTTP':
            datecs_http = DtHttp()
            fp_state = datecs_http.fiscal_receipt('71', 'server')
            if fp_state == 'OK':
                logg_main.info('Fiscal Printer: ' + str(fp_type) + ' ' + comm_port + ' ' + baud_rate)
                res = datecs_http.fiscal_receipt(send_code, 'server')
            else:
                error_msg = datecs_http.GETStateFPText(fp_state)
                res = error_msg
        elif fp_type == 'SHTRIH':
            comm_port = f'COM{comm_port}'
            shtrih = Shtrih(comm_port, baud_rate)
            shtrih.pay_type_list = {'N': 1, 'P': 0, 'E': 2, 'U': 3}
            v_fp_state = shtrih.connect()
            if v_fp_state == 0:
                try:
                    res = shtrih.fiscal_receipt(send_code)
                except Exception as err_fp:
                    res = f'Eroare necunoscuta {err_fp}'
            else:
                res = f'Error connect comm port {comm_port}, {baud_rate}'
            shtrih.disconnect()
        elif fp_type == 'VIRTUAL':
            res = 'OK'
        else:
            res = "Nu este setat FP de acest model " + str(fp_type)

        # Transmiterea raspunsului ====================
        send_msg = res
        g_res = res
        logg_main.info(f'Raspuns trimis la client: {send_msg}')
        DB_CONNECTOR.update_fp_res(v_id, send_msg, v_is_pos)
        # self.request.sendall(send_msg)
        # =============================================
    except KeyboardInterrupt as ex_gen:
        logg_main.error(f'other error: {ex_gen}')
        g_res = ''
        pass


if __name__ == '__main__':
    g_res = ''
    # ========================================================
    current_path = os.path.dirname(os.path.abspath(__file__))
    date_now = datetime.now().strftime("%Y%m%d")
    app_exit = False

    # setarea afisarii logurilor 'logging'
    try:
        os.makedirs(LOG_CONST.LOGSavePath)
    except Exception as ex:
        print('No found directori')

    logging_level = 'DEBUG'

    logFormatter = logging.Formatter("%(asctime)s [%(name)-27.27s] [%(levelname)-8.8s] "
                                     "F:[%(lineno)d: %(funcName)-20.20s] %(message)s",
                                     '%m-%d-%y %H:%M:%S')
    rootLogger = logging.getLogger()

    fileHandler = logging.FileHandler(LOG_CONST.LOGSavePath + date_now + LOG_CONST.name_log)
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

    logg_main.info(LOG_CONST.START_APP)
    logg_main.info(version_app)
    logg_main.info(sys.version)

    # ================ Creare fisier configurari ============
    config = CFG('Service_FP_UNA.ini')
    config.conf.add_section('Connection')
    config.conf.set('Connection', 'port', '7')
    config.conf.set('Connection', 'boudrate', '9600')

    config.create_cfg_file()
    # =======================================================

    try:
        NAME_HOST = sys.argv[1]
        SERVER = sys.argv[2]
        ORACLE_DIR_ = sys.argv[3]
        ID = sys.argv[4]
        # NAME_HOST = 'mmici'
        # SERVER = 'MILESHTI_NEW'
        # ID = '239P'

        ORACLE_DIR = r'C:\oracle\instantclient_12_2'

        v_db_name = NAME_HOST
        v_db_pass = NAME_HOST
        v_db_server = SERVER
        v_oracle_dir = ORACLE_DIR

        logg_main.info(f'ID: {ID}')

        v_id = ID.replace('P', '')
        v_id = v_id.replace('R', '')
        v_id = int(v_id)
        v_is_pos = False if ID.find('P') == -1 else True
        v_is_repeat_print = False if ID.find('R') == -1 else True

        logg_main.info(f'{v_db_name} {v_db_server} {v_oracle_dir} {v_id}')

        DB_CONNECTOR = DB_Method(v_db_name, v_db_pass, v_db_server, v_oracle_dir)
    except Exception as err:
        logg_main.error(err)
    else:
        logg_main.info('Connect db successful')

        v_list_sc_check = DB_CONNECTOR.get_check_una(v_id)

        if v_is_pos and v_list_sc_check[0][7] in (48, '48'):
            # Printarea chec fiscal dupa achitarea din POS
            v_is_pos = False
            print_check(v_list_sc_check)

            if g_res[:3] == 'ERR':
                v_list_sc_check = [(None,
                                    'Anulare Bon',
                                    '/br115200/port7/tDATECS/c60',
                                    None,
                                    None,
                                    None,
                                    None
                                    )]

                print_check(v_list_sc_check)
            else:
                # printare don de serviciu (bon primit de la POS terminal)
                # noinspection PyRedeclaration
                v_is_pos = True
                print_check(v_list_sc_check)
        if v_is_repeat_print:
            v_is_pos = True
            print_check(v_list_sc_check)
        else:
            print_check(v_list_sc_check)
