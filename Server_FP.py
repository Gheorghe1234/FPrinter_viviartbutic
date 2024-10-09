import socketserver
import json

import time as time_
import getpass
import configparser

from FPrinter_Driver.FP_Tremol_ZFPLAB import FP_Tremol as Fpd
from FPrinter_Driver.FP_Datex import DATEX_Comm as Dt
from FPrinter_Driver.FP_Datex_v167 import DATEX_Comm as Dt_v167
from FPrinter_Driver.FP_Datex import FP_Datex as DtHttp
from FPrinter_Driver.FP_RTI import Rti1000
from datetime import *
from UNA_Support.Utility import *
from FP_Shtih_Driver.utils import FpUtil as Shtrih
from IQOS.IQOS import *
from CONFIG_from_FP import *
from FPrinter_Driver.FP_Virtual import *


def get_conf_env(p_env, p_env_default):
    try:
        v_result = config.conf.get(p_env[0], p_env[1])
    except Exception:
        logg_main.info(f'Set Default ENV {p_env}')
        v_result = p_env_default

    return v_result


def verifica_actualizeaza_fisier_ini(p_def_value, p_file_path):
    file_path = p_file_path
    section_name = 'TinaFpDatecs'
    param_name = 'comtcpipaddr'

    config_local = configparser.ConfigParser()
    config_local.read(file_path)

    # print(p_def_value[0][1])
    print(config_local[section_name])
    try:
        v_comtcpipaddr = config_local[section_name][param_name]
    except KeyError:
        v_comtcpipaddr = '0.0.0.0'

    if v_comtcpipaddr == p_def_value[0][1]:
        logger.info(f"Parametrul '{param_name}' din fisierul '{file_path}' corespunde valorii din 'v_def_value'.")
        return

    config_local[section_name] = {}
    for param, value in p_def_value:
        config_local[section_name][param] = value

    with open(file_path, 'w') as config_file:
        config_local.write(config_file)

    logger.info(f"Fisierul '{file_path}' a fost actualizat cu valorile din 'v_def_value'.")


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        """
        /br115200
        /port - comm port
        /t - type Fiscal Printer "DATECS, DATECSHTTP, TREMOL"
        /c - code sent to FP

        ex: /br115200/port7/tTREMOL/c38
42, 8888888888888888888888888888888888888888
42, 1234567890123456789012345678901234567890
42, 8888888888888888888888888888888888888888
42, 1234567890123456789012345678901234567890
39
cIQOS
        """
        v_type_read_msg = int(config.conf.get('OTHER', 'type_read_message'))
        if v_type_read_msg == 2:
            logg_main.info(f'Type read MSG UAMenu {v_type_read_msg}')
            data1 = self.request.recv(50960).strip()
            logg_main.info(f'DATA1: {data1}')
            data2 = self.request.recv(50960).strip()
            logg_main.info(f'DATA2: {data2}')
            data = f"{data1.decode('utf-8', 'ignore')}{data2.decode('utf-8', 'ignore')}"
            # data = data2.decode('utf-8', 'ignore')
        else:
            logg_main.info(f'Type read MSG UAMenu {v_type_read_msg}')
            data1 = self.request.recv(50960).strip()
            logg_main.info(f'DATA: {data1}')
            data = data1.decode('utf-8', 'ignore')

        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        l_msg_1 = '{1} Date now: ' + dt_string
        print('\n' + l_msg_1)
        logg_main.info(l_msg_1)
        msg_client = '{2} Mesaj client: ' + str(data)
        logg_main.info(msg_client)

        start_code = msg_client.find('/c')
        baud_rate, err_extract = extract_str(msg_client, '/br')
        comm_port, err_extract = extract_str(msg_client, '/port')
        fp_type, err_extract = extract_str(msg_client, '/t')
        send_code = msg_client[start_code + 2:]

        iqos_url = config.conf.get('OTHER', 'iqos_url')

        if send_code.find('cIQOS') > -1:
            iqos = Iqos(iqos_url)
            v_bon = iqos.get_check()
            send_code = send_code.replace('cIQOS', v_bon)

        try:
            if fp_type == 'TREMOL' or fp_type == 'TREMOL_TCP':

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

                # send_msg = str(len(res)) + '\n' + res
                # send_msg = send_msg.encode('cp1251')
                # self.request.sendall(send_msg)
                # print(tremol.response_text)
                # log.info(tremol.response_text)
                logg_main.info(tremol.response_text)
            elif fp_type == 'DATECS':
                try:
                    l_msg_3 = ' {3} Fiscal Printer: ' + str(fp_type) + ' ' + comm_port + ' ' + baud_rate
                    logg_main.info(l_msg_3)
                    err = datecs.open_port(int(comm_port), int(baud_rate))
                    logg_main.info(datecs.msg_res)
                    datecs.len_printing_text = int(get_conf_env(['OTHER', 'len_printing_text'], 42))
                    logg_main.info(f'len_printing_text: {datecs.len_printing_text}')
                    datecs.msg_res = ''

                    if err == 0:
                        res = datecs.fiscal_receipt(send_code, 'server')
                        if res == 0 or res == -1:
                            clos_r = datecs.close_port()
                            clos_r = 'Close connection Printer '.format(clos_r)
                            logg_main.info(clos_r)
                        send_msg = datecs.msg_res
                        res = send_msg
                    else:
                        res = str(err) + ': Eroare conexiune FP'
                # except Exception as e_datecs:
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

                # send_msg = str(len(res)) + '\n' + res
                # self.request.sendall(send_msg)
            elif fp_type == 'HTTP':
                fp_state = datecs_http.fiscal_receipt('71', 'server')
                # fp_state = 'OK'
                if fp_state == 'OK':
                    logg_main.info('Fiscal Printer: ' + str(fp_type) + ' ' + comm_port + ' ' + baud_rate)
                    res = datecs_http.fiscal_receipt(send_code, 'server')
                    # send_msg = str(len(res)) + '\n' + res
                    # send_msg = res
                else:
                    error_msg = datecs_http.GETStateFPText(fp_state)
                    # send_msg = str(len(error_msg)) + '\n' + error_msg
                    res = error_msg
                # self.request.sendall(send_msg)
                # log.info('send_msg: ' + send_msg)
            elif fp_type == 'SHTRIH':
                comm_port = f'COM{comm_port}'
                shtrih = Shtrih(comm_port, baud_rate)
                shtrih.pay_type_list = v_pay_type_list
                v_fp_state = shtrih.connect()
                if v_fp_state == 0:
                    try:
                        res = shtrih.fiscal_receipt(send_code)
                    except Exception as err:
                        res = f'Eroare necunoscuta {err}'
                else:
                    res = f'Error connect comm port {comm_port}, {baud_rate}'
                shtrih.disconnect()
            elif fp_type == 'RTI':
                comm_port = comm_port
                v_rti = Rti1000(current_path)
                v_fp_state = v_rti.open_port(comm_port, baud_rate)
                if v_fp_state == 0:
                    try:
                        res = v_rti.fiscal_receipt(send_code)
                    except KeyboardInterrupt as err:
                    # except Exception as err:
                        res = f'Eroare necunoscuta {err}'
                else:
                    res = f'Error connect comm port {comm_port}, {baud_rate}'
            elif fp_type == 'VIRTUAL':
                try:
                    l_msg_3 = ' Virtual FP: ' + str(fp_type) + ' ' + comm_port + ' ' + baud_rate
                    logg_main.info(l_msg_3)
                    err = virtual_fp.open_port(int(comm_port), int(baud_rate))
                    logg_main.info(virtual_fp.msg_res)
                    virtual_fp.len_printing_text = int(get_conf_env(['OTHER', 'len_printing_text'], 42))
                    logg_main.info(f'len_printing_text: {virtual_fp.len_printing_text}')
                    virtual_fp.msg_res = ''

                    if err == 0:
                        res = virtual_fp.fiscal_receipt(send_code, 'server')
                        if res == 0 or res == -1:
                            clos_r = virtual_fp.close_port()
                            clos_r = 'Close connection Printer '.format(clos_r)
                            logg_main.info(clos_r)
                        send_msg = virtual_fp.msg_res
                        res = send_msg
                    else:
                        res = str(err) + ': Eroare conexiune FP'
                # except Exception as e_virtual_fp:
                except KeyboardInterrupt as e_virtual_fp:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    lmsg_e_virtual_fp = '{exc_type}, {f_name}, {exc_tb} \n{e}' \
                        .format(exc_type=exc_type, f_name=f_name, exc_tb=exc_tb.tb_lineno, e=e_virtual_fp)
                    logg_main.error(lmsg_e_virtual_fp)
                    res = lmsg_e_virtual_fp
                finally:
                    clos_r = virtual_fp.close_port()
                    clos_r = 'finally Close connection Printer '.format(clos_r)
                    logg_main.info(clos_r)
                    pass

                # send_msg = str(len(res)) + '\n' + res
                # self.request.sendall(send_msg)
            else:
                res = "Nu este setat FP de acest model " + str(fp_type)

            # Transmiterea raspunsului ====================
            send_msg = (str(len(res)) + '\n' + res).encode()
            logg_main.info(f'Raspuns trimis la client: {send_msg.decode("utf-8", errors="ignore")}')
            self.request.sendall(send_msg)
            # =============================================
        except KeyboardInterrupt as ex_gen:
            logg_main.error(f'other error: {ex_gen}')
            pass


# ========================================================
current_path = os.path.dirname(os.path.abspath(sys.argv[0]))
date_now = datetime.now().strftime("%Y%m%d")
app_exit = False

# setarea afisarii logurilor 'logging'
try:
    os.makedirs(LOG_CONST.LOGSavePath)
except Exception as ex:
    pass

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

if __name__ == '__main__':
    logg_main.info(LOG_CONST.START_APP)
    logg_main.info(version_app)
    logg_main.info(sys.version)
    logg_main.info(f'current_path: {current_path}')

    try:
        try:
            tremol = Fpd()
        except Exception as ex:
            logg_main.info(ex)
            MSG = 'Eroare Initializare ZFPLabService'
            logg_main.info(MSG)

        try:
            v_datecs_protocol = int(get_conf_env(['OTHER', 'datecs_protocol'], 1))

            v_datecs_protocol_txt = {
                2: 'Wtdedit 1.6.6.1',
                1: 'Wtdedit 1.6.7.0',
                3: 'Wtdedit 1.6.7.0_old'
            }
            logg_main.info(f'Datecs protocol version: {v_datecs_protocol_txt[v_datecs_protocol]}')

            v_datecs_type_Protocol_Model = int(get_conf_env(['OTHER', 'datecs_type_Protocol_Model'], 0))

            logg_main.info(f'datecs_type_Protocol_Model: {v_datecs_type_Protocol_Model}')

            if v_datecs_protocol == 1 or v_datecs_protocol == 3:
                datecs = Dt_v167()
                datecs.datecs_type_Protocol_Model = v_datecs_type_Protocol_Model
                datecs.datecs_protocol = v_datecs_protocol
            else:
                datecs = Dt()

            v_is_tinafpdatecs = int(get_conf_env(['OTHER', 'is_tinafpdatecs'], 0))

            if v_is_tinafpdatecs == 1:
                try:
                    v_setup_tina_fp_datecs = config.conf.items('TinaFpDatecs')
                except configparser.NoSectionError:
                    logg_main.info(f'In fisierul setup.ini nu este sectia "TinaFpDatecs"')
                else:
                    v_username_account = getpass.getuser()
                    v_default_tina_fp_setup = f'c:\\Users\\{v_username_account}\\TinaFpDatecs'

                    if not os.path.exists(v_default_tina_fp_setup):
                        os.makedirs(v_default_tina_fp_setup)
                        logger.info(f'Creare folder {v_default_tina_fp_setup}')

                    v_file_name = 'TinaFpDatecs.ini'
                    v_file_path = os.path.join(v_default_tina_fp_setup, v_file_name)

                    if os.path.isfile(v_file_path):
                        verifica_actualizeaza_fisier_ini(v_setup_tina_fp_datecs, v_file_path)
                    else:
                        open(v_file_path, 'w').close()
                        logg_main.info(f'Creare fisier {v_file_name}')
                        verifica_actualizeaza_fisier_ini(v_setup_tina_fp_datecs, v_file_path)

        except Exception as ex:
            logg_main.info(ex)
            MSG = 'Lipseste driver-ul pentru Printerul Datecs'
            logg_main.info(MSG)

        datecs_http = DtHttp()
        virtual_fp = VIRTUAL_Comm(current_path)

    except Exception as ex:
        logg_main.error(f'{LOG_CONST.ERRORUnknown} {ex}')
        time_.sleep(SYSVal.SLEEP_CMD)
    else:
        v_pay_type_list = get_conf_env(['FP_TYPE_PAY', 'type_pay'], '{"N":0, "P":1, "E":2, "U":3}')
        v_pay_type_list = json.loads(v_pay_type_list)
        logg_main.info(f'Pay type list: {v_pay_type_list}')

        try:
            logg_main.info('Server Start -  127.0.0.1:8880')
            server = socketserver.TCPServer(('', 8880), EchoTCPHandler)
            server.serve_forever()
        except KeyboardInterrupt:
            logg_main.info(LOG_CONST.CLOSE_APP)
