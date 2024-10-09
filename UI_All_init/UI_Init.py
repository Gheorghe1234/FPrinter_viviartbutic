from FPrinter_Driver.FP_Tremol import FP_Tremol
from FPrinter_Driver.FP_Tremol_ZFPLAB import FP_Tremol as ZFPLAB
from FPrinter_Driver.FP_Datex import DATEX_Comm

class UI_Init:

    def __init__(self):
        self.ModelFP = -1
        self.TypeConnection = -1
        self.CommPort = -1
        self.BaudRate = -1
        self.IPAddress = '127.0.0.1'
        self.OperatorIndex = -1
        self.OperatorName = None
        self.OperatorPass = -1
        self.FP = None
        self.FPName = None
        pass

    def OpenConnection(self):
        if self.ModelFP == 0:
            self.FP = DATEX_Comm()
            self.FPName = 'Datex'
        elif self.ModelFP == 1:
            self.FP = FP_Tremol()
            self.FP.comm_port = self.CommPort
            self.FPName = 'Tremol'
        elif self.ModelFP == 2:
            self.FP = ZFPLAB()
            self.FP.comm_port = 'COM' + str(self.CommPort)
            self.FPName = 'Tremol ZFPLAB'
        else: print("Alegeti Modelul")

        res = self.FP.open_port(self.CommPort)
        print self.CommPort
        print self.FPName
        return res

    def CloseConnection(self):
        res = -1
        try:
            self.FP.close_port()
            self.FPName = None
            res = 0
        except AttributeError:
            res = -1
            pass

        return res

    def ReportDaily(self, type):
        if self.ModelFP == 0:
            # self.FP = DATEX_Comm()
            if type == 'Z':
                res = self.FP.fiscal_receipt('69,0', 'server')
            elif type == 'Zlong':
                res = self.FP.fiscal_receipt('69,0', 'server')
            elif type == 'ZDepartament':
                res = self.FP.fiscal_receipt('117', 'server')
        elif self.ModelFP == 1:
            # self.FP = FP_Tremol()
            self.FP.comm_port = self.CommPort
        elif self.ModelFP == 2:
            # self.FP = ZFPLAB()
            self.FP.comm_port = 'COM' + str(self.CommPort)
        else: print("Alegeti Modelul")

        return res
