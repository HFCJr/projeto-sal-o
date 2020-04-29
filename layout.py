# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import util
import arq
import matplotlib.pyplot as plt

grupo=0
###########################################################################
## Class MAINframe
###########################################################################


class MIAN ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Salão Encaracolados", pos = wx.DefaultPosition, size = wx.Size( 500,106 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		lay1V = wx.BoxSizer( wx.VERTICAL )
		
		self.label1 = wx.StaticText( self, wx.ID_ANY, u"Oque deseja fazer ?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label1.Wrap( -1 )
		lay1V.Add( self.label1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		lay2H = wx.BoxSizer( wx.HORIZONTAL )
		
		lay3V = wx.BoxSizer( wx.VERTICAL )
		
		self.B1regis = wx.Button( self, wx.ID_ANY, u"Registrar Funcionário", wx.DefaultPosition, wx.DefaultSize, 0 )
		lay3V.Add( self.B1regis, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		lay2H.Add( lay3V, 1, wx.EXPAND, 5 )
		
		lay4V = wx.BoxSizer( wx.VERTICAL )
		
		self.B2 = wx.Button( self, wx.ID_ANY, u"Remover Funcionário", wx.DefaultPosition, wx.DefaultSize, 0 )
		lay4V.Add( self.B2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		lay2H.Add( lay4V, 1, wx.EXPAND, 5 )
		
		lay5V = wx.BoxSizer( wx.VERTICAL )
		
		self.B3 = wx.Button( self, wx.ID_ANY, u"Calcular Salários", wx.DefaultPosition, wx.DefaultSize, 0 )
		lay5V.Add( self.B3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		lay2H.Add( lay5V, 1, wx.EXPAND, 5 )
		
		
		lay1V.Add( lay2H, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		self.SetSizer( lay1V )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.B1regis.Bind( wx.EVT_BUTTON, self.funB1 )
		self.B2.Bind( wx.EVT_BUTTON, self.funB2 )
		self.B3.Bind( wx.EVT_BUTTON, self.funB3 )
			
	def __del__( self ):
		pass
	def funB1( self, event ):
		util.apresenta(regis)
		event.Skip()
	
	def funB2( self, event ):
		util.apresenta(ap)
		event.Skip()
	
	def funB3( self, event ):
		util.apresenta(pagar)
		wx.Abort()
	
		
	

###########################################################################
## Class Freme2
###########################################################################
class regisfun ( wx.Dialog ):
	

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Registrar Funcionário", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		lay9V = wx.BoxSizer( wx.VERTICAL )
		
		self.espaço = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.espaço.Wrap( -1 )
		lay9V.Add( self.espaço, 0, wx.ALL, 5 )
		
		lay10H = wx.BoxSizer( wx.HORIZONTAL )
		
		self.label3 = wx.StaticText( self, wx.ID_ANY, u"Primeiro Nome:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label3.Wrap( -1 )
		lay10H.Add( self.label3, 0, wx.ALL, 5 )
		
		self.caixtext1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lay10H.Add( self.caixtext1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		lay9V.Add( lay10H, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		lay11V = wx.BoxSizer( wx.VERTICAL )
		
		self.B5 = wx.Button( self, wx.ID_ANY, u"Registrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		lay11V.Add( self.B5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		lay9V.Add( lay11V, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( lay9V )
		self.Layout()
		lay9V.Fit( self )
		
		self.Centre( wx.BOTH )
		
		self.B5.Bind( wx.EVT_BUTTON, self.func_regis )	
	def __del__( self ):
		pass
	
	def func_regis( self, event ):
		if self.caixtext1.GetValue():
			NAME =self.caixtext1.GetValue()
		else : 
			NAME = "nada"
		arq.escarq("banco/funcionarios.txt",NAME.strip().lower())
		wx.Abort()

		
	
class Apagaregis ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Apagar Funcionário", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		lay9V = wx.BoxSizer( wx.VERTICAL )
		
		self.espaço = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.espaço.Wrap( -1 )
		lay9V.Add( self.espaço, 0, wx.ALL, 5 )
		
		lay10H = wx.BoxSizer( wx.HORIZONTAL )
		
		self.label3 = wx.StaticText( self, wx.ID_ANY, u"Primeiro Nome:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label3.Wrap( -1 )
		lay10H.Add( self.label3, 0, wx.ALL, 5 )
		
		self.caixtext2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		lay10H.Add( self.caixtext2, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		lay9V.Add( lay10H, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		lay11V = wx.BoxSizer( wx.VERTICAL )
		
		self.B5 = wx.Button( self, wx.ID_ANY, u"Excluir", wx.DefaultPosition, wx.DefaultSize, 0 )
		lay11V.Add( self.B5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		lay9V.Add( lay11V, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( lay9V )
		self.Layout()
		lay9V.Fit( self )
		
		self.Centre( wx.BOTH )
		
		self.B5.Bind( wx.EVT_BUTTON, self.func_ex )	
	def __del__( self ):
		pass
	def func_ex( self, event ):
		arq.excluirn("banco/funcionarios.txt",self.caixtext2.GetValue().strip().lower())
		wx.Abort()
	
class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lucros", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"conta àgua :     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer22.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, u"000,00", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_textCtrl8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer3.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"conta Luz :            ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer23.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, u"000,00", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.m_textCtrl9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer3.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"conta internet :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer24.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, u"000,00", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_textCtrl10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer3.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"gastos produtos :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		bSizer25.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, u"000,00", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_textCtrl11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer3.Add( bSizer25, 1, wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"gerar registro", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_button10, 1, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		
		gSizer3.Add( bSizer26, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
		self.m_button10.Bind( wx.EVT_BUTTON, self.fung )

	def __del__( self ):
		pass

	def fung( self, event ):
		agua =float(self.m_textCtrl8.GetValue().replace(",","."))
		luz =float(self.m_textCtrl9.GetValue().replace(",","."))
		internet =float(self.m_textCtrl10.GetValue().replace(",","."))
		produtos =float(self.m_textCtrl11.GetValue().replace(",","."))
		tot=agua+luz+internet+produtos

		vetfun=util.vetfunn(util.vet(arq.lerarq("salão.txt")))
		util.GrafBar("Dinheiro por funcionario para o salão",vetfun,"totalserv")
		util.GrafBar("quantidade de serviço por funcionario para o salão",vetfun,"quantserv")	
		arq.sala(vetfun,tot)

		wx.Abort()
		event.Skip()
		
class main(MIAN):
	"""docstring for main"""
	def __init__(self, parent):
		MIAN.__init__(self,parent)
	
class regis(regisfun):
	"""docstring for main"""
	def __init__(self, parent):
		regisfun.__init__(self,parent)

class ap(Apagaregis):
	"""docstring for main"""
	def __init__(self, parent):
		Apagaregis.__init__(self,parent)

class pagar(MyFrame2):
	"""docstring for pagar"""
	def __init__(self, parent):
		MyFrame2.__init__(self,parent)