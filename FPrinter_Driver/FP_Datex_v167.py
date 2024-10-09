# coding=utf-8
import logging
from datetime import datetime, timedelta
import time as time_
import pytz

from win32com import client
from CONSTANT import *
from FPrinter_Driver.emulator_method_FP import send_fp

logger = logging.getLogger(__name__)


def get_key_array(p_array, p_key, p_default):
    try:
        v_res = p_array[p_key]
    except KeyError:
        v_res = p_default
    except Exception as err:
        logger.error(f'{err}')
        v_res = p_default

    return v_res


def explode_text(p_text, p_len):
    v_result = []
    if len(p_text) <= p_len:
        v_result.append(p_text)  # Textul este mai mic sau egal cu lungimea specificată, deci îl adăugăm în listă
    else:
        for i in range(0, len(p_text), p_len):
            bucata = p_text[i:i + p_len]
            v_result.append(bucata)  # Adăugăm bucata în listă

    return v_result


def check_dst(p_date):
    timezone = pytz.timezone('Europe/Chisinau')
    v_date = timezone.localize(datetime.strptime(p_date, "%d-%m-%y %H:%M:%S"))
    return v_date.dst() != timedelta(0)


# noinspection DuplicatedCode
class DATEX_Comm:
    def __init__(self):
        self.msg_res_err = ''
        self.datecs_type_Protocol_Model = 0
        self.datecs_protocol = 1
        logger.info(f'Init DATEX_Comm module')
        # self.device = client.Dispatch("Wtdedit.FpAtl.1")
        self.device = client.Dispatch("Wtdedit.FpAtl")
        self.msg_res = ''
        self.EJ_OPERATIONS = ''
        # self.log = Log(LOG_CONST.FP_Log, LOG_CONST.LOGSavePath)
        self.pay_type_list = {
            'N': 0,  # NUMERAR (CASH)
            'P': 1,  # CARD
            'C': 2,  # CREDIT
            'A': 3,  # TICHETE MASA (MEAL VOUCHERS)
            'B': 4,  # TICHETE VALORICE (VALUE TICKETS)
            'D': 5,  # VOUCHER
            'E': 6,  # PLATA MODERNA (MODERN PAYMENT)
            'F': 7,  # CARD + AVANS IN NUMERAR (CASH IN ADVANCE)
            'H': 8,  # ALTE METODE (OTHER METHODS)
            'I': 9,  # Foreign currency
        }
        self.total_amount_check = 0
        self.total_amount_pay_type = 0
        self.is_open_fiscal_recipient = False

        self.len_printing_text = 42

        self.DST = ' DST'
        self.DST_flag = True
        self.set_dst()
        # if check_dst(datetime.now().strftime("%d-%m-%y %H:%M:%S")):
        #     self.DST = ' DST'
        #     self.DST_flag = True
        #     logger.info('set time format: DST')
        # else:
        #     self.DST = ''
        #     self.DST_flag = False
        #     logger.info('NOT set time format: DST')

    def set_dst(self, p_date=datetime.now()):
        v_date = p_date.strftime("%d-%m-%y %H:%M:%S")
        logger.info(f'set_dst, param: [{v_date}]')
        if check_dst(v_date):
            self.DST = ' DST'
            self.DST_flag = True
            logger.info('set time format: DST')
        else:
            self.DST = ''
            self.DST_flag = False
            logger.info('NOT set time format: DST')

    def get_open_port(self, p_com, p_baudrate=9600):
        logger.info(f'Func. get_open_port run, param: [com {p_com}], [baudrate {p_baudrate}]')

        # Activarea TypeProtocol/TypeModel pentru anumite tipuri de FP
        if self.datecs_type_Protocol_Model == 1:
            logger.info(f'Activam TypeProtocol/TypeModel')
            # self.device.TypeProtocol = self.device.FpTypeProtocol.FpTypeProtocol_NEW
            # self.device.TypeModel = self.device.FpTypeModel.FpTypeModel_DP25
            self.device.TypeProtocol = 1
            self.device.TypeModel = 3

        v_res1 = self.device.OpenPortL(911304495, p_com, p_baudrate)
        time_.sleep(1)
        v_res2 = self.device.Send(488839203, 74, '', '')
        v_res2_err = str(v_res2[1])
        v_res2_err_code = v_res2_err[:v_res2_err.find('\t')]

        if v_res1 is True and (v_res2_err_code == '0' or v_res2_err_code == ''):
            v_res = 0
        else:
            v_res = 1

        logger.info(f'return: {v_res}, {v_res1}, {v_res2}')
        return v_res, v_res1, v_res2

    def open_port(self, com, baudrate=9600):
        logger.info(f'Run, param: {com}, {baudrate}')
        v_res = 1
        v_repeat = 1
        v_res1, v_res2 = '', ''

        # TODO
        # return 0

        for i in range(1, 3):
            v_res, v_res1, v_res2 = self.get_open_port(com, baudrate)
            v_repeat = i
            if v_res == 0:
                break

        self.msg_res = '[{repet}] OpenPortL: {res1}, Command 74: {res2}'.format(res1=v_res1, res2=v_res2,
                                                                                repet=v_repeat)

        logger.info(f'Return: {v_res}, self.msg_res-{self.msg_res}')
        return v_res

    def param_convert_new_protocol(self, p_cmd, p_param):
        logger.info('=' * 60)
        logger.info(f'Convert func. param: [{p_cmd}], [{p_param}]')
        p_cmd = int(p_cmd)
        v_list_cote_tva = {
            'A': 1,  # vat group A;
            'B': 2,  # vat group B;
            'C': 3,  # vat group C;
            'D': 4,  # vat group D;
            'E': 5,  # vat group E;
            'O': 6,  # alte taxe;
            'N': 7   # exempt;
        }

        try:
            v_cmd = p_cmd
            if p_cmd == 33:
                v_result = p_param
            elif p_cmd == 35:
                v_result = f'{p_param}\\t'
            elif p_cmd == 38:
                v_result = f'{p_param}'
            elif p_cmd == 39:
                v_result = f'{p_param}\\t'
            elif p_cmd == 42:
                v_result = f'{p_param}\\t'
                # v_result = f'{p_param}'
                v_cmd = 54 if self.is_open_fiscal_recipient else v_cmd
            elif p_cmd == 44:
                if len(str(p_param)) == 0:
                    p_param = 1
                v_result = f'{p_param}\\t'
            elif p_cmd == 45:
                v_cmd = 46
                v_result = p_param
            elif p_cmd == 46:
                v_result = p_param
            elif p_cmd == 47:
                v_result = f'{p_param}\\t'
            elif p_cmd == 48:
                v_step1 = p_param.find(',')
                v_step2 = p_param.find(',', v_step1 + 1)
                v_op_code = p_param[:v_step1]
                # v_op_pwd = p_param[v_step1 + 1:v_step2]
                v_op_pwd = '1'
                v_till_nmb = p_param[v_step2 + 1:]

                v_result = f'{v_op_code}\\t{v_op_pwd}\\t{v_till_nmb}\\t'
                self.is_open_fiscal_recipient = True
            elif p_cmd == 49:
                logger.info(f'p_param: {p_param}')

                # noinspection DuplicatedCode
                v_param_arr = str(p_param).split('\\t')
                logger.info(f'v_param_arr: {v_param_arr}')
                v_produs_name = v_param_arr[0]
                v_product_detail = v_param_arr[1]
                v_cota_tva = v_product_detail[0:1]
                v_price = v_product_detail[1:v_product_detail.find('*')]
                v_qnt = v_product_detail[v_product_detail.find('*') + 1:]

                try:
                    v_departament = v_param_arr[2]
                except IndexError:
                    v_departament = '0'

                try:
                    v_discount_type = v_param_arr[3]
                except IndexError:
                    v_discount_type = '0'

                try:
                    v_discount_value = v_param_arr[4]
                except IndexError:
                    v_discount_value = '0'

                try:
                    v_um = v_param_arr[5]
                except IndexError:
                    v_um = 'unit.'

                # if v_departament.isalpha():
                #     v_um = v_departament
                #     v_departament = '0'

                self.total_amount_check = self.total_amount_check + (float(v_price) * float(v_qnt))
                self.total_amount_check = round(self.total_amount_check, 2)

                v_cota_tva = v_list_cote_tva[v_cota_tva]

                v_result = f'{v_produs_name}\t{v_cota_tva}\t{v_price}\t{v_qnt}\t{v_discount_type}\t' \
                           f'{v_discount_value}\t{v_departament}\t{v_um}\t'
                logger.info(f'total_amount_check: {self.total_amount_check}')
            elif p_cmd == 53:
                v_step1 = p_param.find('\\t')

                v_pay_type = p_param[v_step1 + 2:v_step1 + 3]
                v_pay_type = self.pay_type_list[v_pay_type]
                v_suma = p_param[v_step1 + 3:]

                if v_suma == '0' or v_suma == '':
                    v_suma = self.total_amount_check - self.total_amount_pay_type
                else:
                    self.total_amount_pay_type = self.total_amount_pay_type + float(v_suma)

                v_result = f'{v_pay_type}\t{v_suma}\t'
            elif p_cmd == 54:
                v_result = f'{p_param}\\t'
            elif p_cmd == 56:
                v_result = p_param
                self.is_open_fiscal_recipient = False
                self.total_amount_pay_type = 0
                self.total_amount_check = 0
            elif p_cmd == 60:
                v_result = p_param
            elif p_cmd == 61:
                # v_result = f'{p_param}:00 DST\\t'
                v_result = f'{p_param}:00{self.DST}\\t'
            elif p_cmd == 62:
                v_cmd = 62
                v_result = p_param
            elif p_cmd == 65:
                v_result = f'0\t'
            elif p_cmd == 69:
                if p_param == '2':
                    v_type_rep = 'X'
                elif p_param == '0':
                    v_type_rep = 'Z'
                elif p_param == '3':
                    v_type_rep = 'D'
                else:
                    v_type_rep = 'Z'

                v_result = f'{v_type_rep}\\t'
                logger.info(f'TEST {v_result}')
            elif p_cmd == 70:
                v_amount = float(p_param)
                if v_amount >= 0:
                    v_type_op = 0
                else:
                    v_type_op = 1
                    v_amount = v_amount * -1

                v_result = f'{v_type_op}\t{v_amount}\t'
            elif p_cmd == 84:
                v_step1 = p_param.find(',')

                v_barcode_data = p_param[:v_step1]
                v_barcode_type = p_param[v_step1 + 1:]

                if v_barcode_type not in ['1', '2', '3', '4', '5']:
                    logger.info(f'protocolul nou datecs Wtdedit 1.6.7.0 nu permite tipul de barcode {v_barcode_type}')
                    v_barcode_type = '1'

                v_result = f'{v_barcode_type}\t{v_barcode_data}\t5\t'
            elif p_cmd == 100:
                v_result = f'{p_param}\t'
            elif p_cmd == 106:
                v_result = f'1\t'
            elif p_cmd == 117:
                # report of Departament
                v_result = f'D\t'
            elif p_cmd == 119:
                v_param = p_param.split(',')

                v_option = get_key_array(v_param, 0, 'R')

                v_datastart = datetime.strptime(get_key_array(v_param, 2, '220699110041'), "%d%m%y%H%M%S")
                self.set_dst(v_datastart)
                if self.DST_flag:
                    v_datastart = v_datastart.strftime("%d-%m-%y %H:%M:%S DST")
                else:
                    v_datastart = v_datastart.strftime("%d-%m-%y %H:%M:%S")

                v_dataend = datetime.strptime(get_key_array(v_param, 3, '220699230041'), "%d%m%y%H%M%S")
                self.set_dst(v_dataend)
                if self.DST_flag:
                    v_dataend = v_dataend.strftime("%d-%m-%y %H:%M:%S DST")
                else:
                    v_dataend = v_dataend.strftime("%d-%m-%y %H:%M:%S")

                v_param_ = f'{v_datastart}\t{v_dataend}\t0\t'

                # TODO Testare
                v_rsp_124 = self.device.SendEx(488839203, 124, v_param_, '')
                # v_rsp_124 = send_fp(488839203, 124, v_param_, '')

                logger.info(f'v_rsp_124: {v_rsp_124}')
                v_rsp_124_res = v_rsp_124[1].split('\t')
                self.EJ_OPERATIONS = ''
                if v_rsp_124[0] and v_rsp_124_res[0] == '0':
                    v_min_nr_check = int(get_key_array(v_rsp_124_res, 4, 0))
                    v_max_nr_check = int(get_key_array(v_rsp_124_res, 6, 0))

                    if v_option == 'R':
                        v_result_ = self.read_ej(v_min_nr_check, v_max_nr_check)
                    elif v_option == 'P':
                        v_result_ = self.print_ej(v_min_nr_check, v_max_nr_check)
                    else:
                        v_result_ = (False, '-200001\t')

                else:
                    logger.error(f'v_rsp_124, Comanda: {v_param_.encode()}, ERR {LIST_ERR[v_rsp_124_res[0]]}')
                    v_result_ = v_rsp_124

                v_result = v_result_
            elif p_cmd == 124:
                v_step1 = p_param.find(',')
                v_step2 = p_param.find(',', v_step1 + 1)
                v_step3 = p_param.find(',', v_step2 + 1)
                v_step3 = len(p_param) if v_step3 == -1 else v_step3

                v_start_date = p_param[:v_step1]
                v_end_date = p_param[v_step1 + 1:v_step2]
                v_doc_type = p_param[v_step2 + 1:v_step3]

                v_result = f'{v_start_date}\\t{v_end_date}\\t{v_doc_type}\\t'
            elif p_cmd == 125:
                v_param = p_param.split(',')
                v_option = get_key_array(v_param, 0, None)
                v_doc_number = get_key_array(v_param, 1, None)
                v_doc_type = get_key_array(v_param, 2, None)

                if v_doc_number is None:
                    v_doc_number = ''
                else:
                    v_doc_number = f'{v_doc_number}\\t'

                if v_doc_type is None:
                    v_doc_type = ''
                else:
                    v_doc_type = f'{v_doc_type}\\t'

                v_result = f'{v_option}\\t{v_doc_number}{v_doc_type}'
            else:
                v_cmd = -1
                v_result = f'-1\tNu este este setata comanda trimisa: {p_cmd}'
        except Exception as ex:
            v_cmd = -2
            v_result = f'-2\tEroare in sintaxa comanda: {p_cmd}'
            logger.error(f'{v_result}')
            logger.error(f'{ex}')

        logger.info(f'Return convert func.: [{v_cmd}], [{v_result}]')
        return v_cmd, v_result

    def param_convert_new_protocol_old(self, p_cmd, p_param):
        logger.info('=' * 60)
        logger.info(f'Convert func. param: [{p_cmd}], [{p_param}]')
        p_cmd = int(p_cmd)
        v_list_cote_tva = {
            'A': 1,  # vat group A;
            'B': 2,  # vat group B;
            'C': 3,  # vat group C;
            'D': 4,  # vat group D;
            'E': 5,  # vat group E;
            'O': 6,  # alte taxe;
            'N': 7   # exempt;
        }

        try:
            v_cmd = p_cmd
            if p_cmd == 33:
                v_result = p_param
            elif p_cmd == 35:
                v_result = f'{p_param}\\t'
            elif p_cmd == 38:
                self.is_open_fiscal_recipient = False
                v_result = f'{p_param}'
            elif p_cmd == 39:
                v_result = f'{p_param}'
            elif p_cmd == 42:
                v_result = f'{p_param}\\t'
                # v_result = f'{p_param}'
                v_cmd = 54 if self.is_open_fiscal_recipient else v_cmd
            elif p_cmd == 44:
                if len(str(p_param)) == 0:
                    p_param = 1
                v_result = f'{p_param}\\t'
            elif p_cmd == 45:
                v_cmd = 46
                v_result = p_param
            elif p_cmd == 46:
                v_result = p_param
            elif p_cmd == 47:
                v_result = f'{p_param}\\t'
            elif p_cmd == 48:
                v_step1 = p_param.find(',')
                v_step2 = p_param.find(',', v_step1 + 1)
                v_op_code = p_param[:v_step1]
                # v_op_pwd = p_param[v_step1 + 1:v_step2]
                v_op_pwd = '1'
                v_till_nmb = p_param[v_step2 + 1:]

                v_result = f'{v_op_code}\\t{v_op_pwd}\\t{v_till_nmb}\\t\\t'
                self.is_open_fiscal_recipient = True
            elif p_cmd == 49:
                logger.info(f'p_param: {p_param}')

                # noinspection DuplicatedCode
                v_param_arr = str(p_param).split('\\t')
                logger.info(f'v_param_arr: {v_param_arr}')
                v_produs_name = v_param_arr[0]
                v_product_detail = v_param_arr[1]
                v_cota_tva = v_product_detail[0:1]
                v_price = v_product_detail[1:v_product_detail.find('*')]
                v_qnt = v_product_detail[v_product_detail.find('*') + 1:]

                try:
                    v_departament = v_param_arr[2]
                except IndexError:
                    v_departament = '0'

                try:
                    v_discount_type = v_param_arr[3]
                except IndexError:
                    v_discount_type = '0'

                try:
                    v_discount_value = v_param_arr[4]
                except IndexError:
                    v_discount_value = '0'

                try:
                    v_um = v_param_arr[5]
                except IndexError:
                    v_um = 'unit.'

                # if v_departament.isalpha():
                #     v_um = v_departament
                #     v_departament = '0'

                self.total_amount_check = self.total_amount_check + (float(v_price) * float(v_qnt))
                self.total_amount_check = round(self.total_amount_check, 2)

                v_cota_tva = v_list_cote_tva[v_cota_tva]

                v_result = f'{v_produs_name}\\t{v_cota_tva}\\t{float(v_price)}\\t{v_qnt}\\t{v_discount_type}\\t' \
                           f'{v_discount_value}\\t{v_departament}\\t'
                logger.info(f'total_amount_check: {self.total_amount_check}')
            elif p_cmd == 53:
                v_step1 = p_param.find('\\t')

                v_pay_type = p_param[v_step1 + 2:v_step1 + 3]
                v_pay_type = self.pay_type_list[v_pay_type]
                v_suma = p_param[v_step1 + 3:]

                if v_suma == '0' or v_suma == '':
                    v_suma = self.total_amount_check - self.total_amount_pay_type
                else:
                    self.total_amount_pay_type = self.total_amount_pay_type + float(v_suma)

                v_result = f'{v_pay_type}\t{v_suma}\t'
            elif p_cmd == 54:
                v_result = f'{p_param}\\t'
            elif p_cmd == 56:
                v_result = p_param
                self.is_open_fiscal_recipient = False
                self.total_amount_pay_type = 0
                self.total_amount_check = 0
            elif p_cmd == 60:
                v_result = p_param
            elif p_cmd == 61:
                # v_result = f'{p_param}:00 DST\\t'
                v_result = f'{p_param}:00{self.DST}\\t'
            elif p_cmd == 62:
                v_cmd = 62
                v_result = p_param
            elif p_cmd == 65:
                v_result = f'0\t'
            elif p_cmd == 69:
                if p_param == '2':
                    v_type_rep = 'X'
                elif p_param == '0':
                    v_type_rep = 'Z'
                elif p_param == '3':
                    v_type_rep = 'D'
                else:
                    v_type_rep = 'Z'

                v_result = f'{v_type_rep}\\t'
                logger.info(f'TEST {v_result}')
            elif p_cmd == 70:
                v_amount = float(p_param)
                if v_amount >= 0:
                    v_type_op = 0
                else:
                    v_type_op = 1
                    v_amount = v_amount * -1

                v_result = f'{v_type_op}\t{v_amount}\t'
            elif p_cmd == 84:
                v_step1 = p_param.find(',')

                v_barcode_data = p_param[:v_step1]
                v_barcode_type = p_param[v_step1 + 1:]

                if v_barcode_type not in ['1', '2', '3', '4', '5']:
                    logger.info(f'protocolul nou datecs Wtdedit 1.6.7.0 nu permite tipul de barcode {v_barcode_type}')
                    v_barcode_type = '1'

                v_result = f'{v_barcode_type}\t{v_barcode_data}\t5\t'
            elif p_cmd == 100:
                v_result = f'{p_param}\t'
            elif p_cmd == 106:
                v_result = f'1\t'
            elif p_cmd == 117:
                # report of Departament
                v_result = f'D\t'
            elif p_cmd == 119:
                v_param = p_param.split(',')

                v_option = get_key_array(v_param, 0, 'R')

                v_datastart = datetime.strptime(get_key_array(v_param, 2, '220699110041'), "%d%m%y%H%M%S")
                self.set_dst(v_datastart)
                if self.DST_flag:
                    v_datastart = v_datastart.strftime("%d-%m-%y %H:%M:%S DST")
                else:
                    v_datastart = v_datastart.strftime("%d-%m-%y %H:%M:%S")

                v_dataend = datetime.strptime(get_key_array(v_param, 3, '220699230041'), "%d%m%y%H%M%S")
                self.set_dst(v_dataend)
                if self.DST_flag:
                    v_dataend = v_dataend.strftime("%d-%m-%y %H:%M:%S DST")
                else:
                    v_dataend = v_dataend.strftime("%d-%m-%y %H:%M:%S")

                v_param_ = f'{v_datastart}\t{v_dataend}\t0\t'

                # TODO Testare
                v_rsp_124 = self.device.SendEx(488839203, 124, v_param_, '')
                # v_rsp_124 = send_fp(488839203, 124, v_param_, '')

                logger.info(f'v_rsp_124: {v_rsp_124}')
                v_rsp_124_res = v_rsp_124[1].split('\t')
                self.EJ_OPERATIONS = ''
                if v_rsp_124[0] and v_rsp_124_res[0] == '0':
                    v_min_nr_check = int(get_key_array(v_rsp_124_res, 4, 0))
                    v_max_nr_check = int(get_key_array(v_rsp_124_res, 6, 0))

                    if v_option == 'R':
                        v_result_ = self.read_ej(v_min_nr_check, v_max_nr_check)
                    elif v_option == 'P':
                        v_result_ = self.print_ej(v_min_nr_check, v_max_nr_check)
                    else:
                        v_result_ = (False, '-200001\t')

                else:
                    logger.error(f'v_rsp_124, Comanda: {v_param_.encode()}, ERR {LIST_ERR[v_rsp_124_res[0]]}')
                    v_result_ = v_rsp_124

                v_result = v_result_
            elif p_cmd == 124:
                v_step1 = p_param.find(',')
                v_step2 = p_param.find(',', v_step1 + 1)
                v_step3 = p_param.find(',', v_step2 + 1)
                v_step3 = len(p_param) if v_step3 == -1 else v_step3

                v_start_date = p_param[:v_step1]
                v_end_date = p_param[v_step1 + 1:v_step2]
                v_doc_type = p_param[v_step2 + 1:v_step3]

                v_result = f'{v_start_date}\\t{v_end_date}\\t{v_doc_type}\\t'
            elif p_cmd == 125:
                v_param = p_param.split(',')
                v_option = get_key_array(v_param, 0, None)
                v_doc_number = get_key_array(v_param, 1, None)
                v_doc_type = get_key_array(v_param, 2, None)

                if v_doc_number is None:
                    v_doc_number = ''
                else:
                    v_doc_number = f'{v_doc_number}\\t'

                if v_doc_type is None:
                    v_doc_type = ''
                else:
                    v_doc_type = f'{v_doc_type}\\t'

                v_result = f'{v_option}\\t{v_doc_number}{v_doc_type}'
            else:
                v_cmd = -1
                v_result = f'-1\tNu este este setata comanda trimisa: {p_cmd}'
        except Exception as ex:
            v_cmd = -2
            v_result = f'-2\tEroare in sintaxa comanda: {p_cmd}'
            logger.error(f'{v_result}')
            logger.error(f'{ex}')

        logger.info(f'Return convert func.: [{v_cmd}], [{v_result}]')
        return v_cmd, v_result

    def read_ej(self, p_min_nr_check, p_max_nr_check):
        for nr_check in range(p_min_nr_check, p_max_nr_check + 1):
            v_param_ = f'0\t{nr_check}\t0\t'

            # TODO Testare
            v_rsp_125_0 = self.device.SendEx(488839203, 125, v_param_, '')
            # v_rsp_125_0 = send_fp(488839203, 125, v_param_, '')

            logger.info(f'v_rsp_125_0: {v_rsp_125_0}')
            v_rsp_125_0_res = v_rsp_125_0[1].split('\t')
            if v_rsp_125_0[0] and v_rsp_125_0_res[0] == '0':
                v_contor = True

                while v_contor:
                    # TODO Testare
                    v_rsp_125_1 = self.device.SendEx(488839203, 125, '1\t', '')
                    # v_rsp_125_1 = send_fp(488839203, 125, '1\t', '')  # emulator raspuns  FP

                    logger.info(f'v_rsp_125_1 ({nr_check}): {v_rsp_125_1}')
                    v_rsp_125_1_res = v_rsp_125_1[1].split('\t')
                    if v_rsp_125_1[0] and v_rsp_125_1_res[0] == '0':
                        if str(v_rsp_125_1_res[1]).find('0H : ') == -1 and \
                           str(v_rsp_125_1_res[1]).find('Temperatura: ') == -1:
                            self.EJ_OPERATIONS = f'{self.EJ_OPERATIONS}\n{v_rsp_125_1_res[1].encode("utf-8").decode()}'
                    else:
                        logger.info(f'v_rsp_125_1 ({nr_check}), '
                                    f'ERR {v_rsp_125_1_res[0]} {LIST_ERR[v_rsp_125_1_res[0]]}')
                        break

                self.EJ_OPERATIONS = f'{self.EJ_OPERATIONS}\n============================'

            else:
                logger.error(f'v_rsp_125_0, Check: '
                             f'{v_param_.encode()}, ERR {v_rsp_125_0_res[0]} {LIST_ERR[v_rsp_125_0_res[0]]}')

        v_result_ = (True, f'0\tOK')
        return v_result_

    # noinspection DuplicatedCode
    def print_ej(self, p_min_nr_check, p_max_nr_check):
        self.msg_res_err = ''
        for nr_check in range(p_min_nr_check, p_max_nr_check + 1):
            v_param_ = f'3\t{nr_check}\t0\t'

            v_rsp_125_3 = self.device.SendEx(488839203, 125, v_param_, '')
            # v_rsp_125_3 = send_fp(488839203, 125, v_param_, '')  # emulator raspuns  FP

            logger.info(f'v_rsp_125_3, param: {v_param_.encode()}, result: {v_rsp_125_3}')
            v_rsp_125_3_res = v_rsp_125_3[1].split('\t')
            if v_rsp_125_3[0] and v_rsp_125_3_res[0] == '0':
                logger.info(f'v_rsp_125_3, print check {nr_check} ok')
            else:
                logger.error(f'v_rsp_125_3, Check: '
                             f'{v_param_.encode()}, ERR {v_rsp_125_3_res[0]} {LIST_ERR[v_rsp_125_3_res[0]]}')

        v_result_ = (True, f'0\tOK')
        self.EJ_OPERATIONS = 'OK'
        return v_result_

    def fiscal_receipt(self, p_code, p_type='form'):
        logger.info(f'Run, param: {p_code}, {p_type}')
        logger.info(f'datecs_protocol: {self.datecs_protocol}')
        v_res = ''
        p_code = self.read_code(p_code)
        for row in p_code:
            v_param = row['param'].replace("\r", "")
            v_command = int(row['command'])
            if v_command == 61:
                try:
                    datetime.strptime(v_param, '%d-%m-%y %H:%M')
                except Exception as err:
                    logger.error(f'fiscal_receipt, v_command 61: {err}')
                    self.msg_res = 'Format data incorect, ex: DD-MM-YY HH:MM (01-12-21 14:01)'
                    break

            if self.datecs_protocol == 3:
                v_command, v_param = self.param_convert_new_protocol_old(v_command, v_param)
            else:
                v_command, v_param = self.param_convert_new_protocol(v_command, v_param)

            if v_command == -1:
                v_rsp = [False, v_param]
            elif v_command == 119:
                v_rsp = v_param
            else:
                v_rsp = self.device.SendEx(488839203, v_command, v_param, '')

            logger.info(f'Result FP=> {v_command}:{v_rsp}')
            if p_type == 'form':

                if v_command == 56 and v_rsp[1] == "":
                    v_res += "<pre><FONT COLOR='#070707'>I: " + str(v_command) + ", " + row[
                        'param'] + "<FONT COLOR='#ff0000'>\nO: " + "Eroare inchidere bon" + "</pre></br>"
                else:
                    v_res += "<pre><FONT COLOR='#070707'>I: " + str(v_command) + ", " + row[
                        'param'] + "<FONT COLOR='#00CC00'>\nO: " + str(v_rsp) + "</pre></br>"
            elif p_type == 'server':
                v_resp_code = str(v_rsp[1])
                v_resp_code = v_resp_code[:v_resp_code.find('\t')]
                if v_rsp[0] and (v_resp_code == '0' or v_resp_code == ''):
                    v_res = 0
                    if v_command == 62:
                        try:
                            self.msg_res = v_rsp[1].split("\t")[1]
                        except IndexError:
                            self.msg_res = 'Null'
                    elif v_command == 65:
                        try:
                            self.msg_res = v_rsp[1][1:]
                        except IndexError:
                            self.msg_res = 'Null'
                    elif v_command == 119:
                        self.msg_res = self.EJ_OPERATIONS
                    else:
                        self.msg_res = 'OK'
                    self.msg_res_err = ''
                    logger.info(f'self.msg_res: {self.msg_res}')
                else:
                    v_res = -1
                    # self.msg_res += str(v_rsp) + "\n"
                    v_err_send = self.device.Send(488839203, 100, f'{v_resp_code}\t', '')
                    v_text_err = str(v_err_send[1])
                    v_step1 = v_text_err.find('\\t')
                    v_step2 = v_text_err.find('\\t', v_step1 + 2)
                    v_step3 = v_text_err.find('\\t', v_step2 + 2)

                    v_text = v_text_err[v_step2 + 2:v_step3]
                    try:
                        v_err_fp_doc = LIST_ERR[v_resp_code]
                        logger.info(f'v_err_fp_doc: {v_err_fp_doc}')
                    except Exception as err:
                        logger.info(f'Eroare cautare in LIST_ERR: {err}')
                        v_err_fp_doc = v_text
                    self.msg_res = f'ERR, CMD-{v_command}: {v_rsp}, \n{v_resp_code}: {v_err_fp_doc}'
                    self.msg_res_err += f'{v_command}: {v_rsp}, \n{v_resp_code}: {v_err_fp_doc}'
                    break
        # self.close_port()
        return v_res

    def close_port(self):
        logger.info(f'Run close port')
        res = self.device.ClosePort()

        logger.info(f'Return: {res}')
        return res

    def read_code(self, code):
        logger.info(f'Run, param: {code}')
        res = []
        code = code.split('\n')
        for row in code:
            row = str(row)
            item = row.find(',')
            if item == -1:
                line = {
                    'command': row[0:],
                    'param': ''
                }
                res.append(line)
            else:
                if int(row[0:item]) in (42, 54):
                    for v_val in explode_text(row[item + 1:], self.len_printing_text):
                        line = {
                            'command': row[0:item],
                            'param': v_val
                        }
                        res.append(line)
                else:
                    line = {
                        'command': row[0:item],
                        'param': row[item + 1:]
                    }
                    res.append(line)

        logger.info(f'Return: {res}')
        return res
