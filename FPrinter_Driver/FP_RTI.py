# coding=utf-8
import logging
import ctypes
from FPrinter_Driver.general_method import *

logger = logging.getLogger(__name__)


class pyReceiptRowStructure(ctypes.Structure):
    _fields_ = [("name", ctypes.c_wchar_p),
                ("price", ctypes.c_double),
                ("count", ctypes.c_double),
                ("prod_id", ctypes.c_int32),
                ("discount", ctypes.c_double),
                ("tax_group", ctypes.c_char)]


class Rti1000:
    def __init__(self, p_current_path):
        logger.info(f'Init Rti1000 module, param [{p_current_path}]')

        self.count_prod_check = 1
        self.v_arr = (pyReceiptRowStructure * self.count_prod_check)()
        self.current_sc = 0

        self.sum_check_internal = 0
        self.sum_check_cash = 0
        self.sum_check_card = 0

        # self.rti1000 = ctypes.CDLL(f'{p_current_path}\\rti1000.dll')
        self.rti1000 = ctypes.CDLL(f'C:\\Users\\user\\Desktop\\NGaidarji\\RTI_driver\\rti1000.dll')

        '''
          первоначальная настройка (входные параметры: название ком порта, скорость связи)
        '''
        self.rti1000.Setup.argtypes = [ctypes.c_wchar_p,
                                       ctypes.c_wchar_p]

        '''
          закрытие смены, печать Z отчета (результат выполнения операции, может быть или 'OK' или текст ошибки)
        '''
        self.rti1000.ZReport.restype = ctypes.c_wchar_p

        '''
          печать X отчета (результат выполнения операции, может быть или 'OK' или текст ошибки)
        '''
        self.rti1000.XReport.restype = ctypes.c_wchar_p

        '''
          печать копии последнего чека (результат выполнения операции, может быть или 'OK' или текст ошибки)
        '''
        self.rti1000.PrintReceiptCopy.restype = ctypes.c_wchar_p

        '''
          сбросить открытый чек (результат выполнения операции, может быть или 'OK' или текст ошибки)
        '''
        self.rti1000.ResetReceipt.restype = ctypes.c_wchar_p

        '''
          получить номер текущего Z отчета (результат выполнения операции, может быть или 'OK' или текст ошибки)
          параметр передается по ссылке, в который вернеться значение номера текущего Z отчета
        '''
        self.rti1000.GetShiftNo.restype = ctypes.c_wchar_p
        self.rti1000.GetShiftNo.argtypes = [ctypes.c_void_p]

        '''
          служебный внос средст в денежный ящик (результат выполнения операции, может быть или 'OK' или текст ошибки)
          входной параметр - сумма внесения
        '''
        self.rti1000.AddMoneyToCashDrawer.restype = ctypes.c_wchar_p
        self.rti1000.AddMoneyToCashDrawer.argtypes = [ctypes.c_double]

        '''
          службный вынос денежных средств (результат выполнения операции, может быть или 'OK' или текст ошибки)
          входной параметр сумма изъятия
        '''
        self.rti1000.GiveMoneyFromCashDrawer.restype = ctypes.c_wchar_p
        self.rti1000.GiveMoneyFromCashDrawer.argtypes = [ctypes.c_double]

        '''
          получить номер текущего чека
          параметр передается по ссылке, в который вернеться значение номера текущего чека
        '''
        self.rti1000.GetReceiptNo.restype = ctypes.c_wchar_p
        self.rti1000.GetReceiptNo.argtypes = [ctypes.c_void_p]

        '''
          получить сумму продаж в текущей смене
          параметр передается по ссылке, в который вернеться значение суммы продаж в текущей смене
        '''
        self.rti1000.GetShiftSalesAmount.restype = ctypes.c_wchar_p
        self.rti1000.GetShiftSalesAmount.argtypes = [ctypes.c_void_p]

        '''
          открыть денежный ящик (результат выполнения операции, может быть или 'OK' или текст ошибки)
        '''
        self.rti1000.OpenCashDrawer.restype = ctypes.c_wchar_p

        '''
          получение статуса фискалки (результат выполнения операции, может быть или 'OK' или текст ошибки)
          все параметры передается по ссылке (серийный номер фискалки, регистрационный номер фискалки, taxNumber, 
          версия прошивки)
        '''
        self.rti1000.GetStatus.restype = ctypes.c_wchar_p
        self.rti1000.GetStatus.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]

        '''
          регистрация кассира (результат выполнения операции, может быть или 'OK' или текст ошибки)
          входной параметр ФИО КАССИРА
        '''
        self.rti1000.RegisterCashier.argtypes = [ctypes.c_wchar_p]
        self.rti1000.RegisterCashier.restype = ctypes.c_wchar_p

        '''
          получить дату/время из фискалки (результат выполнения операции, может быть или 'OK' или текст ошибки)
          параметр передается по ссылке в который вернется строка с текущей датой временем 
          в фискалке в формате yyyy-MM-dd hh:mm:ss
        '''
        self.rti1000.GetDateTime.argtypes = [ctypes.c_void_p]
        self.rti1000.GetDateTime.restype = ctypes.c_wchar_p

        '''
          продажа/печать чека (результат выполнения операции, может быть или 'OK' или текст ошибки)
          список параметров
          1. Сумма оплаты банковской картой
          2. Сумма оплаты наличными
          3. Общая сумма скидки по чеку (печатается в виде комментария в конце чека)
          4. Общая сумма чека без учета скидки (печатается в виде комментарий в конце чека)
          5. Указатель на массив записей со структурой pyReceiptRowStructure (указатель на массив строк чека)
          6. Количество записей в массиве (по сути количество строк в чеке)
          7. параметр передается по ссылке в результате веренться значение здачи, которая положена по чеку
          8. параметр передается по ссылке в результате веренться строка с Warning сообщением. 
             Пример "Заканчивается бумага"
        '''
        self.rti1000.PrintReceipt.restype = ctypes.c_wchar_p
        self.rti1000.PrintReceipt.argtypes = [ctypes.c_double,
                                              ctypes.c_double,
                                              ctypes.c_double,
                                              ctypes.c_double,
                                              ctypes.c_void_p,
                                              ctypes.c_int32,
                                              ctypes.c_void_p,
                                              ctypes.c_void_p
                                              ]

    def open_port(self, p_com, p_baud_rate=115200):
        logger.info(f'param: [{p_com}, {p_baud_rate}]')
        v_com = f'COM{p_com}'
        self.rti1000.Setup(v_com, p_baud_rate)
        v_res = self.rti1000.ResetReceipt()

        if v_res == 'OK':
            return 0
        else:
            return v_res

    def fiscal_receipt(self, p_code):
        v_res = ''
        self.count_prod_check = p_code.count("49,")
        p_code = read_code(p_code)

        for row in p_code:
            v_rsp = self.code_conv(int(row['comand']), str(row['param']))
            p_pos_err = v_rsp.find('OK')
            # v_err = int(v_rsp[3:p_pos_err])
            v_err = v_rsp
            logger.info(f'err: {v_err}')

            v_res += v_rsp + "\n"
        return v_res

    def code_conv(self, p_code, p_params):

        v_list_cote_tva = {
            'A': '0',  # vat group A;
            'B': '1',  # vat group B;
            'C': '2',  # vat group C;
            'D': '3',  # vat group D;
            'E': '4',  # vat group E;
        }

        try:
            if p_code == 48:
                logger.info(f'count_prod_check: {self.count_prod_check}')
                self.v_arr = (pyReceiptRowStructure*self.count_prod_check)()
                self.current_sc = 0
                v_res = 'OK'
            elif p_code == 49:
                v_param_arr = str(p_params).split('\\t')
                logger.info(f'v_param_arr: {v_param_arr}')
                v_produs_name = v_param_arr[0]
                v_product_detail = v_param_arr[1]
                v_cota_tva = v_product_detail[0:1]
                v_price = v_product_detail[1:v_product_detail.find('*')]
                v_qnt = v_product_detail[v_product_detail.find('*') + 1:]

                self.v_arr[self.current_sc].price = float(v_price)
                self.v_arr[self.current_sc].name = v_produs_name
                self.v_arr[self.current_sc].count = float(v_qnt)
                self.v_arr[self.current_sc].prod_id = 1000 + self.current_sc
                self.v_arr[self.current_sc].discount = 0
                self.v_arr[self.current_sc].tax_group = v_list_cote_tva[v_cota_tva]

                self.sum_check_internal += (float(v_price)*float(v_qnt))

                self.current_sc += 1

                v_res = 'OK'
            elif p_code == 53:
                v_step1 = p_params.find('\\t')

                v_pay_type = p_params[v_step1 + 2:v_step1 + 3]
                v_suma = p_params[v_step1 + 3:]

                if v_pay_type == 'C':  # Tip acitare Card
                    if v_suma == '0' or v_suma == '':
                        self.sum_check_card = self.sum_check_internal - self.sum_check_cash
                    else:
                        self.sum_check_card = float(v_suma)
                else:  # Tip acitare Cash
                    if v_suma == '0' or v_suma == '':
                        self.sum_check_cash = self.sum_check_internal - self.sum_check_card
                    else:
                        self.sum_check_cash = float(v_suma)

                v_res = 'OK'
            elif p_code == 56:
                logger.info(f'sum_check_card: {self.sum_check_card}')
                logger.info(f'sum_check_cash: {self.sum_check_cash}')

                rest = ctypes.c_double(0)
                has_warning = ctypes.c_bool(0)
                result = self.rti1000.PrintReceipt(self.sum_check_card,
                                                   self.sum_check_cash,
                                                   0,
                                                   0,
                                                   ctypes.pointer(self.v_arr),
                                                   self.count_prod_check,
                                                   ctypes.byref(rest),
                                                   ctypes.byref(has_warning)
                                                   )
                logger.info(f'result: {result}')
                logger.info(f'rest: {rest.value}')
                logger.info(f'has_warning: {has_warning}')
                v_res = f'{result}, rest: {rest.value}, has_warning: {has_warning}'
            elif p_code == 60:
                v_res = self.rti1000.ResetReceipt()
            elif p_code == 69:
                if p_params == '2':
                    v_res = self.rti1000.XReport()
                elif p_params == '0':
                    v_res = self.rti1000.ZReport()
                else:
                    v_res = self.rti1000.ZReport()
            elif p_code == 70:
                v_amount = float(p_params)
                if v_amount >= 0:
                    v_res = self.rti1000.AddMoneyToCashDrawer(v_amount)
                else:
                    v_res = self.rti1000.GiveMoneyFromCashDrawer(v_amount * -1)
            elif p_code == 106:
                v_res = self.rti1000.OpenCashDrawer()
            else:
                v_res = "nu este asa cod"
        except Exception as ex:
            v_res = f'-2\tEroare in sintaxa comanda: {p_code}'
            logger.error(f'{v_res}')
            logger.error(f'{ex}')

        logger.info(str(p_code) + ': ' + str(v_res))
        return str(p_code) + ': ' + str(v_res)
