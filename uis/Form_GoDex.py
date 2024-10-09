# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Print sticket FP GoDex", pos = wx.DefaultPosition, size = wx.Size( 540,514 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 540,380 ), wx.Size( -1,-1 ) )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.SetBackgroundColour( wx.Colour( 233, 254, 169 ) )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.st_format_sticker = wx.StaticText( self, wx.ID_ANY, u"Format Eticheta:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_format_sticker.Wrap( -1 )

		self.st_format_sticker.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.st_format_sticker.SetMinSize( wx.Size( 150,-1 ) )

		gbSizer1.Add( self.st_format_sticker, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cb_format_stickerChoices = []
		self.cb_format_sticker = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cb_format_stickerChoices, 0 )
		self.cb_format_sticker.SetSelection( 0 )
		gbSizer1.Add( self.cb_format_sticker, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer1.Add( self.m_staticline1, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND |wx.ALL, 5 )

		self.st_nume_prod = wx.StaticText( self, wx.ID_ANY, u"Nume produs:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_nume_prod.Wrap( -1 )

		self.st_nume_prod.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer1.Add( self.st_nume_prod, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_BOTTOM|wx.TOP|wx.LEFT, 5 )

		self.et_nume_produs = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.et_nume_produs, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND|wx.LEFT, 5 )

		self.st_pret = wx.StaticText( self, wx.ID_ANY, u"Pret:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_pret.Wrap( -1 )

		self.st_pret.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer1.Add( self.st_pret, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.et_pret = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.et_pret, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.et_masa = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.et_masa, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.LEFT, 5 )

		self.st_total = wx.StaticText( self, wx.ID_ANY, u"Total:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_total.Wrap( -1 )

		self.st_total.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer1.Add( self.st_total, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.et_total = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.et_total, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.st_masa = wx.StaticText( self, wx.ID_ANY, u"Masa:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_masa.Wrap( -1 )

		self.st_masa.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer1.Add( self.st_masa, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.st_Barcod = wx.StaticText( self, wx.ID_ANY, u"Barcod:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_Barcod.Wrap( -1 )

		self.st_Barcod.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer1.Add( self.st_Barcod, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.et_barcod = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.et_barcod, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.st_ingrediente = wx.StaticText( self, wx.ID_ANY, u"Ingrediente:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_ingrediente.Wrap( -1 )

		self.st_ingrediente.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer1.Add( self.st_ingrediente, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 2 ), wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		self.rt_ingrediente = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,150 ), 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		gbSizer1.Add( self.rt_ingrediente, wx.GBPosition( 10, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer1.Add( self.m_staticline2, wx.GBPosition( 11, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND |wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.bt_preview = wx.Button( self, wx.ID_ANY, u"Preview", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_NONE )
		self.bt_preview.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.bt_preview.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer2.Add( self.bt_preview, 0, wx.ALL, 5 )

		self.bt_print = wx.Button( self, wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_NONE )
		self.bt_print.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.bt_print.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer2.Add( self.bt_print, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		gbSizer1.Add( bSizer2, wx.GBPosition( 12, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( gbSizer1, 1, wx.EXPAND|wx.LEFT, 8 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer1.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 10 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.st_date_connect_FP = wx.StaticText( self, wx.ID_ANY, u"Date connectare Printer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_date_connect_FP.Wrap( -1 )

		self.st_date_connect_FP.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer2.Add( self.st_date_connect_FP, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.st_ip = wx.StaticText( self, wx.ID_ANY, u"IP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_ip.Wrap( -1 )

		gbSizer2.Add( self.st_ip, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.et_ip = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.et_ip, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.st_port = wx.StaticText( self, wx.ID_ANY, u"Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_port.Wrap( -1 )

		self.st_port.SetMinSize( wx.Size( 70,-1 ) )

		gbSizer2.Add( self.st_port, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.et_port = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.et_port, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer2.Add( self.m_staticline3, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND |wx.ALL, 5 )

		self.rt_result = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.rt_result.SetMinSize( wx.Size( 200,340 ) )

		gbSizer2.Add( self.rt_result, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( gbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.bt_preview.Bind( wx.EVT_BUTTON, self.onclick_bt_preview )
		self.bt_print.Bind( wx.EVT_BUTTON, self.onclick_bt_print )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def onclick_bt_preview( self, event ):
		event.Skip()

	def onclick_bt_print( self, event ):
		event.Skip()


