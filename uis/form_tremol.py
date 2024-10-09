# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis\form_tremol.ui'
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

class Ui_Tremol(object):
    def setupUi(self, Tremol):
        Tremol.setObjectName(_fromUtf8("Tremol"))
        Tremol.resize(681, 651)
        Tremol.setMinimumSize(QtCore.QSize(681, 651))
        Tremol.setMaximumSize(QtCore.QSize(681, 651))
        Tremol.setBaseSize(QtCore.QSize(0, 0))
        self.ln_commport = QtGui.QLineEdit(Tremol)
        self.ln_commport.setGeometry(QtCore.QRect(12, 14, 128, 39))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ln_commport.setFont(font)
        self.ln_commport.setStyleSheet(_fromUtf8("padding: 10px;"))
        self.ln_commport.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_commport.setObjectName(_fromUtf8("ln_commport"))
        self.ln_boud = QtGui.QLineEdit(Tremol)
        self.ln_boud.setGeometry(QtCore.QRect(155, 14, 128, 39))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ln_boud.setFont(font)
        self.ln_boud.setStyleSheet(_fromUtf8("padding: 10px;"))
        self.ln_boud.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_boud.setObjectName(_fromUtf8("ln_boud"))
        self.bt_findConnection = QtGui.QPushButton(Tremol)
        self.bt_findConnection.setEnabled(True)
        self.bt_findConnection.setGeometry(QtCore.QRect(298, 10, 187, 48))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_findConnection.sizePolicy().hasHeightForWidth())
        self.bt_findConnection.setSizePolicy(sizePolicy)
        self.bt_findConnection.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bt_findConnection.setFont(font)
        self.bt_findConnection.setStyleSheet(_fromUtf8("padding: 10px;"))
        self.bt_findConnection.setObjectName(_fromUtf8("bt_findConnection"))
        self.bt_OpenCommport = QtGui.QPushButton(Tremol)
        self.bt_OpenCommport.setGeometry(QtCore.QRect(500, 10, 176, 48))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bt_OpenCommport.setFont(font)
        self.bt_OpenCommport.setStyleSheet(_fromUtf8("padding: 10px;"))
        self.bt_OpenCommport.setObjectName(_fromUtf8("bt_OpenCommport"))
        self.t_code = QtGui.QTextEdit(Tremol)
        self.t_code.setGeometry(QtCore.QRect(10, 70, 661, 192))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t_code.setFont(font)
        self.t_code.setObjectName(_fromUtf8("t_code"))
        self.t_result = QtGui.QTextEdit(Tremol)
        self.t_result.setEnabled(True)
        self.t_result.setGeometry(QtCore.QRect(10, 331, 661, 311))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t_result.setFont(font)
        self.t_result.setObjectName(_fromUtf8("t_result"))
        self.bt_sendCode = QtGui.QPushButton(Tremol)
        self.bt_sendCode.setGeometry(QtCore.QRect(290, 280, 111, 38))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bt_sendCode.setFont(font)
        self.bt_sendCode.setStyleSheet(_fromUtf8("padding: 5px;"))
        self.bt_sendCode.setObjectName(_fromUtf8("bt_sendCode"))

        self.retranslateUi(Tremol)
        QtCore.QObject.connect(self.bt_sendCode, QtCore.SIGNAL(_fromUtf8("pressed()")), self.t_result.clear)
        QtCore.QMetaObject.connectSlotsByName(Tremol)

    def retranslateUi(self, Tremol):
        Tremol.setWindowTitle(_translate("Tremol", "Tremol", None))
        self.bt_findConnection.setText(_translate("Tremol", "Find Commport", None))
        self.bt_OpenCommport.setText(_translate("Tremol", "Open Comport", None))
        self.bt_sendCode.setText(_translate("Tremol", "SEND", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Tremol = QtGui.QWidget()
    ui = Ui_Tremol()
    ui.setupUi(Tremol)
    Tremol.show()
    sys.exit(app.exec_())

