#!python
# -*- coding: UTF-8 -*-

'''
/*
 * @Author: jeay 
 * @Date: 2018-05-28 15:00:31 
 * @Last Modified by: jeay
 * @Last Modified time: 2018-05-29 17:07:36
 */
'''

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ConvFrame
###########################################################################

class ConvFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"文件编码批量转换", pos = wx.DefaultPosition, size = wx.Size( 407,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		TopFrameGbSizer = wx.GridBagSizer( 0, 0 )
		TopFrameGbSizer.SetFlexibleDirection( wx.BOTH )
		TopFrameGbSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		TopFrameGbSizer.SetMinSize( wx.Size( 407,480 ) ) 
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText1 = wx.StaticText( self, wx.ID_ANY, u"请选择目录：", wx.Point( -1,-1 ), wx.Size( -1,28 ), 0 )
		self.staticText1.Wrap( -1 )
		self.staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		self.dirPicker = wx.DirPickerCtrl( self, wx.ID_ANY, u"GET_VALUE", u"请选择目录", wx.DefaultPosition, wx.Size( 280,28 ), wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		gbSizer1.Add( self.dirPicker, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.staticText2 = wx.StaticText( self, wx.ID_ANY, u"目标编码：", wx.DefaultPosition, wx.Size( -1,28 ), 0 )
		self.staticText2.Wrap( -1 )
		gbSizer1.Add( self.staticText2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )
		
		m_choiceChoices = [ u"UTF8", u"GB2312", u"GBK", u"GB18030" ]
		self.m_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 280,28 ), m_choiceChoices, 0 )
		self.m_choice.SetSelection( 0 )
		gbSizer1.Add( self.m_choice, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		TopFrameGbSizer.Add( gbSizer1, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText3 = wx.StaticText( self, wx.ID_ANY, u"文件后缀名：", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.staticText3.Wrap( -1 )
		gbSizer2.Add( self.staticText3, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALIGN_RIGHT, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u".txt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetValue(True) 
		gbSizer2.Add( self.m_checkBox1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u".php", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetValue(True) 
		gbSizer2.Add( self.m_checkBox2, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u".html", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.SetValue(True) 
		gbSizer2.Add( self.m_checkBox3, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, u".htm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox4.SetValue(True) 
		gbSizer2.Add( self.m_checkBox4, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_checkBox5 = wx.CheckBox( self, wx.ID_ANY, u".css", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox5.SetValue(True) 
		gbSizer2.Add( self.m_checkBox5, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_checkBox6 = wx.CheckBox( self, wx.ID_ANY, u".js", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox6.SetValue(True) 
		gbSizer2.Add( self.m_checkBox6, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_checkBox7 = wx.CheckBox( self, wx.ID_ANY, u".sass", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox7.SetValue(True) 
		gbSizer2.Add( self.m_checkBox7, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_checkBox8 = wx.CheckBox( self, wx.ID_ANY, u".scss", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_checkBox8, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_checkBox9 = wx.CheckBox( self, wx.ID_ANY, u".vue", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_checkBox9, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_checkBox10 = wx.CheckBox( self, wx.ID_ANY, u".jsx", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_checkBox10, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button = wx.Button( self, wx.ID_ANY, u"开始处理", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		
		TopFrameGbSizer.Add( gbSizer2, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.EXPAND, 5 )
		
		self.m_staticline = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_HORIZONTAL )
		TopFrameGbSizer.Add( self.m_staticline, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 3 ), wx.EXPAND |wx.ALL, 5 )
		
		gbSizerLog = wx.GridBagSizer( 0, 0 )
		gbSizerLog.SetFlexibleDirection( wx.BOTH )
		gbSizerLog.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticTextLog = wx.StaticText( self, wx.ID_ANY, u"输出日志：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticTextLog.Wrap( -1 )
		gbSizerLog.Add( self.staticTextLog, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		listBoxLogChoices = [ ]
		self.listBoxLog = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 353,180 ), listBoxLogChoices, 0 )
		gbSizerLog.Add( self.listBoxLog, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		
		TopFrameGbSizer.Add( gbSizerLog, wx.GBPosition( 4, 2 ), wx.GBSpan( 3, 1 ), wx.EXPAND, 5 )
		
		
		self.SetSizer( TopFrameGbSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.OnChangeCheckBox )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.OnChangeCheckBox )
		self.m_checkBox3.Bind( wx.EVT_CHECKBOX, self.OnChangeCheckBox )
		self.m_checkBox4.Bind( wx.EVT_CHECKBOX, self.OnChangeCheckBox )
		self.m_checkBox5.Bind( wx.EVT_CHECKBOX, self.OnChangeCheckBox )
		self.m_checkBox6.Bind( wx.EVT_CHECKBOX, self.OnChangeCheckBox )
		self.m_checkBox7.Bind( wx.EVT_CHECKBOX, self.OnChangeCheckBox )
		self.m_checkBox8.Bind( wx.EVT_CHECKBOX, self.OnChangeCheckBox )
		self.m_checkBox9.Bind( wx.EVT_CHECKBOX, self.OnChangeCheckBox )
		self.m_checkBox10.Bind( wx.EVT_CHECKBOX, self.OnChangeCheckBox )
		self.m_button.Bind( wx.EVT_BUTTON, self.StartConvert )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnChangeCheckBox( self, event ):
		event.Skip()
	
	def StartConvert( self, event ):
		event.Skip()
