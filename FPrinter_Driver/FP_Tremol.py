from win32com import client

class FP_Tremol:
    def __init__(self):
        self.zfp = client.Dispatch("Zfpcom.ZekaFP")
        # self.zfp.Setup(10, 115200, 3, 1000)
        self.comm_port = 10
        self.baud = 115200
        self.sumFiscalBon = 0.0
        self.sumPaymentNonReg = 0.0
        self.errorCode = 0

    def OpenPort(self, com = 0):
        self.zfp.Setup(self.comm_port, self.baud, 3, 1000)
        res = self.zfp.GetErrorString(self.zfp.errorCode, 0)
        self.errorCode = self.zfp.errorCode

        return res

    def ClosePort(self):
        pass

    def FindPort(self):
        val = self.zfp.FindFirstFPCOMEx()
        if val:
            self.comm_port = (val >> 24) & 0xFF
            self.baud = val & 0x00FFFFFF
            res = 0
        else:
            res = 1
        return res

    def OpenBon(self):
        self.zfp.OpenBonWithEJ(1, b'0000', 0)
        res = self.zfp.GetErrorString(self.zfp.errorCode, 0)
        self.errorCode = self.zfp.errorCode
        return res

    def CloseBon(self):
        self.zfp.CloseBon()
        res = self.zfp.GetErrorString(self.zfp.errorCode, 0)
        self.errorCode = self.zfp.errorCode
        return res

    def PaperCut(self):
        self.zfp.PaperCut()
        res = self.zfp.GetErrorString(self.zfp.errorCode, 0)
        self.errorCode = self.zfp.errorCode
        return res

    def PrintText(self, line, align, width):
        self.zfp.SetLineWidth(width)  # 38 - 42
        self.zfp.PrintText(line, align)  # 0 = left alignment, 1 = right alignment, 2 = center text)
        res = self.zfp.GetErrorString(self.zfp.errorCode, 0)
        self.errorCode = self.zfp.errorCode
        return res

    def PrintBarcode(self, barcode, type):
        res = self.zfp.PrintBarcode(barcode, type)
        res = self.zfp.GetErrorString(self.zfp.errorCode, 0)
        self.errorCode = self.zfp.errorCode
        return res

    def OpenFiscalBon(self, OpCode, OpPwd):
        self.zfp.OpenFiscalBon(OpCode, OpPwd, 0, 0)
        res = self.zfp.GetErrorString(self.zfp.errorCode, 0)
        self.errorCode = self.zfp.errorCode
        return res

    def SellFreeEx(self, Tab, TaxCd, Price, Qwan):
        self.zfp.SellFreeEx(Tab, TaxCd, Price, Qwan, 0, 0)
        res = self.zfp.GetErrorString(self.zfp.errorCode, 0)
        self.errorCode = self.zfp.errorCode
        return res

    def PaymentEx(self, Amount, PaidMode):
        self.zfp.PaymentEx(Amount, PaidMode, 0, 1, 0)
        res = self.zfp.GetErrorString(self.zfp.errorCode, 0)
        self.errorCode = self.zfp.errorCode
        return res

    def ReportDaily(self, type):
        self.zfp.ReportDaily(type, 0)
        res = self.zfp.GetErrorString(self.zfp.errorCode, 0)
        self.errorCode = self.zfp.errorCode
        return res

    def OfficialSumsEx(self, sum):
        self.zfp.OfficialSumsEx(1, b'0000', 0, sum, '')
        res = self.zfp.GetErrorString(self.zfp.errorCode, 0)
        self.errorCode = self.zfp.errorCode
        return res

    def CloseFiscalBon(self):
        self.zfp.CloseFiscalBon()
        res = self.zfp.GetErrorString(self.zfp.errorCode, 0)
        self.errorCode = self.zfp.errorCode
        return res

    def CodeConv(self, code, params):
        params = str(params)
        paymentMode = {
            'N': 0,
            'P': 1,
            'C': 3
        }
        taxGrup = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
        }
        if code == 38:
            res = self.OpenBon()
        elif code == 39:
            res = self.CloseBon()
        elif code == 42:
            res = self.PrintText(params, 0, 38)
        elif code == 45:
            res = self.PaperCut()
        elif code == 49:
            res = 'n'
            try:
                pos_Tab = params.find('\\t')
                Tab = bytes(params[0:pos_Tab])
                TaxCd = taxGrup[params[pos_Tab + 2:pos_Tab + 3]]
                pos_Price = params.find('.')
                Price = float(params[pos_Tab + 3:pos_Price + 3])
                pos_Qwan = params.find('*')
                if pos_Qwan == -1:
                    Qwan = 1
                    self.sumFiscalBon += Price
                else:
                    Qwan = float(params[pos_Qwan + 1:])
                    self.sumFiscalBon += (Price * Qwan)
                res = self.SellFreeEx(Tab, TaxCd, Price, Qwan)
            except KeyError:
                res = 'Nu ati indicat parametrii'
                self.errorCode = 2
        elif code == 48:
            try:
                OpCode = int(params[0:1])
                OpPwd = bytes(params[2:6])
                TillNmb = params[7:8]
                res = self.OpenFiscalBon(OpCode, OpPwd)
            except ValueError:
                res = 'Nu ati indicat parametrii'
                self.errorCode = 2
        elif code == 53:
            if params == '':
                res = "Nu ati indicat parametrii"
                self.errorCode = 2
            else:
                pos_Amount = params.find('.')
                Tab = params[2:3]
                Amount = params[3:pos_Amount + 3]
                if Amount == '':
                    Amount = format(self.sumFiscalBon - self.sumPaymentNonReg, '.2f')
                else:
                    Amount = float(params[3:pos_Amount + 3])
                    self.sumPaymentNonReg += Amount
                if Tab == '':
                    PaidMode = 0
                else:
                    PaidMode = paymentMode[Tab]
                res = self.PaymentEx(Amount, PaidMode)
        elif code == 56:
            res = self.CloseFiscalBon()
        elif code == 69:
            res = self.ReportDaily(1)
        elif code == 70:
            res = self.OfficialSumsEx(0.01)
        elif code == 84:
            if params == '':
                res = "Nu ati indicat parametrii"
                self.errorCode = 2
            else:
                pos_type = params.find(',')
                barcode_type = params[0:pos_type]
                barcode_value = params[pos_type + 1:]
                res = self.PrintBarcode(barcode_value, int(barcode_type))
        else:
            res = "nu este asa cod"

        return str(code) + ': ' + str(res)
        # return str(Qwan)

    def fiscal_receipt(self, code, type):
        res = ''
        code = self.read_code(code)
        for row in code:
            rsp = self.CodeConv(int(row['comand']), str(row['param']))
            # res += rsp + '\n'
            pos_err = rsp.find(' (')
            err = int(rsp[3:pos_err])
            if type == 'form':
                if err == 0:
                    res += "<FONT COLOR='#00CC00'>" + rsp + "<br>"
                else:
                    res += "<FONT COLOR='#ff0000'>" + rsp + "<br>"
            elif type == 'server':
                    res += rsp + "\n"
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
                    'param': row[item + 1:]
                }
            res.append(line)

        return res