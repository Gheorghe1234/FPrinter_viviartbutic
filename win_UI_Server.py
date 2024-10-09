# -*- coding: utf-8 -*-
# Created by Nicolae Gaidarji at 11.09.2020
from CONSTANT import *
from uis.form_UI_Server import *
from UNA_Support.config_util import CFG
from UNA_Support.getLog import Log
from UNA_Support.Utility import *
import socket
import os

class _mainFrame(mainForm):
    def __init__(self, arg):
        mainForm.__init__(self, arg)

        self.cb_dir_model_fp.AppendItems(['DATECS', 'TREMOL', 'HTTP', 'SHTRIH'])
        self.cb_dir_model_fp.SetSelection(0)
        self.cb_dir_comport.AppendItems(['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'COM10', 'COM11', 'COM12'])
        self.cb_dir_comport.SetSelection(0)
        self.cb_dir_boudrate.AppendItems(['1200', '9600', '19200', '38400', '115200'])
        self.cb_dir_boudrate.SetSelection(2)

        self.cb_ui_model_fp.AppendItems(['DATECS', 'TREMOL', 'HTTP'])
        self.cb_ui_model_fp.SetSelection(0)
        self.cb_ui_comport.AppendItems(['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'COM10', 'COM11', 'COM12'])
        self.cb_ui_comport.SetSelection(0)
        self.cb_ui_boudrate.AppendItems(['1200', '9600', '19200', '38400', '115200'])
        self.cb_ui_boudrate.SetSelection(2)

        self.cb_ui_operator.AppendItems(['Operator 1', 'Operator 2', 'Operator 3', 'Operator 4'])
        self.cb_ui_operator.SetSelection(0)

        self.cb_ui_tva.AppendItems(['A', 'B', 'C', 'D'])
        self.cb_ui_tva.SetSelection(0)
        self.te_ui_pass_op.SetValue('0000')
        self.te_ui_name_prod.SetValue('Nume produs')
        self.te_ui_price.SetValue('00.0')
        self.te_ui_cnt_prod.SetValue('1')

        self.write_dir_code()
        self.write_ui_result()
        self.fiscal_bon_enable(False)

    def write_dir_code(self, msg_code=None):
        self.rt_dir_code.Clear()
        msg_code = msg_code if msg_code != None else '''38
42, 8888888888888888888888888888888888888888
42, 1234567890123456789012345678901234567890
42, 8888888888888888888888888888888888888888
42, 1234567890123456789012345678901234567890
39'''
        boudrate = self.cb_dir_boudrate.GetValue()
        port = self.cb_dir_comport.GetValue()[3:]
        type_fp = self.cb_dir_model_fp.GetValue()
        self.rt_dir_code.WriteText('''/br{boudrate}/port{port}/t{type_fp}/c{msg_code}'''.format(boudrate=boudrate, port=port, type_fp=type_fp, msg_code=msg_code))

    def write_ui_result(self, msg_code=None):
        self.rt_ui_code.Clear()
        msg_code = msg_code if msg_code != None else rt_ui_default
        boudrate = self.cb_ui_boudrate.GetValue()
        port = self.cb_ui_comport.GetValue()[3:]
        type_fp = self.cb_ui_model_fp.GetValue()
        self.rt_ui_code.WriteText('''/br{boudrate}/port{port}/t{type_fp}/c{msg_code}'''.format(boudrate=boudrate, port=port, type_fp=type_fp, msg_code=msg_code))

    def cb_write_ui_rezult(self):
        msg = str(self.rt_ui_code.GetValue())
        msg = msg[msg.find('/c')+2:]
        self.write_ui_result(msg)

    def cb_write_dir_rezult(self):
        msg = str(self.rt_dir_code.GetValue())
        msg = msg[msg.find('/c') + 2:]
        self.write_dir_code(msg)

    def onclick_cb_dir_boudrate(self, event):
        self.cb_write_dir_rezult()

    def onclick_cb_dir_comport(self, event):
        self.cb_write_dir_rezult()

    def onclick_cb_dir_model_fp(self, event):
        self.cb_write_dir_rezult()
        model_fp =  self.cb_dir_model_fp.GetValue()
        if model_fp == 'HTTP':
            self.cb_dir_comport.Enable(False)
            self.cb_dir_boudrate.Enable(False)
            self.st_dir_Text1.SetLabel("Model FP:   ")
        else:
            self.cb_dir_comport.Enable(True)
            self.cb_dir_boudrate.Enable(True)
            self.st_dir_Text1.SetLabel("Model FP / COM PORT / Boudrate:")

    def onclick_cb_ui_model_fp( self, event ):
        self.cb_write_ui_rezult()
        model_fp = self.cb_ui_model_fp.GetValue()
        if model_fp == 'HTTP':
            self.cb_ui_comport.Enable(False)
            self.cb_ui_boudrate.Enable(False)
            self.st_ui_text1.SetLabel("Model FP")
        else:
            self.cb_ui_comport.Enable(True)
            self.cb_ui_boudrate.Enable(True)
            self.st_ui_text1.SetLabel("Model FP / COM PORT / Boudrate:")

    def onclick_cb_ui_comport( self, event ):
        self.cb_write_ui_rezult()

    def onclick_cb_ui_boudrate( self, event ):
        self.cb_write_ui_rezult()

    def send_msg_server(self, msg):
        wait = wx.BusyCursor()
        page = self.nb_main.GetSelection()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('127.0.0.1', 8880))
            sock.send(msg.encode())
            result = sock.recv(40960000)
        except socket.error as ex:
            del wait
            lmsg = 'Server Unavailable, {ex}'.format(ex=ex)
            wx.MessageBox(lmsg, LOG_CONST.Error, wx.OK | wx.ICON_ERROR)
        except Exception as ex:
            del wait
            wx.MessageBox(ex, LOG_CONST.Error, wx.OK | wx.ICON_ERROR)
        else:
            del wait
            self.rt_dir_result.Clear() if page == 0 else self.rt_ui_result.Clear()
            result = result[result.find('\n') + 1:]
            result = result.decode('cp1251', 'ignore')
            self.rt_dir_result.WriteText(result) if page == 0 else self.rt_ui_result.WriteText(result)

    def onclick_bt_dir_print( self, event ):
        msg = self.rt_dir_code.GetValue()
        self.send_msg_server(msg)

    def onclick_bt_ui_report_x( self, event ):
        self.write_ui_result('69,0')
        msg = self.rt_ui_code.GetValue()
        self.send_msg_server(msg)

    def onclick_bt_ui_report_z( self, event ):
        self.write_ui_result('69,2')
        msg = self.rt_ui_code.GetValue()
        self.send_msg_server(msg)

    def onclick_bt_ui_paper_cut( self, event ):
        self.write_ui_result('45')
        msg = self.rt_ui_code.GetValue()
        self.send_msg_server(msg)

    def onclick_bt_ui_paper_feed( self, event ):
        self.write_ui_result('44,3')
        msg = self.rt_ui_code.GetValue()
        self.send_msg_server(msg)

    def onclick_bt_ui_ft_status( self, event ):
        self.write_ui_result('71')
        msg = self.rt_ui_code.GetValue()
        self.send_msg_server(msg)

    def onclick_bt_ui_add_nobf_bon( self, event ):
        msg = str(self.rt_ui_code.GetValue())
        msg = msg.replace(rt_ui_default, '')
        msg = msg.replace('\n39', '')
        text = self.lb_ui_add_nonf_bon.GetValue()
        self.rt_ui_code.Clear()
        if str(msg).find('c38') == -1:
            text = '{msg}38\n42, {text}'.format(text=text, msg=msg)
        else:
            text = '{msg}\n42, {text}'.format(text=text,msg=msg)
        self.rt_ui_code.WriteText(text)
        msg = self.rt_ui_code.GetValue()
        self.send_msg_server(msg)

    def onclick_bt_ui_print_nonf_bon( self, event ):
        msg = str(self.rt_ui_code.GetValue())
        if msg.find('\n39') == -1:
            self.rt_ui_code.WriteText('\n39')
            msg = self.rt_ui_code.GetValue()
        else:
            msg = msg
        self.send_msg_server(msg)

    def block_non_numbers( self, event):
        key_code = event.GetKeyCode()

        # Allow ASCII numerics
        if ord('0') <= key_code <= ord('9'):
            event.Skip()
            return

        # Allow decimal points
        if key_code == ord('.'):
            event.Skip()
            return

        # Allow tabs and backspace
        if key_code == ord('\t') or key_code == 8:
            event.Skip()
            return

        # Block everything else
        return

    def onclick_bt_ui_cash_out( self, event):
        sum_cash_out = self.et_ui_cash_out.GetValue()
        if sum_cash_out == '':
            wx.MessageBox('Introduceti suma', LOG_CONST.Info, wx.OK | wx.ICON_INFORMATION)
        else:
            sum_cash_out = float(sum_cash_out)
            msg = '70,{cashout}'.format(cashout=sum_cash_out)
            self.write_ui_result(msg)
            msg = self.rt_ui_code.GetValue()
            self.send_msg_server(msg)

    def onclick_bt_ui_add_oper( self, event):
        msg = str(self.rt_ui_code.GetValue())
        msg = msg.replace(rt_ui_default, '')
        oper = self.cb_ui_operator.GetSelection() + 1
        pass_oper = self.te_ui_pass_op.GetValue()
        if msg.find('c48') == -1:
            self.rt_ui_code.Clear()
            text = '{msg}48,{oper},{pass_oper},1'.format(oper=oper, msg=msg, pass_oper=pass_oper)
            self.rt_ui_code.WriteText(text)
            self.fiscal_bon_enable(True)

    def onclick_bt_ui_add_prod( self, event):
        prod_name = str(self.te_ui_name_prod.GetValue())
        v_tva = str(self.cb_ui_tva.GetValue())
        price = self.te_ui_price.GetValue()
        prod_cnt = self.te_ui_cnt_prod.GetValue()
        prod_cnt = 1 if prod_cnt == '' else prod_cnt

        msg = str(self.rt_ui_code.GetValue())
        if prod_name == '' or price == '':
            wx.MessageBox('Completati toate cimpurile', LOG_CONST.Info, wx.OK | wx.ICON_INFORMATION)
        else:
            text = '\n49,{prod_name}\\t{v_tva}{price}*{prod_cnt}'\
                .format(prod_name=prod_name, msg=msg, v_tva=v_tva, price=price, prod_cnt=prod_cnt)
            self.rt_ui_code.WriteText(text)

    def fiscal_bon_enable(self, enabled):
        self.te_ui_name_prod.Enable(enabled)
        self.cb_ui_tva.Enable(enabled)
        self.te_ui_price.Enable(enabled)
        self.te_ui_cnt_prod.Enable(enabled)
        self.bt_ui_add_prod.Enable(enabled)
        self.bt_ui_print_fiscal_bon.Enable(enabled)

    def onclick_bt_ui_print_fiscal_bon( self, event):
        msg = str(self.rt_ui_code.GetValue())
        if msg.find('53,\\t') == -1:
            self.rt_ui_code.WriteText('\n53,\\tN\n56')
            msg = self.rt_ui_code.GetValue()
        else:
            msg = msg
        self.send_msg_server(msg)


def show_form():
    app = []
    Form_main = []

    app = wx.App()
    Form_main = _mainFrame(None)
    Form_main.Show()
    app.MainLoop()

    return 1

show_form()
