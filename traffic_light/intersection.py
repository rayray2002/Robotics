import threading
import time
class Traffic_Light(threading.Thread):
	def __init__(self, go_time, wait_time):
		threading.Thread.__init__(self)
		self.go_time = go_time
		self.wait_time = wait_time
		self.start = time.time
	def run(self):
		light = 'red.png'

th = Traffic_Light(1,1)
th.start()