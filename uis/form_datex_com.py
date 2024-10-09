# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis\form_datex_com.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(738, 666)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bt_openConnection = QtGui.QPushButton(self.centralwidget)
        self.bt_openConnection.setGeometry(QtCore.QRect(10, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_openConnection.setFont(font)
        self.bt_openConnection.setObjectName(_fromUtf8("bt_openConnection"))
        self.ln_comPort = QtGui.QLineEdit(self.centralwidget)
        self.ln_comPort.setGeometry(QtCore.QRect(10, 40, 151, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ln_comPort.setFont(font)
        self.ln_comPort.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_comPort.setObjectName(_fromUtf8("ln_comPort"))
        self.bt_closeConnection = QtGui.QPushButton(self.centralwidget)
        self.bt_closeConnection.setGeometry(QtCore.QRect(10, 100, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_closeConnection.setFont(font)
        self.bt_closeConnection.setObjectName(_fromUtf8("bt_closeConnection"))
        self.te_result = QtGui.QTextEdit(self.centralwidget)
        self.te_result.setGeometry(QtCore.QRect(180, 310, 541, 311))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.te_result.setFont(font)
        self.te_result.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.te_result.setReadOnly(True)
        self.te_result.setObjectName(_fromUtf8("te_result"))
        self.bt_sendCode = QtGui.QPushButton(self.centralwidget)
        self.bt_sendCode.setEnabled(True)
        self.bt_sendCode.setGeometry(QtCore.QRect(180, 230, 132, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_sendCode.setFont(font)
        self.bt_sendCode.setCheckable(False)
        self.bt_sendCode.setObjectName(_fromUtf8("bt_sendCode"))
        self.l_comPortNR = QtGui.QLabel(self.centralwidget)
        self.l_comPortNR.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l_comPortNR.setFont(font)
        self.l_comPortNR.setAlignment(QtCore.Qt.AlignCenter)
        self.l_comPortNR.setObjectName(_fromUtf8("l_comPortNR"))
        self.l_result = QtGui.QLabel(self.centralwidget)
        self.l_result.setGeometry(QtCore.QRect(180, 280, 541, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l_result.setFont(font)
        self.l_result.setAlignment(QtCore.Qt.AlignCenter)
        self.l_result.setObjectName(_fromUtf8("l_result"))
        self.te_send = QtGui.QTextEdit(self.centralwidget)
        self.te_send.setEnabled(True)
        self.te_send.setGeometry(QtCore.QRect(180, 10, 541, 211))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.te_send.setFont(font)
        self.te_send.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.te_send.setReadOnly(False)
        self.te_send.setObjectName(_fromUtf8("te_send"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.bt_openConnection.setText(_translate("MainWindow", "Open Connection", None))
        self.bt_closeConnection.setText(_translate("MainWindow", "Close Connection", None))
        self.bt_sendCode.setText(_translate("MainWindow", "Send Code", None))
        self.l_comPortNR.setText(_translate("MainWindow", "Com Port NR", None))
        self.l_result.setText(_translate("MainWindow", "Result", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

