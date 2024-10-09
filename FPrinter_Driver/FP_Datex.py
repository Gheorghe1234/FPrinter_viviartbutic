# coding=utf-8
import logging
from datetime import datetime

import requests
from win32com import client
import serial
import os
import json
from CONSTANT import *
from Support.getLog import Log
from UNA_Support.Utility import *


logger = logging.getLogger(__name__)


class DATEX_Comm:
    def __init__(self):
        logger.info(f'Init DATEX_Comm module')
        self.device = client.Dispatch("Wtdedit.FpAtl.1")
        self.msg_res = ''
        self.EJ_OPERATIONS = ''
        self.log = Log(LOG_CONST.FP_Log, LOG_CONST.LOGSavePath)

    def get_open_port(self, com, baudrate=9600):
        logger.info(f'Func. get_open_port run, param: [com {com}], [baudrate {baudrate}]')
        res1 = self.device.OpenPortL(911304495, com, baudrate)
        res2 = self.device.Send(488839203, 62, '', '')
        if res1 is True and res2[0] is True:
            res = 0
        else:
            res = 1

        logger.info(f'return: {res}, {res1}, {res2}')
        return res, res1, res2

    def open_port(self, com, baudrate=9600):
        logger.info(f'Run, param: {com}, {baudrate}')
        res = 1
        repeat = 1
        res1, res2 = '', ''
        for i in range(1, 6):
            res, res1, res2 = self.get_open_port(com, baudrate)
            repeat = i
            if res == 0:
                break

        self.msg_res = '[{repet}] OpenPortL: {res1}, Comand 62: {res2}'.format(res1=res1, res2=res2, repet=repeat)

        logger.info(f'Return: {res}, self.msg_res-{self.msg_res}')
        return res

    def fiscal_receipt(self, code, p_type='form'):
        logger.info(f'Run, param: {code}, {p_type}')
        res = ''
        code = self.read_code(code)
        for row in code:
            rsp = '0'
            param = row['param'].replace("\r", "")
            command = int(row['comand'])
            if command == 61:
                try:
                    datetime.strptime(param, '%d-%m-%y %H:%M')
                except Exception:
                    self.msg_res = 'Format data incorect, ex: DD-MM-YY HH:MM (01-12-21 14:01)'
                    break
            rsp = self.device.Send(488839203, command, param, '')
            logger.info(f'Result FP=> {command}:{rsp}')
            if p_type == 'form':
                if command == 56 and rsp[1] == "":
                    res += "<pre><FONT COLOR='#070707'>I: " + str(command) + ", " + row[
                        'param'] + "<FONT COLOR='#ff0000'>\nO: " + "Eroare inchidere bon" + "</pre></br>"
                else:
                    res += "<pre><FONT COLOR='#070707'>I: " + str(command) + ", " + row[
                        'param'] + "<FONT COLOR='#00CC00'>\nO: " + str(rsp) + "</pre></br>"
            elif p_type == 'server':
                if rsp[0] == True and rsp[1] != u'F':
                    res = 0
                    if command == 48 and rsp[1] == u'':
                        self.msg_res = 'Eroare deschidere bon fiscal ' + str(rsp)
                        break
                    if command == 56 and rsp[1] == u'':
                        self.msg_res = 'Eroare inchidere bon fiscal ' + str(rsp)
                        break
                    if command == 38 and rsp[1] == u'':
                        self.msg_res = 'Eroare deschidere bon fiscal ' + str(rsp)
                        break
                    if command == 39 and rsp[1] == u'':
                        self.msg_res = 'Eroare inchidere bon fiscal ' + str(rsp)
                        break
                    if command == 65:
                        self.msg_res = str(rsp[1])
                        break
                    if command == 62:
                        self.msg_res = str(f'{rsp[1]}')
                        break
                    if command == 119 and param.find('R') !=-1:
                        self.EJ_OPERATIONS = ''
                        result = self.device.Send(488839203, command, param, '')
                        self.EJ_OPERATIONS += result[1][2:] + '\n'
                        while True:
                            result = self.device.Send(488839203, 119, 'N', '')
                            self.EJ_OPERATIONS += result[1][2:] + '\n'
                            if result[1] == u'F':
                                break
                        self.msg_res = self.EJ_OPERATIONS
                        print(self.EJ_OPERATIONS)
                        self.log.Info(self.EJ_OPERATIONS)
                        break

                    self.msg_res = 'OK'
                elif rsp[0] == True and command == 119:
                    self.msg_res = self.EJ_OPERATIONS + 'F'
                    self.EJ_OPERATIONS = ''
                else:
                    res = -1
                    self.msg_res += str(rsp) + "\n"
                    break
        self.close_port()
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
                    'comand': row[0:],
                    'param': ''
                }
            else:
                line = {
                    'comand': row[0:item],
                    'param': row[item+1:]
                }
            res.append(line)

        logger.info(f'Return: {res}')
        return res

    def close_port(self):
        logger.info(f'Run close port')
        res = self.device.ClosePort()

        logger.info(f'Return: {res}')
        return res

    def serial_ports(self):
        logger.info(f'Run')
        if os.name == 'nt':  # Windows
            available = []
            for i in range(1, 512):
                try:
                    sport = 'COM%d' % (i)
                    s = serial.Serial(sport, baudrate=128000)
                    available.append(sport)
                    s.close()
                except (serial.SerialException, ValueError):
                    pass
            return available
        else:  # macOS and Linux
            from serial.tools import list_ports
            return [port[0] for port in list_ports.comports()]


class FP_Datex:
    def __init__(self):
        self.Payments = {}
        self.FiscalReceiptURL = 'http://localhost:3333/fpservice/json/PrintBill'
        self.NonFiscalReceiptURL = 'http://localhost:3333/fpservice/json/PrintNonFiscalBill'
        self.ReportZURL = 'http://localhost:3333/fpservice/json/PrintReportZ'
        self.ReportXURL = 'http://localhost:3333/fpservice/json/PrintReportX'
        self.GetStateURL = 'http://localhost:3333/fpservice/json/GetState'
        self.CashOutURL = 'http://localhost:3333/fpservice/json/CashOut'
        self.FiscalReceiptPload = {}
        self.PLU = []
        self.DiscountSum = 0
        self.FooterText = "Thank you!"
        self.HeaderText = 'Operator 1'
        self.Number = "1"
        self.Payments['Code'] = "1"
        self.Payments['PaymentSum'] = 50
        self.sumFiscalBon = 0
        self.FreeText = None
        self.RecipeType = None

    def PrintFiscalReceipt(self):
        pload = self.FiscalReceiptPload
        r = requests.post( self.FiscalReceiptURL, json=pload)

        return r.text

    def PrintNonFiscalReceipt(self, pload):
        r = requests.post(self.NonFiscalReceiptURL, json=pload)

        return r.text

    def PrintReportZ(self):
        r = requests.get(self.ReportZURL)

        return r.text

    def PrintReportX(self):
        r = requests.get(self.ReportXURL)

        return r.text

    def CashOut(self, suma):
        jsuma = { "Suma": suma}
        print (jsuma)
        r = requests.post(self.CashOutURL, json=jsuma)
        if r.ok:
            return r.text
        else:
            return 'URL incorect'

    def GetState(self):
        r = requests.get(self.GetStateURL)

        return r.text

    def setFiscalReceiptPLU(self, PLU):
        pload = {
            "DiscountSum": self.DiscountSum,
            "FooterText": self.FooterText,
            "HeaderText": self.HeaderText,
            "Lines": PLU,
            "Number": self.Number,
            "Payments": [{
                "Code": self.Payments['Code'],
                "PaymentSum": self.Payments['PaymentSum']
            }]
        }
        self.FiscalReceiptPload = pload
        return pload

    def fiscal_receipt(self, code, type):
        res = ''
        code = self.read_code(code)
        for row in code:
            param = str(row['param']).replace('\r', '')
            comand = int(row['comand'])
            rsp = self.CodeConv(comand, str(row['param']))
            try:
                pos_JSON = rsp.find(': {')
                JSON_MSG = rsp[pos_JSON + 2:] if pos_JSON != -1 else {u'ErrorCode': 20, u'ErrorMessage': rsp, u'TaskId': 0}
                MSG_FP = json.loads(JSON_MSG) if pos_JSON != -1 else JSON_MSG
                ErrorCode = MSG_FP['ErrorCode']
                State = MSG_FP['State'] if comand == 71 else 0
                if comand == 71:
                    print(self.GETStateFPText(State))
                else:
                    print(MSG_FP)

                err = 0
                if type == 'form':
                    if err == 0:
                        res += "<FONT COLOR='#00CC00'>" + rsp + "<br>"
                    else:
                        res += "<FONT COLOR='#ff0000'>" + rsp + "<br>"
                elif type == 'server':
                    try:
                        if ErrorCode == 0 and State == 0:
                            res = "OK"
                        elif ErrorCode == 0 and State != 0:
                            res = str(State)
                        else:
                            res += rsp + "\n"
                    except Exception as ex:
                        res = str(ex)
            except Exception as ex:
            # except KeyboardInterrupt as ex:
                res = str(ex)
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
                    'param': row[item+1:]
                }
            res.append(line)

        return res

    def CodeConv(self, code, params):
        params = str(params)
        paymentMode = {
            'N': 1,
            'P': 4,
        }
        if code == 38:
            res = res = {u'ErrorCode': 0, u'ErrorMessage': 0, u'TaskId': 0}
            self.FreeText = []
            self.RecipeType = 'NonFiscal'
        elif code == 39:
            pload = {"Lines": self.FreeText}
            res = self.PrintNonFiscalReceipt(pload)
            self.FreeText = None
            self.RecipeType = None
        elif code == 42:
            if self.RecipeType == 'NonFiscal':
                self.FreeText.append(params.replace("\r", ""))
            else:
                self.FooterText = self.FooterText +  str(params)
            res = {u'ErrorCode': 0, u'ErrorMessage': 0, u'TaskId': 0}
        elif code == 49:
            try:
                pos_Tab = params.find('\\t')
                Tab = bytes(params[0:pos_Tab])
                TaxName = params[pos_Tab + 2:pos_Tab + 3]
                params2, err = extract_str(params+'/', '\\t')
                pos_Qwan = params2.find('*')
                Price = float(params2[1:pos_Qwan])
                if pos_Qwan == -1:
                    Qwan = 1
                    self.sumFiscalBon += Price
                else:
                    Qwan = float(params2[pos_Qwan + 1:])
                    self.sumFiscalBon += (Price * Qwan)
                PLU = {
                        "Amount": float(Qwan),
                        "Discount": 1.5,
                        "Name": Tab,
                        "PLU": 0,
                        "Price": float(Price),
                        "VAT": TaxName
                    }
                self.PLU.append(PLU)
                res = {u'ErrorCode': 0, u'ErrorMessage': 0, u'TaskId': 0}
            except KeyError:
                res = 'Nu ati indicat parametrii'
                self.errorCode = 2
        elif code == 45: res = 0
        elif code == 48:
            try:
                self.RecipeType = 'Fiscal'
                OpCode = int(params[0:1])
                self.HeaderText = 'Operator ' + str(OpCode)
                self.FooterText = ''
                res = {u'ErrorCode': 0, u'ErrorMessage': 0, u'TaskId': 0}
            except ValueError:
                res = 'Nu ati indicat parametrii'
                self.errorCode = 2
        elif code == 53:
            if params == '':
                res = "Nu ati indicat parametrii"
                self.errorCode = 2
            else:
                pos_Amount = params.find('.')
                summ_received, err = extract_str(params+'/', '\\t')
                # Tab = params[2:3]
                Tab = summ_received[:1]
                # Amount = params[3:pos_Amount + 3]
                Amount = summ_received[1:]
                print (Amount, Tab, '-------------------')
                if Amount == '':
                    Amount = format(self.sumFiscalBon, '.2f')
                    self.sumFiscalBon = 0
                else:
                    self.sumFiscalBon = 0
                    # Amount = float(params[3:pos_Amount + 3])
                    Amount = float(Amount)

                self.Payments['Code'] = str(paymentMode[Tab])
                self.Payments['PaymentSum'] = float(Amount)
                res = {u'ErrorCode': 0, u'ErrorMessage': 0, u'TaskId': 0}
        elif code == 56:
            self.setFiscalReceiptPLU(self.PLU)
            print(self.FiscalReceiptPload)
            res = self.PrintFiscalReceipt()
            self.PLU = []
            self.FiscalReceiptPload = {}
            self.RecipeType = None
            self.FooterText = ''
        elif code == 69:
            if int(params) == 2:
                res = self.PrintReportX()
            else:
                res = self.PrintReportZ()
        elif code == 70:
            suma = float(params)
            res = self.CashOut(suma)
        elif code == 71: res = self.GetState()
        else: res = "nu este asa cod"

        return str(code) + ': ' + str(res)

    def GETStateFPText(self, code):
        TextState = {
            0: 'OK',
            1: 'No printer connection',
            2: 'There is no paper in the printer / Printer Cover Open',
            4: 'Fiscal check opened',
            5: 'Printer Cover Open',
            20: 'Unknown error'
        }

        return TextState[int(code)]