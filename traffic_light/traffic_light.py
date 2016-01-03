import wx,string,time,threading
#from intersection import Traffic_Light
light = 'off.png'
running_state = 0

class Traffic_Light(threading.Thread):
	"""traffic light self.thread"""
	def __init__(self, go_time, wait_time, panel):
		threading.Thread.__init__(self)
		self.go_time = go_time
		self.wait_time = wait_time
		self.panel = panel
		
	def run(self):
		global light, running_state
		print 'run'
		light = 'green.png'
		time.sleep(self.go_time)
		
		light = 'yellow.png'
		time.sleep(1)
		
		light = 'red.png'
		time.sleep(self.wait_time)
		light = 'green.png'
		running_state = 0
		
class Intersection(wx.Frame):
	def __init__(self, parent=None, id=-1, pos=wx.DefaultPosition, title='Traffic light'):
		global light
		image = wx.Image(light, wx.BITMAP_TYPE_PNG) 
		self.temp = image.ConvertToBitmap()
		
		size = self.temp.GetWidth(), self.temp.GetHeight() + 40 
		wx.Frame.__init__(self, parent, id, title, pos, size) 
		self.panel = wx.Panel(self)
		
		self.btn = wx.Button(parent=self.panel,label='Press me',pos=(80,self.temp.GetHeight()))
		self.Bind(wx.EVT_BUTTON,self.BtnClick,self.btn)
		
		self.updateTimer = wx.Timer(None)
		self.updateTimer.Bind(wx.EVT_TIMER, self.load_image)
		
		light = 'off.png'
		self.load_image(None)
		
		self.SetClientSize(size)
		
	def load_image(self, event):
		image = wx.Image(light, wx.BITMAP_TYPE_PNG) 
		self.temp = image.ConvertToBitmap()
		wx.StaticBitmap(parent=self.panel, bitmap=self.temp) 
		#print event

	def BtnClick(self,event):
		global running_state, light
		self.th = Traffic_Light(3,5,self.panel)
		self.th.start()
		running_state = 1
		self.updateTimer.Start(500)
			
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = Intersection()
	frame.Show()
	app.MainLoop()