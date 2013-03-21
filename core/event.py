class Event:
    """this is a superclass for any events that might be generated by an
    object and sent to the EventManager"""
    def __init__(self):
        self.name = "Generic Event"

class TickEvent(Event):
	def __init__(self):
		self.name = "CPU Tick Event"

class QuitEvent(Event):
	def __init__(self):
		self.name = "Program Quit Event"

class GameStartEvent(Event):
	def __init__(self):
		self.name = "Game Started Event"

class AppStartEvent(Event):
	def __init__(self):
		self.name = "App Started Event"

class AppStartEvent(Event):
    def __init__(self):
        self.name = "App Started Event"

class KeyboardEvent(Event):
    def __init__(self, key=None):
        self.name = "Keyboard Event"
        self.key = key

class MouseEvent(Event):
    def __init__(self, button=None):
        self.name = "Mouse Event"
        self.button = button

class SetCellEvent(Event):
    def __init__(self, posx=None, posy=None):
        self.name = "Set Cell Event"
        self.posx = posx
        self.posy = posy

class DelCellEvent(Event):
    def __init__(self, posx=None, posy=None):
        self.name = "Delete Cell Event"
        self.posx = posx
        self.posy = posy

class NewGenerationEvent(Event):
    def __init__(self, whitelist=None, blacklist=None, stables=None):
        self.name = "New Generation Event"
        self.whitelist = whitelist
        self.blacklist = blacklist
        self.stables = stables

class PauseEvent(Event):
    def __init__(self):
        self.name = "Pause Event"

class ChangeSpeedEvent(Event):
    UP = 1
    DOWN = 0
    def __init__(self, delayChange=None):
        self.name = "Change Speed Event"
        self.delayChange = delayChange
        if delayChange < 0:
            self.state = ChangeSpeedEvent.UP
        else:
            self.state = ChangeSpeedEvent.DOWN

class ScreenAvaibleEvent(Event):
    def __init__(self, screen=None):
        self.name = "Screen Avaible Event"
        self.screen = screen

class ShowNotificationEvent(Event):
    def __init__(self, notification=None):
        self.name = "Show notification"
        self.notification = notification

class DisplayRefreshEvent(Event):
    def __init__(self, layer=None):
        self.name = "Display Refresh"
        self.layer = layer