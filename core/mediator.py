from weakref import WeakKeyDictionary

from core.singleton import singleton

@singleton
class Mediator:
	"""this object is responsible for coordinating most communication
	between the Model, View, and Controller."""
	def __init__(self):
		self.listeners = WeakKeyDictionary()
		self.eventQueue= []
		self.debug = True


	def registerListener( self, listener ):
		self.listeners[ listener ] = 1


	def unregisterListener( self, listener ):
		if listener in self.listeners:
			del self.listeners[ listener ]

		
	def post( self, event ):
		listeners = self.listeners.items()

		for listener in listeners:
			#if isinstance(event, ShowNotificationEvent):
			#	print listener[0]

			listener[0].notify( event )

		del listeners