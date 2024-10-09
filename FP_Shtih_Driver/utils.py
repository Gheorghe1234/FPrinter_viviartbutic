import logging

from FP_Shtih_Driver.protocol_shtrih import Protocol as FpShtrih
from FP_Shtih_Driver.commands import *
from .handlers import commands as hc
from datetime import datetime


logger = logging.getLogger(__name__)


class FpUtil:
    def __init__(self, p_port, p_baudrate):
        logger.info(f'Init module FPUtil, param: {p_port}, {p_baudrate}')
        self.response_text = ''
        self.error_text = ''
        self.sumPaymentNonReg = 0
        self.sumFiscalBon = 0
        self.sumPaymentsOp53 = 0
        self.PaymentMode = 0
        self.v_port = p_port
        self.v_baudrate = p_baudrate
        self.device = FpShtrih(self.v_port, self.v_baudrate, 10)
        self.send = Commands(self.device)
        self.pay_type_list = {'N': 1, 'P': 0, 'E': 2, 'U': 3}
        self.pay_type_list_convert = {self.pay_type_list[k]: k for k in self.pay_type_list}
        self.payment_sum = {'N': 0, 'P': 0, 'E': 0, 'U': 0}

    def connect(self):
        logger.info(f'Connect from device')
        try:
            self.device.connect()
        except Exception as ex:
            logger.error(f'Error connection port {self.v_port} \n {ex}')
            return 1
        else:
            return 0

    def final_cut(self):
        for i in range(5):
            self.send.print_string('')
        # self.send.feed(6)
        self.send.cut()

    def disconnect(self):
        logger.info(f'Disconnect from devoce')
        self.device.disconnect()

    def chek_result(self, p_res):
        v_res = str(p_res)
        v_err_pos = v_res.find(hc.ERROR_CODE_STR)
        v_len = len(hc.ERROR_CODE_STR) + 3
        v_pos1 = v_len + v_err_pos
        v_pos2 = v_res[v_err_pos:].find(',') + v_err_pos

        v_err = v_res[v_pos1:v_pos2]
        self.response_text = v_res

        return v_err

    def code_processing(self, p_code, p_params):
        logger.info(f'Code Processing, param: {p_code}, {p_params}')
        v_params = str(p_params)
        v_payment_mode = self.pay_type_list

        v_tax_group = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
        }
        if p_code == 38:
            v_res = self.send.open_non_fiscal_document()
            # v_res = self.send.title_doc()
            v_res = self.chek_result(v_res)
        elif p_code == 39:
            v_res = self.send.close_non_fiscal_document()
            # v_res = self.send.finis_document()
            v_res = self.chek_result(v_res)
        elif p_code == 42:
            v_res = self.send.print_string(v_params)
            v_res = self.chek_result(v_res)
        elif p_code == 45:
            v_res = self.send.cut()
            v_res = self.chek_result(v_res)
        elif p_code == 48:
            try:
                v_par_list = v_params.split(',')
                v_op_code = int(v_par_list[0])
                v_op_pwd = int(v_par_list[1])
                v_till_nmb = int(v_par_list[2])

                logger.info(f'Operation 48, param: {v_op_code}, {v_op_pwd}, {v_till_nmb}')
                v_res = self.send.open_check(0, v_op_pwd)
                v_res = self.chek_result(v_res)
            except ValueError:
                v_res = 'Nu ati indicat parametrii'
                self.errorCode = 2
            except Exception as err:
                logger.error(err)
                v_res = err
                self.errorCode = 2
        elif p_code == 49:
            try:
                v_pos_tab = v_params.find('\\t')
                # v_tab = bytes(v_params[0:v_pos_tab])
                v_tab = v_params[0:v_pos_tab]
                v_tax_cd = v_tax_group[v_params[v_pos_tab + 2:v_pos_tab + 3]]
                # v_pos_price = v_params.find('.')
                v_pos_price_start = v_pos_tab + 3
                v_pos_price_end = len(v_params) if v_params.find('*') == -1 else v_params.find('*')
                v_price = float(v_params[v_pos_price_start:v_pos_price_end])
                v_pos_qwan = v_params.find('*')
                if v_pos_qwan == -1:
                    v_qwan = 1
                    self.sumFiscalBon += v_price
                else:
                    v_qwan = float(v_params[v_pos_qwan + 1:])
                    self.sumFiscalBon += (v_price * v_qwan)
                v_res = self.send.sale((v_tab, int(v_qwan*1000), int(v_price*100)), tax1=v_tax_cd)
                v_res = self.chek_result(v_res)
            except KeyError:
                v_res = 'Nu ati indicat parametrii'
                self.errorCode = 2
        elif p_code == 53:
            if v_params == '':
                v_res = "Nu ati indicat parametrii"
                self.errorCode = 2
            else:
                v_pos_amount = v_params.find('.')
                v_tab = v_params[2:3]
                # v_amount = v_params[3:v_pos_amount + 3]
                v_amount = v_params[3:]

                if v_tab == '':
                    v_paid_mode_nr = 0
                    v_paid_mode_dict = 'P'
                else:
                    v_paid_mode_nr = v_payment_mode[v_tab]
                    v_paid_mode_dict = v_tab

                # if v_amount == '':
                if len(v_amount) <= 1:
                    v_amount_int = self.sumFiscalBon - self.sumPaymentNonReg
                else:
                    v_amount_int = float(v_params[3:])
                    self.sumPaymentNonReg += v_amount_int

                # v_res = self.PaymentEx(v_amount, v_paid_mode)
                self.payment_sum[v_paid_mode_dict] = int(v_amount_int*100)
                # self.PaymentMode = int(v_paid_mode_nr)
                self.sumPaymentsOp53 = int(v_amount_int*100)
                v_res = 0
        elif p_code == 56:
            v_cash = self.payment_sum[self.pay_type_list_convert[0]]
            v_payment_type2 = self.payment_sum[self.pay_type_list_convert[1]]
            v_payment_type3 = self.payment_sum[self.pay_type_list_convert[2]]
            v_payment_type4 = self.payment_sum[self.pay_type_list_convert[3]]
            print(self.payment_sum)

            # v_res = self.send.close_check(cash=self.sumPaymentsOp53, payment_type2=1, payment_type3=1, payment_type4=1)
            v_res = self.send.close_check(cash=v_cash, payment_type2=v_payment_type2, payment_type3=v_payment_type3, payment_type4=v_payment_type4)
            v_res = self.chek_result(v_res)
        elif p_code == 61:
            try:
                v_params = datetime.strptime(v_params, '%d-%m-%y %H:%M')
            except Exception:
                v_res = 'Format data incorect, ex: DD-MM-YY HH:MM (01-12-21 14:01)'
            else:
                v_res = self.send.set_datetime(v_params)
        elif p_code == 69:
            if v_params == 0:
                v_res = self.send.x_report()
                v_res = self.chek_result(v_res)
            elif v_params == 2:
                v_res = self.send.z_report()
                v_res = self.chek_result(v_res)
            else:
                v_res = self.send.x_report()
                v_res = self.chek_result(v_res)
        elif p_code == 70:
            v_params = float(v_params) * 100
            if v_params > 0:
                v_res = self.send.income(int(v_params))
            else:
                v_res = self.send.outcome(abs(int(v_params)))
            v_res = self.chek_result(v_res)
        elif p_code == 106:
            v_res = self.send.open_drawer()
            v_res = self.chek_result(v_res)
        else:
            v_res = "nu este asa cod"

        return str(p_code) + ': ' + str(v_res)

    def fiscal_receipt(self, p_code, p_type='server'):
        v_res = ''
        v_code = self.trans_code(p_code)
        for row in v_code:
            rsp = self.code_processing(int(row['comand']), str(row['param']))
            try:
                err = int(rsp[rsp.find(':') + 2:rsp.find(':') + 3])
            except ValueError:
                err = -1

            if p_type == 'form':
                if err == 0:
                    text = ' Succes comand' if self.response_text == None else ' ' + self.response_text
                    v_res += "<FONT COLOR='#00CC00'>" + rsp + text + "<br>"
                elif err == -1:
                    v_res += "<FONT COLOR='#ff0000'>" + rsp[0:rsp.find(':') + 2] + self.response_text + "<br>"
            elif p_type == 'server':
                if err == 0:
                    v_res = "OK"
                else:
                    v_res += str(rsp) + str(self.response_text) + "\n"
                    # res += str(rsp) + str(self.error_text)
                    break
        self.final_cut()
        return v_res

    @staticmethod
    def trans_code(code):
        logger.info(f'We transform the variable into a list , param:\n {code}')
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
        logger.info(f'return: {res}')
        return res



