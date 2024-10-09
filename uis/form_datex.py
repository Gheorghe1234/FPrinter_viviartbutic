# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis\form_datex_http.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(677, 480)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 661, 461))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.bt_ReportZ = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_ReportZ.setFont(font)
        self.bt_ReportZ.setObjectName(_fromUtf8("bt_ReportZ"))
        self.gridLayout.addWidget(self.bt_ReportZ, 8, 0, 1, 2)
        self.te_result = QtGui.QTextEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        self.te_result.setFont(font)
        self.te_result.setObjectName(_fromUtf8("te_result"))
        self.gridLayout.addWidget(self.te_result, 0, 2, 10, 1)
        self.bt_PrintFiscReceipt = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_PrintFiscReceipt.setFont(font)
        self.bt_PrintFiscReceipt.setObjectName(_fromUtf8("bt_PrintFiscReceipt"))
        self.gridLayout.addWidget(self.bt_PrintFiscReceipt, 3, 0, 1, 2)
        self.cb_PaymentType = QtGui.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cb_PaymentType.setFont(font)
        self.cb_PaymentType.setObjectName(_fromUtf8("cb_PaymentType"))
        self.gridLayout.addWidget(self.cb_PaymentType, 2, 1, 1, 1)
        self.ln_Footer = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ln_Footer.setFont(font)
        self.ln_Footer.setObjectName(_fromUtf8("ln_Footer"))
        self.gridLayout.addWidget(self.ln_Footer, 1, 1, 1, 1)
        self.la_Header = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.la_Header.setFont(font)
        self.la_Header.setObjectName(_fromUtf8("la_Header"))
        self.gridLayout.addWidget(self.la_Header, 0, 0, 1, 1)
        self.bt_PrintNonFiscalReceipt = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_PrintNonFiscalReceipt.setFont(font)
        self.bt_PrintNonFiscalReceipt.setObjectName(_fromUtf8("bt_PrintNonFiscalReceipt"))
        self.gridLayout.addWidget(self.bt_PrintNonFiscalReceipt, 4, 0, 1, 2)
        self.la_Footer = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.la_Footer.setFont(font)
        self.la_Footer.setObjectName(_fromUtf8("la_Footer"))
        self.gridLayout.addWidget(self.la_Footer, 1, 0, 1, 1)
        self.ln_Header = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ln_Header.setFont(font)
        self.ln_Header.setObjectName(_fromUtf8("ln_Header"))
        self.gridLayout.addWidget(self.ln_Header, 0, 1, 1, 1)
        self.bt_ReportX = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_ReportX.setFont(font)
        self.bt_ReportX.setObjectName(_fromUtf8("bt_ReportX"))
        self.gridLayout.addWidget(self.bt_ReportX, 7, 0, 1, 2)
        self.la_PaymentType = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.la_PaymentType.setFont(font)
        self.la_PaymentType.setObjectName(_fromUtf8("la_PaymentType"))
        self.gridLayout.addWidget(self.la_PaymentType, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.bt_ReportZ.setText(_translate("Form", "Report Z", None))
        self.bt_PrintFiscReceipt.setText(_translate("Form", "Print Fisc Receipt", None))
        self.la_Header.setText(_translate("Form", "Text Header:", None))
        self.bt_PrintNonFiscalReceipt.setText(_translate("Form", "Print Non Fiscal Receipt", None))
        self.la_Footer.setText(_translate("Form", "Text Footer:", None))
        self.bt_ReportX.setText(_translate("Form", "Report X", None))
        self.la_PaymentType.setText(_translate("Form", "Payment Type:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

