import wx,string,time,threading
#from intersection import Traffic_Light
light = "off.png"
thread_state = 0
class Traffic_Light(threading.Thread):
	def __init__(self, go_time, wait_time):
		threading.Thread.__init__(self)
		self.go_time = go_time
		self.wait_time = wait_time
		#self.start = time.time()
		
	def run(self):
		global light, thread_state
		print "run"
		light = 'red.png'
		time.sleep(1)
		light = 'yellow.png'
		time.sleep(1)
		thread_state = 0

class Intersection(wx.Frame):
	def __init__(self, parent=None, id=-1, pos=wx.DefaultPosition, title='Traffic light'):
		#wx.Frame.__init__(self,parent=None,title=u"Traffic light")
		global light
		light = 'off.png'
		self.light_num = 0
		image = wx.Image(light, wx.BITMAP_TYPE_PNG) 
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
		image = wx.Image(light, wx.BITMAP_TYPE_PNG) 
		self.temp = image.ConvertToBitmap()
		wx.StaticBitmap(parent=self.panel, bitmap=self.temp) 
		
	def BtnClick(self,event):
		global thread_state, light
		th = Traffic_Light(1,2)
		print "thread start"
		th.start()
		thread_state = 1
		light_old = light
		while thread_state == 1:
			if light_old != light:
				self.update()
			light_old = light
			
		
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = Intersection()
	frame.Show()
	app.MainLoop()