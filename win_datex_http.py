import sys

from PyQt4 import QtGui
from uis.form_datex import Ui_Form
from FPrinter_Driver.FP_Datex import FP_Datex as FPD


class win_datex(QtGui.QMainWindow):

    def __init__(self):
        super(win_datex, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.datex = FPD()

        self.ui.cb_PaymentType.addItems(('Numerar', 'Cu card'))

        self.ui.bt_PrintFiscReceipt.clicked.connect(self.bt_PrintFiscReceipt_click)
        self.ui.bt_PrintNonFiscalReceipt.clicked.connect(self.bt_PrintNonFiscalReceipt_click)
        self.ui.bt_ReportX.clicked.connect(self.bt_ReportX_click)
        self.ui.bt_ReportZ.clicked.connect(self.bt_ReportZ_click)

    def bt_PrintFiscReceipt_click(self):
        footerText = str(self.ui.ln_Footer.text())
        headerText = str(self.ui.ln_Header.text())
        paymentType = self.ui.cb_PaymentType.currentText()

        if len(footerText) > 0:
            self.datex.FooterText = footerText
        if len(headerText) > 0:
            self.datex.HeaderText = headerText
        if paymentType == 'Cu card':
            self.datex.Payments['Code'] = "4"

        PLU = [{
            "Amount": 2.0,
            "Discount": 1.5,
            "Name": "Coca-Cola 0.5L",
            "PLU": 0,
            "Price": 12.33,
            "VAT": "A"
        }, {
            "Amount": 1.0,
            "Discount": 2.2,
            "Name": "Ciocolata Mars",
            "PLU": 0,
            "Price": 7.30,
            "VAT": "A"
        }]
        self.datex.setFiscalReceiptPLU(PLU)
        res =  self.datex.PrintFiscalReceipt()

        self.ui.te_result.setText(str(res))

        # QtGui.QMessageBox.about(self, "INFO", str(paymentType))

    def bt_PrintNonFiscalReceipt_click(self):
        pload = { "Lines":["Text liber", "Text liber2"] }
        res = self.datex.PrintNonFiscalReceipt(pload)

        self.ui.te_result.setText(str(res))

    def bt_ReportX_click(self):
        res = self.datex.PrintReportX()

        self.ui.te_result.setText(str(res))

    def bt_ReportZ_click(self):
        res = self.datex.PrintReportZ()

        self.ui.te_result.setText(str(res))

def main():
    app = QtGui.QApplication([])
    application = win_datex()
    application.show()
    sys.exit(app.exec_())

main()