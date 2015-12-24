import wx,string,time
class Traffic_light(wx.Frame):
	def __init__(self, parent=None, id=-1,  
                 pos=wx.DefaultPosition, title='Traffic light'):
		#wx.Frame.__init__(self,parent=None,title=u"Traffic light")
		self.light = 'off.png'
		image = wx.Image(self.light, wx.BITMAP_TYPE_PNG) 
		self.temp = image.ConvertToBitmap()  
		size = self.temp.GetWidth(), self.temp.GetHeight()+40 
		wx.Frame.__init__(self, parent, id, title, pos, size) 
		self.panel = wx.Panel(self)
		self.btn = wx.Button(parent=self.panel,label="Press me",pos=(80,self.temp.GetHeight()))
		#新增 BtnClick 事件 -- 開始 --
		self.Bind(wx.EVT_BUTTON,self.BtnClick,self.btn)
		#新增 BtnClick 事件 -- 結束 --
		self.bmp = wx.StaticBitmap(parent=self.panel, bitmap=self.temp)  
		self.SetClientSize(size)
	def update(self):
		#self.light = 'red.png' 
		image = wx.Image(self.light, wx.BITMAP_TYPE_PNG) 
		self.temp = image.ConvertToBitmap()
		wx.StaticBitmap(parent=self.panel, bitmap=self.temp) 
		
	def BtnClick(self,event):
		self.light = 'green.png'
		self.update()
		
	def light(self):
		self.light = 'red.png'
		
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = Traffic_light()
	frame.Show()
	app.MainLoop()