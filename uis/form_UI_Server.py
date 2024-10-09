# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class mainForm
###########################################################################

class mainForm ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"UI service Server_FP", pos = wx.DefaultPosition, size = wx.Size( 670,599 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 670,450 ), wx.Size( 670,-1 ) )

		s_main = wx.BoxSizer( wx.VERTICAL )

		self.nb_main = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.p_direct_code = wx.Panel( self.nb_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		s_dir = wx.GridBagSizer( 0, 0 )
		s_dir.SetFlexibleDirection( wx.BOTH )
		s_dir.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.st_dir_Text1 = wx.StaticText( self.p_direct_code, wx.ID_ANY, u"Model FP / COM PORT / Boudrate:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_dir_Text1.Wrap( -1 )

		s_dir.Add( self.st_dir_Text1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		cb_dir_model_fpChoices = []
		self.cb_dir_model_fp = wx.ComboBox( self.p_direct_code, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, cb_dir_model_fpChoices, 0 )
		s_dir.Add( self.cb_dir_model_fp, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		cb_dir_comportChoices = []
		self.cb_dir_comport = wx.ComboBox( self.p_direct_code, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, cb_dir_comportChoices, 0 )
		s_dir.Add( self.cb_dir_comport, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		cb_dir_boudrateChoices = []
		self.cb_dir_boudrate = wx.ComboBox( self.p_direct_code, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, cb_dir_boudrateChoices, 0 )
		s_dir.Add( self.cb_dir_boudrate, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.rt_dir_code = wx.richtext.RichTextCtrl( self.p_direct_code, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.rt_dir_code.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		s_dir.Add( self.rt_dir_code, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 4 ), wx.EXPAND |wx.ALL, 5 )

		self.rt_dir_result = wx.richtext.RichTextCtrl( self.p_direct_code, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.rt_dir_result.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		self.rt_dir_result.SetMinSize( wx.Size( -1,150 ) )

		s_dir.Add( self.rt_dir_result, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 4 ), wx.EXPAND|wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.bt_dir_print = wx.ToggleButton( self.p_direct_code, wx.ID_ANY, u"Printeaza", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bt_dir_print.SetValue( True )
		s_dir.Add( self.bt_dir_print, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		s_dir.AddGrowableCol( 0 )
		s_dir.AddGrowableRow( 1 )

		self.p_direct_code.SetSizer( s_dir )
		self.p_direct_code.Layout()
		s_dir.Fit( self.p_direct_code )
		self.nb_main.AddPage( self.p_direct_code, u"Direct", False )
		self.p_ui = wx.Panel( self.nb_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		s_ui = wx.GridBagSizer( 0, 0 )
		s_ui.SetFlexibleDirection( wx.BOTH )
		s_ui.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.bt_ui_report_x = wx.Button( self.p_ui, wx.ID_ANY, u"Raport X", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.bt_ui_report_x, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.bt_ui_report_z = wx.Button( self.p_ui, wx.ID_ANY, u"Raport Z", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.bt_ui_report_z, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.bt_ui_paper_cut = wx.Button( self.p_ui, wx.ID_ANY, u"Paper cut", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.bt_ui_paper_cut, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.bt_ui_paper_feed = wx.Button( self.p_ui, wx.ID_ANY, u"Paper feed", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.bt_ui_paper_feed, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.bt_ui_ft_status = wx.Button( self.p_ui, wx.ID_ANY, u"FP status", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.bt_ui_ft_status, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self.p_ui, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		s_ui.Add( self.m_staticline1, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 3 ), wx.EXPAND |wx.ALL, 5 )

		self.lb_ui_add_nonf_bon = wx.TextCtrl( self.p_ui, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.lb_ui_add_nonf_bon, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		self.bt_ui_add_nobf_bon = wx.Button( self.p_ui, wx.ID_ANY, u"Add line", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.bt_ui_add_nobf_bon, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.bt_ui_print_nonf_bon = wx.Button( self.p_ui, wx.ID_ANY, u"Print non fiscal Bon", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.bt_ui_print_nonf_bon, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self.p_ui, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		s_ui.Add( self.m_staticline2, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 3 ), wx.EXPAND |wx.ALL, 5 )

		self.bt_ui_cash_out = wx.Button( self.p_ui, wx.ID_ANY, u"Cash Out", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.bt_ui_cash_out, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self.p_ui, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticline3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_staticline3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		s_ui.Add( self.m_staticline3, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

		self.st_fiscal_bon = wx.StaticText( self.p_ui, wx.ID_ANY, u"Bon Fiscal:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_fiscal_bon.Wrap( -1 )

		self.st_fiscal_bon.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )

		s_ui.Add( self.st_fiscal_bon, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.et_ui_cash_out = wx.TextCtrl( self.p_ui, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.et_ui_cash_out.SetMaxSize( wx.Size( 90,-1 ) )

		s_ui.Add( self.et_ui_cash_out, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		cb_ui_operatorChoices = []
		self.cb_ui_operator = wx.ComboBox( self.p_ui, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, cb_ui_operatorChoices, 0 )
		self.cb_ui_operator.SetMaxSize( wx.Size( 90,-1 ) )

		s_ui.Add( self.cb_ui_operator, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.te_ui_pass_op = wx.TextCtrl( self.p_ui, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.te_ui_pass_op.SetMaxSize( wx.Size( 90,-1 ) )

		s_ui.Add( self.te_ui_pass_op, wx.GBPosition( 9, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.bt_ui_add_oper = wx.Button( self.p_ui, wx.ID_ANY, u"Add Operator", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.bt_ui_add_oper, wx.GBPosition( 9, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.te_ui_name_prod = wx.TextCtrl( self.p_ui, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.te_ui_name_prod, wx.GBPosition( 10, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

		cb_ui_tvaChoices = []
		self.cb_ui_tva = wx.ComboBox( self.p_ui, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, cb_ui_tvaChoices, 0 )
		self.cb_ui_tva.SetMaxSize( wx.Size( 90,-1 ) )

		s_ui.Add( self.cb_ui_tva, wx.GBPosition( 10, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.te_ui_price = wx.TextCtrl( self.p_ui, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.te_ui_price.SetMaxSize( wx.Size( 90,-1 ) )

		s_ui.Add( self.te_ui_price, wx.GBPosition( 11, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.te_ui_cnt_prod = wx.TextCtrl( self.p_ui, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.te_ui_cnt_prod.SetMaxSize( wx.Size( 90,-1 ) )

		s_ui.Add( self.te_ui_cnt_prod, wx.GBPosition( 11, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.bt_ui_add_prod = wx.Button( self.p_ui, wx.ID_ANY, u"Add Product", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.bt_ui_add_prod, wx.GBPosition( 11, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.bt_ui_print_fiscal_bon = wx.Button( self.p_ui, wx.ID_ANY, u"Print fiscal Bon", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_ui.Add( self.bt_ui_print_fiscal_bon, wx.GBPosition( 12, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.rt_ui_code = wx.richtext.RichTextCtrl( self.p_ui, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.rt_ui_code.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer3.Add( self.rt_ui_code, 1, wx.EXPAND |wx.ALL, 5 )

		self.rt_ui_result = wx.richtext.RichTextCtrl( self.p_ui, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.rt_ui_result.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		self.rt_ui_result.SetMinSize( wx.Size( -1,150 ) )
		self.rt_ui_result.SetMaxSize( wx.Size( -1,150 ) )

		bSizer3.Add( self.rt_ui_result, 1, wx.EXPAND |wx.ALL, 5 )


		s_ui.Add( bSizer3, wx.GBPosition( 1, 3 ), wx.GBSpan( 13, 2 ), wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.st_ui_text1 = wx.StaticText( self.p_ui, wx.ID_ANY, u"Model FP / COM PORT / Boudrate:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_ui_text1.Wrap( -1 )

		self.st_ui_text1.SetMinSize( wx.Size( 280,-1 ) )

		bSizer2.Add( self.st_ui_text1, 0, wx.ALL|wx.EXPAND, 5 )

		cb_ui_model_fpChoices = []
		self.cb_ui_model_fp = wx.ComboBox( self.p_ui, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, cb_ui_model_fpChoices, 0 )
		bSizer2.Add( self.cb_ui_model_fp, 0, wx.ALL, 5 )

		cb_ui_comportChoices = []
		self.cb_ui_comport = wx.ComboBox( self.p_ui, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, cb_ui_comportChoices, 0 )
		bSizer2.Add( self.cb_ui_comport, 0, wx.ALL, 5 )

		cb_ui_boudrateChoices = []
		self.cb_ui_boudrate = wx.ComboBox( self.p_ui, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, cb_ui_boudrateChoices, 0 )
		bSizer2.Add( self.cb_ui_boudrate, 0, wx.ALL, 5 )


		s_ui.Add( bSizer2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 5 ), wx.EXPAND, 5 )


		s_ui.AddGrowableCol( 3 )
		s_ui.AddGrowableCol( 4 )
		s_ui.AddGrowableRow( 13 )

		self.p_ui.SetSizer( s_ui )
		self.p_ui.Layout()
		s_ui.Fit( self.p_ui )
		self.nb_main.AddPage( self.p_ui, u"UI", True )

		s_main.Add( self.nb_main, 1, wx.EXPAND, 5 )


		self.SetSizer( s_main )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.cb_dir_model_fp.Bind( wx.EVT_COMBOBOX, self.onclick_cb_dir_model_fp )
		self.cb_dir_comport.Bind( wx.EVT_COMBOBOX, self.onclick_cb_dir_comport )
		self.cb_dir_boudrate.Bind( wx.EVT_COMBOBOX, self.onclick_cb_dir_boudrate )
		self.bt_dir_print.Bind( wx.EVT_TOGGLEBUTTON, self.onclick_bt_dir_print )
		self.bt_ui_report_x.Bind( wx.EVT_BUTTON, self.onclick_bt_ui_report_x )
		self.bt_ui_report_z.Bind( wx.EVT_BUTTON, self.onclick_bt_ui_report_z )
		self.bt_ui_paper_cut.Bind( wx.EVT_BUTTON, self.onclick_bt_ui_paper_cut )
		self.bt_ui_paper_feed.Bind( wx.EVT_BUTTON, self.onclick_bt_ui_paper_feed )
		self.bt_ui_ft_status.Bind( wx.EVT_BUTTON, self.onclick_bt_ui_ft_status )
		self.bt_ui_add_nobf_bon.Bind( wx.EVT_BUTTON, self.onclick_bt_ui_add_nobf_bon )
		self.bt_ui_print_nonf_bon.Bind( wx.EVT_BUTTON, self.onclick_bt_ui_print_nonf_bon )
		self.bt_ui_cash_out.Bind( wx.EVT_BUTTON, self.onclick_bt_ui_cash_out )
		self.et_ui_cash_out.Bind( wx.EVT_CHAR, self.block_non_numbers )
		self.bt_ui_add_oper.Bind( wx.EVT_BUTTON, self.onclick_bt_ui_add_oper )
		self.te_ui_price.Bind( wx.EVT_CHAR, self.block_non_numbers )
		self.te_ui_cnt_prod.Bind( wx.EVT_CHAR, self.block_non_numbers )
		self.bt_ui_add_prod.Bind( wx.EVT_BUTTON, self.onclick_bt_ui_add_prod )
		self.bt_ui_print_fiscal_bon.Bind( wx.EVT_BUTTON, self.onclick_bt_ui_print_fiscal_bon )
		self.cb_ui_model_fp.Bind( wx.EVT_COMBOBOX, self.onclick_cb_ui_model_fp )
		self.cb_ui_comport.Bind( wx.EVT_COMBOBOX, self.onclick_cb_ui_comport )
		self.cb_ui_boudrate.Bind( wx.EVT_COMBOBOX, self.onclick_cb_ui_boudrate )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onclick_cb_dir_model_fp( self, event ):
		event.Skip()

	def onclick_cb_dir_comport( self, event ):
		event.Skip()

	def onclick_cb_dir_boudrate( self, event ):
		event.Skip()

	def onclick_bt_dir_print( self, event ):
		event.Skip()

	def onclick_bt_ui_report_x( self, event ):
		event.Skip()

	def onclick_bt_ui_report_z( self, event ):
		event.Skip()

	def onclick_bt_ui_paper_cut( self, event ):
		event.Skip()

	def onclick_bt_ui_paper_feed( self, event ):
		event.Skip()

	def onclick_bt_ui_ft_status( self, event ):
		event.Skip()

	def onclick_bt_ui_add_nobf_bon( self, event ):
		event.Skip()

	def onclick_bt_ui_print_nonf_bon( self, event ):
		event.Skip()

	def onclick_bt_ui_cash_out( self, event ):
		event.Skip()

	def block_non_numbers( self, event ):
		event.Skip()

	def onclick_bt_ui_add_oper( self, event ):
		event.Skip()

	def onclick_bt_ui_add_prod( self, event ):
		event.Skip()

	def onclick_bt_ui_print_fiscal_bon( self, event ):
		event.Skip()

	def onclick_cb_ui_model_fp( self, event ):
		event.Skip()

	def onclick_cb_ui_comport( self, event ):
		event.Skip()

	def onclick_cb_ui_boudrate( self, event ):
		event.Skip()


