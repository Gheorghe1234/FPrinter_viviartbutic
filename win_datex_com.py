from PyQt4 import QtGui
from uis.form_datex_com import Ui_MainWindow
import sys
from FPrinter_Driver.FP_Datex import DATEX_Comm as DT

class win_datex(QtGui.QMainWindow):

    def __init__(self):
        super(win_datex, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.datex = DT()

        self.ui.bt_openConnection.clicked.connect(self.bt_openConnection_click)
        self.ui.bt_closeConnection.clicked.connect(self.bt_closeConnection_click)
        self.ui.bt_sendCode.clicked.connect(self.bt_sendCode_click)

        self.ui.bt_closeConnection.setDisabled(1)
        self.ui.bt_sendCode.setDisabled(1)
        self.ui.te_send.setDisabled(1)
        self.ui.te_result.setDisabled(1)


    def bt_openConnection_click(self):
        com = self.ui.ln_comPort.text()
        if len(com) > 0:
            err = self.datex.open_port(int(com))
            if err == 0:
                self.ui.te_result.setPlainText(str(err))
                self.open_port("connect")
            else:
                self.ui.te_result.setPlainText(str(err))
        else:
            QtGui.QMessageBox.about(self, "INFO", 'Introduceti portul')

    def bt_closeConnection_click(self):
        err = self.datex.close_port()

        self.open_port("disconnect")
        self.ui.te_result.setPlainText('Connection closed')

    def bt_sendCode_click(self):
        code = self.ui.te_send.toPlainText()

        if code == '':
            QtGui.QMessageBox.about(self, "INFO", 'Introduceti date in cimul de mai sus')
        else:
            res = self.datex.fiscal_receipt(code)
            self.ui.te_result.setText(res)

    def open_port(self, status):
        if status == 'connect':
            self.ui.bt_closeConnection.setDisabled(0)
            self.ui.bt_openConnection.setDisabled(1)
            self.ui.bt_sendCode.setDisabled(0)
            self.ui.te_send.setDisabled(0)
            self.ui.te_result.setDisabled(0)
        elif status == 'disconnect':
            self.ui.bt_closeConnection.setDisabled(1)
            self.ui.bt_openConnection.setDisabled(0)
            self.ui.bt_sendCode.setDisabled(1)
            self.ui.te_send.setDisabled(1)
            self.ui.te_result.setDisabled(1)


def main():
    app = QtGui.QApplication([])
    application = win_datex()
    application.show()
    sys.exit(app.exec_())

main()