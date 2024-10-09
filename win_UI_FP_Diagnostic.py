import logging
import sys
import os
from CONSTANT import *
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QMessageBox
from PySide2.QtCore import Qt
from uis.UI_FP_diagnostic import Ui_FPDiagnostic
from datetime import *
from FPrinter_Driver.FP_Datex import DATEX_Comm as Dt
from FPrinter_Driver.FP_Datex_v167 import DATEX_Comm as Dt_v167
from CONFIG_from_FP import *


class MainWindows(QMainWindow):
    def __init__(self):
        logg_main.info('INIT UI  Ui_FPDiagnostic')
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_FPDiagnostic()
        self.ui.setupUi(self)

        self.ui.cb_comport.addItems(['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'COM10'])
        self.ui.cb_boud_rate.addItems(['1200', '9600', '19200', '38400', '115200'])

        self.ui.gb_diagnostic.setEnabled(0)

        self.ui.bt_conn.clicked.connect(self.click_bt_conn)
        self.ui.bt_rep_z.clicked.connect(self.click_bt_rep_z)
        self.ui.bt_rep_x.clicked.connect(self.click_bt_rep_x)
        self.ui.bt_ram_reset.clicked.connect(self.click_bt_ram_reset)
        self.ui.bt_cancel_fc.clicked.connect(self.click_bt_cancel_fc)

        try:
            v_datecs_protocol = int(config.conf.get('OTHER', 'datecs_protocol'))
        except Exception:
            v_datecs_protocol = 1
        v_datecs_protocol_txt = {2: 'Wtdedit 1.6.6.1', 1: 'Wtdedit 1.6.7.0'}
        logg_main.info(f'Datecs protocol version: {v_datecs_protocol_txt[v_datecs_protocol]}')

        try:
            v_datecs_type_protocol_model = int(config.conf.get('OTHER', 'datecs_type_Protocol_Model'))
        except Exception:
            v_datecs_type_protocol_model = 0
        logg_main.info(f'datecs_type_Protocol_Model: {v_datecs_type_protocol_model}')

        if v_datecs_protocol == 1:
            self.datecs = Dt_v167()
            self.datecs.datecs_type_Protocol_Model = v_datecs_type_protocol_model
        else:
            self.datecs = Dt()

    def dialog_box(self, s):
        dlg = QMessageBox(self)
        # dlg.setIcon(QtWidgets.QMessageBox.Information)
        dlg.setWindowTitle("MessageBox")
        dlg.setText(s)
        dlg.exec_()

    def click_bt_conn(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        v_com_port = self.ui.cb_comport.currentText()
        v_boudrate = self.ui.cb_boud_rate.currentText()

        v_digits = ''
        for c in v_com_port:
            if c.isdigit():
                v_digits += c
        v_com_port = v_digits

        try:
            l_msg_3 = 'Fiscal Printer: ' + v_com_port + ' ' + v_boudrate
            logg_main.info(l_msg_3)
            err = self.datecs.open_port(int(v_com_port), int(v_boudrate))
            logg_main.info(self.datecs.msg_res)
            self.datecs.msg_res = ''
            if err == 0:
                self.ui.fp_activ.setText(f'FP: {v_com_port}/{v_boudrate}')
                self.ui.fp_activ.setStyleSheet("background-color: green; font-weight: bold;")
                self.ui.gb_diagnostic.setEnabled(1)
                self.ui.txb_result.setText(f'Conexiune cu succes, FP: {v_com_port}/{v_boudrate}')
                QApplication.restoreOverrideCursor()
            else:
                QApplication.restoreOverrideCursor()
                self.ui.fp_activ.setStyleSheet("background-color: red; font-weight: bold;")
                self.ui.fp_activ.setText(f'FP: {v_com_port}/{v_boudrate}')
                self.ui.txb_result.setText(f'Eroare conexiune FP \n{self.datecs.msg_res}')
                self.dialog_box(f'Eroare conexiune FP \n{self.datecs.msg_res}')
        except Exception as e_datecs:
            QApplication.restoreOverrideCursor()
            exc_type, exc_obj, exc_tb = sys.exc_info()
            f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            lmsg_e_datecs = '{exc_type}, {f_name}, {exc_tb} \n{e}' \
                .format(exc_type=exc_type, f_name=f_name, exc_tb=exc_tb.tb_lineno, e=e_datecs)
            logg_main.error(lmsg_e_datecs)
            self.ui.txb_result.setText(lmsg_e_datecs)
            self.dialog_box(logg_main)

    def click_bt_rep_z(self):
        self.ui.txb_result.setText('Button click_bt_rep_z clicked')
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.ui.txb_result.setText('')

        res = self.datecs.fiscal_receipt('69,0', 'server')
        send_msg = self.datecs.msg_res

        QApplication.restoreOverrideCursor()
        v_msg = f'Comanda 69,0 (Raport Z)\n{send_msg}'
        logg_main.info(v_msg)
        self.ui.txb_result.setText(v_msg)
        self.dialog_box(v_msg)

    def click_bt_rep_x(self):
        self.ui.txb_result.setText('Button click_bt_rep_x clicked')
        QApplication.setOverrideCursor(Qt.WaitCursor)

        res = self.datecs.fiscal_receipt('69,2', 'server')
        send_msg = self.datecs.msg_res

        QApplication.restoreOverrideCursor()
        v_msg = f'Comanda 69,2 (Raport X)\n{send_msg}'
        logg_main.info(v_msg)
        self.ui.txb_result.setText(v_msg)
        self.dialog_box(v_msg)

    def click_bt_ram_reset(self):
        self.ui.txb_result.setText('Button click_bt_ram_reset clicked')

        QApplication.setOverrideCursor(Qt.WaitCursor)

        # res = self.datecs.fiscal_receipt('48,1,0000,1\n49,Test RAM RESET\\tA0*1\n53,\\tN0\n56', 'server')
        res = self.datecs.fiscal_receipt('48,1,0000,1', 'server')
        send_msg = self.datecs.msg_res

        # self.click_bt_conn()
        self.datecs.fiscal_receipt('60', 'server')

        if send_msg.find('-111024') > 0:
            QApplication.restoreOverrideCursor()
            v_msg = f'Raportul Z nu a fost tiparit de mai mult de 24 ore, Timaprit raportul Z\n{send_msg}'
            logg_main.info(v_msg)
            self.ui.txb_result.setText(v_msg)
            self.dialog_box(v_msg)
        else:
            QApplication.restoreOverrideCursor()
            v_msg = f'Comanda Chec RamReset (Verificarea daca sa Raport Z nu sa tapat mai mult de 24 ore)\n{send_msg}'
            logg_main.info(v_msg)
            self.ui.txb_result.setText(send_msg)
            self.dialog_box(send_msg)

    def click_bt_cancel_fc(self):
        self.ui.txb_result.setText('Button click_bt_cancel_fc clicked ')
        QApplication.setOverrideCursor(Qt.WaitCursor)

        res = self.datecs.fiscal_receipt('60', 'server')
        send_msg = self.datecs.msg_res

        QApplication.restoreOverrideCursor()
        v_msg = f'Comanda 60 (Anulare Check Fiscal)\n{send_msg}'
        logg_main.info(v_msg)
        self.ui.txb_result.setText(v_msg)
        self.dialog_box(v_msg)


current_path = os.path.dirname(os.path.abspath(__file__))
date_now = datetime.now().strftime("%Y%m%d")

# setarea afisarii logurilor 'logging'
try:
    os.makedirs(LOG_CONST.LOGSavePath)
except Exception as ex:
    pass

logging_level = 'DEBUG'

logFormatter = logging.Formatter("%(asctime)s [%(name)-27.27s] [%(levelname)-8.8s] "
                                 "F:[%(lineno)d: %(funcName)-20.20s] %(message)s",
                                 '%m-%d-%y %H:%M:%S')
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler(LOG_CONST.LOGSavePath + date_now + '_UI_FP_Diagnostic.log')
fileHandler.setFormatter(logFormatter)
fileHandler.setLevel(logging_level)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
rootLogger.setLevel(logging_level)

logging.getLogger('urllib3').setLevel('CRITICAL')
logging.getLogger('future_stdlib').setLevel('CRITICAL')
logging.getLogger('PIL').setLevel('CRITICAL')

logg_main = rootLogger
# ========================================================

if __name__ == '__main__':
    logg_main.info('START APP')
    app = QtWidgets.QApplication([])
    window = MainWindows()
    window.show()
    app.exec_()
