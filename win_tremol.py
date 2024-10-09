from PyQt4 import QtGui
from uis.form_tremol import Ui_Tremol
import sys
from FPrinter_Driver.FP_Tremol import FP_Tremol as FPT

class win_tremol(QtGui.QMainWindow):

    def __init__(self):
        super(win_tremol, self).__init__()
        self.ui = Ui_Tremol()
        self.ui.setupUi(self)
        self.tremol = FPT()

        self.ui.bt_sendCode.clicked.connect(self.bt_sendCode_click)
        self.ui.bt_findConnection.clicked.connect(self.bt_findConnection_click)
        self.ui.bt_OpenCommport.clicked.connect(self.bt_OpenCommport_click)

        self.ui.t_result.setDisabled(0)
        self.ui.t_code.setDisabled(1)
        self.ui.bt_sendCode.setDisabled(1)

    def bt_sendCode_click(self):
        code = self.ui.t_code.toPlainText()
        if code == '':
            QtGui.QMessageBox.about(self, "INFO", 'Introduceti date in cimul de mai sus')
        else:
            res = self.tremol.fiscal_receipt(code, 'form')
            self.ui.t_result.setText(res)

    def bt_findConnection_click(self):
        self.tremol.FindPort()
        self.ui.ln_commport.setText(str(self.tremol.comm_port))
        self.ui.ln_boud.setText(str(self.tremol.baud))

    def bt_OpenCommport_click(self):
        comm_port = self.ui.ln_commport.text()
        baud = self.ui.ln_boud.text()
        if len(comm_port) > 0 and len(baud) > 0:
            self.tremol.comm_port = str(comm_port)
            self.tremol.baud = str(baud)
            self.tremol.OpenPort()
            self.ui.t_result.setText(str(self.tremol.comm_port) + ' ' + str(self.tremol.baud))
            self.ui.t_code.setDisabled(0)
            self.ui.bt_sendCode.setDisabled(0)
        else:
            QtGui.QMessageBox.about(self, "INFO", 'Introduceti datele pentru conexiune')


def main():
    app = QtGui.QApplication([])
    application = win_tremol()
    application.show()
    sys.exit(app.exec_())

main()