import wx,string
class MySalgar(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,parent=None,title=u"PR計算器",size=(250,210))
		panel = wx.Panel(self)
		wx.StaticText(parent=panel,label=u"全校人數",pos=(10,10))
		self.a = wx.TextCtrl(parent=panel,pos=(80,10))
		wx.StaticText(parent=panel,label=u"校排",pos=(10,50))
		self.b = wx.TextCtrl(parent=panel,pos=(80,50))
		self.btn = wx.Button(parent=panel,label=u"計算PR",pos=(10,90))
		#新增 BtnClick 事件 -- 開始 --
		self.Bind(wx.EVT_BUTTON,self.BtnClick,self.btn)
		#新增 BtnClick 事件 -- 結束 --
		self.message1 = wx.StaticText(parent=panel,pos=(10,130))
	#撰寫 BtnClick 事件函式 -- 開始 --
	def BtnClick(self,event):
		a = self.a.GetValue()
		a = string.atoi(a)
		b = self.b.GetValue()
		b = string.atoi(b)
		a = int(a)
		b = int(b)
		c = 0.000
		c = (a-b)*10000
		c = (c/(a*100))
		#c = float((a - b) / a) * 100
		print a, b, c
		message1Str = u'您的PR是'+str(c)
		self.message1.SetLabel(message1Str)
	#撰寫 BtnClick 事件函式 -- 結束 --
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MySalgar()
	frame.Show()
	app.MainLoop()
