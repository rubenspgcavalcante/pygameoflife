from core.event import *
from core.controller import *

class CPUSpinnerController(Controller):
	"""..."""
	def __init__(self):
		Controller.__init__(self)
		self.keepGoing = 1

		self.bind(QuitEvent(), self.stop)

	def defaultAction(self):
		pass

	def run(self):
		self.trigger(AppStartEvent())
		while self.keepGoing:
			self.trigger(TickEvent())

	def stop(self, event):
			#this will stop the while loop from running
			self.keepGoing = False