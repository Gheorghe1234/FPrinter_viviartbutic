from PyQt4 import QtGui
from uis.form_UI_allFP import Ui_Form
import sys

from UI_All_init.UI_Init import UI_Init

class win_tremol(QtGui.QMainWindow):

    def __init__(self):
        super(win_tremol, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init = UI_Init()
        self.FP = UI_Init().FP

        self.ui.cb_Model.addItems(('DATEX', 'TREMOL', 'TREMOL ZFPLAB'))
        self.ui.cb_TypeConnection.addItems(('Serial', 'TCP/IP'))
        self.ui.cb_Port.addItems(('COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'COM10', 'COM11', 'COM12', 'COM13', 'COM14'))
        self.ui.cb_Baud.addItems(('1200', '9600', '19200', '38400', '115200'))
        self.ui.cb_OperatoName.addItems(('Operator 1', 'Operator 2', 'Operator 3', 'Operator 4', 'Operator 5', 'Operator 6'))

        self.ui.bt_OpenConn.clicked.connect(self.bt_OpenConn_click)
        self.ui.bt_CloseConn.clicked.connect(self.bt_CloseConn_click)
        self.ui.bt_SaveOperator.clicked.connect(self.bt_SaveOperator_click)
        self.ui.bt_ReportZ.clicked.connect(self.bt_ReportZ_click)
        self.ui.bt_ReportX.clicked.connect(self.bt_ReportX_click)
        self.ui.bt_ReportDept.clicked.connect(self.bt_ReportDept_click)

        self.ui.cb_OperatoName.setDisabled(1)
        self.ui.ln_OperatorPass.setDisabled(1)
        self.ui.bt_SaveOperator.setDisabled(1)
        self.ui.tb_Reports.setDisabled(1)

    def tb_Info_click(self):
        QtGui.QMessageBox.about(self, "INFO", 'Introduceti date in cimul de mai sus')

    def bt_OpenConn_click(self):
        self.init.ModelFP = int(self.ui.cb_Model.currentIndex())
        self.init.TypeConnection = int(self.ui.cb_TypeConnection.currentIndex())
        self.init.CommPort = int(self.ui.cb_Port.currentIndex()) + 1
        self.init.BaudRate = int(self.ui.cb_Baud.currentText())
        self.init.IPAddress = str(self.ui.ln_IPAddress.text()) if str(self.ui.ln_IPAddress.text()) != '' else '127.0.0.1'
        res = self.init.OpenConnection()
        print(res)

        if res == 0:
            QtGui.QMessageBox.about(self, "INFO", 'Conexiune Printer Reusita')
            self.enabledConn(True)
        else:
            QtGui.QMessageBox.about(self, "ERROR", 'Eroare Conexiune Printer')

    def bt_CloseConn_click(self):
        self.init.ModelFP = -1
        self.init.TypeConnection = -1
        self.init.CommPort = -1
        self.init.BaudRate = -1
        self.init.IPAddress = '127.0.0.1'
        res = self.init.CloseConnection()

        if res == 0:
            QtGui.QMessageBox.about(self, "INFO", 'Conexiune finisata')
            self.enabledConn(False)

    def bt_SaveOperator_click(self):
        self.init.OperatorIndex = int(self.ui.cb_OperatoName.currentIndex()) + 1
        self.init.OperatorName = str(self.ui.cb_OperatoName.currentText())
        self.init.OperatorPass = str(self.ui.ln_OperatorPass.text()) if str(self.ui.ln_OperatorPass.text()) != '' else '0000'

        self.ui.la_CurentOperator.setText('Name: ' + self.init.OperatorName + '    Password: ' + self.init.OperatorPass)
        self.enabledTab(True)
        pass

    def bt_ReportZ_click(self):
        res = self.init.ReportDaily('Z')
        self.ui.te_ResultReport.setText(res)
        print(res)

    def bt_ReportX_click(self):
        res = self.init.ReportDaily('Zlong')
        self.ui.te_ResultReport.setText(res)
        print(res)
        pass

    def bt_ReportDept_click(self):
        res = self.init.ReportDaily('ZDepartament')
        self.ui.te_ResultReport.setText(res)
        print(res)
        pass

    def enabledConn(self, type):
        type1 = 1 if type == True else 0
        type2 = 0 if type == True else 1
        self.ui.cb_Port.setDisabled(type1)
        self.ui.cb_Baud.setDisabled(type1)
        self.ui.cb_Model.setDisabled(type1)
        self.ui.cb_TypeConnection.setDisabled(type1)
        self.ui.ln_IPAddress.setDisabled(type1)

        self.ui.cb_OperatoName.setDisabled(type2)
        self.ui.ln_OperatorPass.setDisabled(type2)
        self.ui.bt_SaveOperator.setDisabled(type2)
        self.ui.tb_Reports.setDisabled(type2)

    def enabledTab(self, type):
        type1 = 1 if type == True else 0
        type2 = 0 if type == True else 1

        self.ui.tb_Reports.setDisabled(type2)

        self.ui.la_ReportsHeader.setText('Reports ' + str(self.init.FPName))



def main():
    app = QtGui.QApplication([])
    application = win_tremol()
    application.show()
    sys.exit(app.exec_())

main()