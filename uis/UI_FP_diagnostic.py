# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_FP_diagnostic.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FPDiagnostic(object):
    def setupUi(self, FPDiagnostic):
        if not FPDiagnostic.objectName():
            FPDiagnostic.setObjectName(u"FPDiagnostic")
        FPDiagnostic.resize(445, 630)
        FPDiagnostic.setMinimumSize(QSize(445, 630))
        FPDiagnostic.setMaximumSize(QSize(445, 963))
        icon = QIcon()
        icon.addFile(u"ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        FPDiagnostic.setWindowIcon(icon)
        self.centralwidget = QWidget(FPDiagnostic)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gb_conn = QGroupBox(self.centralwidget)
        self.gb_conn.setObjectName(u"gb_conn")
        palette = QPalette()
        brush = QBrush(QColor(170, 255, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush)
        self.gb_conn.setPalette(palette)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_conn.setFont(font)
        self.gb_conn.setStyleSheet(u"")
        self.formLayout = QFormLayout(self.gb_conn)
        self.formLayout.setObjectName(u"formLayout")
        self.lb_boudrate = QLabel(self.gb_conn)
        self.lb_boudrate.setObjectName(u"lb_boudrate")
        font1 = QFont()
        font1.setPointSize(10)
        self.lb_boudrate.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_boudrate)

        self.lb_comport = QLabel(self.gb_conn)
        self.lb_comport.setObjectName(u"lb_comport")
        self.lb_comport.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lb_comport)

        self.cb_boud_rate = QComboBox(self.gb_conn)
        self.cb_boud_rate.setObjectName(u"cb_boud_rate")
        self.cb_boud_rate.setMinimumSize(QSize(200, 30))
        self.cb_boud_rate.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cb_boud_rate)

        self.cb_comport = QComboBox(self.gb_conn)
        self.cb_comport.setObjectName(u"cb_comport")
        self.cb_comport.setMinimumSize(QSize(200, 30))
        self.cb_comport.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cb_comport)

        self.bt_conn = QPushButton(self.gb_conn)
        self.bt_conn.setObjectName(u"bt_conn")
        self.bt_conn.setMinimumSize(QSize(200, 30))
        self.bt_conn.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.bt_conn)

        self.fp_activ = QLabel(self.gb_conn)
        self.fp_activ.setObjectName(u"fp_activ")
        self.fp_activ.setMinimumSize(QSize(200, 30))
        self.fp_activ.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        self.fp_activ.setFont(font2)
        self.fp_activ.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.fp_activ)


        self.verticalLayout.addWidget(self.gb_conn)

        self.gb_diagnostic = QGroupBox(self.centralwidget)
        self.gb_diagnostic.setObjectName(u"gb_diagnostic")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush)
        self.gb_diagnostic.setPalette(palette1)
        self.gb_diagnostic.setFont(font)
        self.gb_diagnostic.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout = QGridLayout(self.gb_diagnostic)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bt_rep_z = QPushButton(self.gb_diagnostic)
        self.bt_rep_z.setObjectName(u"bt_rep_z")
        self.bt_rep_z.setMinimumSize(QSize(0, 35))
        self.bt_rep_z.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.bt_rep_z, 0, 0, 1, 1)

        self.bt_rep_x = QPushButton(self.gb_diagnostic)
        self.bt_rep_x.setObjectName(u"bt_rep_x")
        self.bt_rep_x.setMinimumSize(QSize(0, 35))
        self.bt_rep_x.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.bt_rep_x, 0, 1, 1, 1)

        self.bt_ram_reset = QPushButton(self.gb_diagnostic)
        self.bt_ram_reset.setObjectName(u"bt_ram_reset")
        self.bt_ram_reset.setMinimumSize(QSize(0, 35))
        self.bt_ram_reset.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.bt_ram_reset, 1, 1, 1, 1)

        self.bt_cancel_fc = QPushButton(self.gb_diagnostic)
        self.bt_cancel_fc.setObjectName(u"bt_cancel_fc")
        self.bt_cancel_fc.setMinimumSize(QSize(0, 35))
        self.bt_cancel_fc.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.bt_cancel_fc, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 2)


        self.verticalLayout.addWidget(self.gb_diagnostic)

        self.txb_result = QTextBrowser(self.centralwidget)
        self.txb_result.setObjectName(u"txb_result")
        self.txb_result.setEnabled(False)
        self.txb_result.setMinimumSize(QSize(0, 650))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.txb_result.setFont(font3)

        self.verticalLayout.addWidget(self.txb_result)

        FPDiagnostic.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FPDiagnostic)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 445, 21))
        FPDiagnostic.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FPDiagnostic)
        self.statusbar.setObjectName(u"statusbar")
        FPDiagnostic.setStatusBar(self.statusbar)

        self.retranslateUi(FPDiagnostic)

        QMetaObject.connectSlotsByName(FPDiagnostic)
    # setupUi

    def retranslateUi(self, FPDiagnostic):
        FPDiagnostic.setWindowTitle(QCoreApplication.translate("FPDiagnostic", u"FP Diagnostic", None))
        self.gb_conn.setTitle(QCoreApplication.translate("FPDiagnostic", u"Connect FP", None))
        self.lb_boudrate.setText(QCoreApplication.translate("FPDiagnostic", u"BoudRate:", None))
        self.lb_comport.setText(QCoreApplication.translate("FPDiagnostic", u"Com Port:", None))
        self.bt_conn.setText(QCoreApplication.translate("FPDiagnostic", u"Connect", None))
        self.fp_activ.setText(QCoreApplication.translate("FPDiagnostic", u"FP:", None))
        self.gb_diagnostic.setTitle(QCoreApplication.translate("FPDiagnostic", u"DIAGNOSTIC", None))
        self.bt_rep_z.setText(QCoreApplication.translate("FPDiagnostic", u"Raport Z", None))
        self.bt_rep_x.setText(QCoreApplication.translate("FPDiagnostic", u"Raport X", None))
        self.bt_ram_reset.setText(QCoreApplication.translate("FPDiagnostic", u"Check RAM RESET", None))
        self.bt_cancel_fc.setText(QCoreApplication.translate("FPDiagnostic", u"Cancel FCheck", None))
        self.txb_result.setPlaceholderText(QCoreApplication.translate("FPDiagnostic", u"RESULT", None))
    # retranslateUi

