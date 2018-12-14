# gui.py
# Graphic User Interface 
#
# Luana Goncalves, Leonardo de Brito
# 02.jun.2017

import wx
import wx.xrc
import main_aqv

class MainFrame ( wx.Frame ):
	"""A graphical user interface for performance characterization of visual quality metrics
        """
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aplicativo de Avalia��o de Qualidade Visual", pos = wx.DefaultPosition, size = wx.Size( 500, 720), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Diret�rio de Imagens Originais", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.text = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer1.Add( self.text, 0, wx.ALL|wx.EXPAND, 5 )
		

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Diret�rio de Imagens de Teste", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer1.Add( self.text1, 0, wx.ALL|wx.EXPAND, 5 )

                
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Diret�rio de Arquivo (avalia��o subjetiva)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer1.Add( self.text2, 0, wx.ALL|wx.EXPAND, 5 )
		
                
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"M�tricas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer1.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_checkBox8 = wx.CheckBox( self, wx.ID_ANY, u"PSNR", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_checkBox8, 0, wx.ALL, 5 )
		
		
		self.m_checkBox9 = wx.CheckBox( self, wx.ID_ANY, u"MSE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_checkBox9, 0, wx.ALL, 5 )
		
		
		self.m_checkBox10 = wx.CheckBox( self, wx.ID_ANY, u"MSSIM", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_checkBox10, 0, wx.ALL, 5 )

		self.m_checkBox11 = wx.CheckBox( self, wx.ID_ANY, u"UQI", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_checkBox11, 0, wx.ALL, 5 )

		self.m_checkBox12 = wx.CheckBox( self, wx.ID_ANY, u"SNR", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_checkBox12, 0, wx.ALL, 5 )

		self.m_checkBox13 = wx.CheckBox( self, wx.ID_ANY, u"PBVIF", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_checkBox13, 0, wx.ALL, 5 )

		self.m_checkBox14 = wx.CheckBox( self, wx.ID_ANY, u"NQM", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_checkBox14, 0, wx.ALL, 5 )

		self.m_checkBox15 = wx.CheckBox( self, wx.ID_ANY, u"RMSE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_checkBox15, 0, wx.ALL, 5 )

		bSizer1.Add( gSizer3, 1, wx.EXPAND, 5 )
                
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Regress�es", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer1.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox16 = wx.CheckBox( self, wx.ID_ANY, u"Regress�o Linear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox16, 0, wx.ALL, 5 )
		
		
		self.m_checkBox17 = wx.CheckBox( self, wx.ID_ANY, u"Regress�o Log�stica", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox17, 0, wx.ALL, 5 )
		
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Avalia��o", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer1.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox18 = wx.CheckBox( self, wx.ID_ANY, u"Correla��o de Pearson", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox18, 0, wx.ALL, 5 )
		
		
		self.m_checkBox19 = wx.CheckBox( self, wx.ID_ANY, u"Correla��o de Spearman", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox19, 0, wx.ALL, 5 )
		
		
		self.m_checkBox20 = wx.CheckBox( self, wx.ID_ANY, u"Raz�o de Outliers", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox20, 0, wx.ALL, 5 )
		
		self.m_checkBox21 = wx.CheckBox( self, wx.ID_ANY, u"Analise de Variancia", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox21, 0, wx.ALL, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Gr�ficos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer1.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox22 = wx.CheckBox( self, wx.ID_ANY, u"Tra�ar Gr�ficos", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox22, 0, wx.ALL, 5 )
  	
		
		self.solveButton = wx.Button( self, wx.ID_ANY, u"Iniciar Avalia��o", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.solveButton, 0, wx.ALL|wx.EXPAND, 5 )
		
                
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.solveButton.Bind( wx.EVT_BUTTON, self.solveFunc )
		
                
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def solveFunc( self, event ):
		orig = self.text.GetPath()
		teste = self.text1.GetPath()
		arquivo = self.text2.GetPath()
		psnr = self.m_checkBox8.GetValue()
		mse = self.m_checkBox9.GetValue()
		mssim = self.m_checkBox10.GetValue()
		uqi = self.m_checkBox11.GetValue()
		snr = self.m_checkBox12.GetValue()
		pbvif = self.m_checkBox13.GetValue()
		nqm = self.m_checkBox14.GetValue()
		rmse = self.m_checkBox15.GetValue()
		lin = self.m_checkBox16.GetValue()
		log = self.m_checkBox17.GetValue()
		pearson = self.m_checkBox18.GetValue()
		spearman = self.m_checkBox19.GetValue()
		out = self.m_checkBox20.GetValue()
		anova = self.m_checkBox21.GetValue()
		plot = self.m_checkBox22.GetValue()
		main_aqv.aqv(orig,teste, arquivo,  psnr, mse, mssim, uqi, snr, pbvif, nqm, rmse, lin, log, pearson, spearman, out, anova, plot)
		
		
def main():
        ex = wx.App()
        frame = MainFrame(None)
        frame.Show()
        ex.MainLoop()    

if __name__ == '__main__':
        main()  

