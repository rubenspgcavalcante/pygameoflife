class Event(object):
    """this is a superclass for any events that might be generated by an
    object and sent to the EventManager"""

    def __init__(self):
        self.name = "Generic Event"


class TickEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "CPU Tick Event"


class QuitEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Program Quit Event"


class GameStartEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Game Started Event"


class AppStartEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "App Started Event"


class AppStartEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "App Started Event"


class KeyboardEvent(Event):
    def __init__(self, key=None):
        Event.__init__(self)
        self.name = "Keyboard Event"
        self.key = key


class MouseEvent(Event):
    def __init__(self, button=None):
        Event.__init__(self)
        self.name = "Mouse Event"
        self.button = button


class SetCellEvent(Event):
    def __init__(self, posx=None, posy=None):
        Event.__init__(self)
        self.name = "Set Cell Event"
        self.posx = posx
        self.posy = posy


class CellAddedEvent(Event):
    def __init__(self, posx=None, posy=None):
        Event.__init__(self)
        self.name = "Cell Added Event"
        self.posx = posx
        self.posy = posy


class DelCellEvent(Event):
    def __init__(self, posx=None, posy=None):
        Event.__init__(self)
        self.name = "Delete Cell Event"
        self.posx = posx
        self.posy = posy


class CellRemovedEvent(Event):
    def __init__(self, posx=None, posy=None):
        Event.__init__(self)
        self.name = "Cell Removed Event"
        self.posx = posx
        self.posy = posy


class PauseEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Pause Event"

class SaveEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Save event"

class LoadEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Load event"

class LoadErrorEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Load error event"

class ChangeSpeedEvent(Event):
    UP = 1
    DOWN = 0

    def __init__(self, delayChange=None):
        Event.__init__(self)
        self.name = "Change Speed Event"
        self.delayChange = delayChange
        if delayChange < 0:
            self.state = ChangeSpeedEvent.UP
        else:
            self.state = ChangeSpeedEvent.DOWN


class ScreenAvaibleEvent(Event):
    def __init__(self, screen=None):
        Event.__init__(self)
        self.name = "Screen Avaible Event"
        self.screen = screen


class ShowNotificationEvent(Event):
    def __init__(self, notification=None):
        Event.__init__(self)
        self.name = "Show notification"
        self.notification = notification

class ShowErrorNotificationEvent(Event):
    def __init__(self, notification=None):
        Event.__init__(self)
        self.name = "Show error notification"
        self.notification = notification

class DisplayRefreshEvent(Event):
    def __init__(self, layer=None):
        Event.__init__(self)
        self.name = "Display Refresh"
        self.layer = layer