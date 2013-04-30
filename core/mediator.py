from weakref import WeakKeyDictionary
from core.event import Event

from core.singleton import singleton

@singleton
class Mediator:
    """this object is responsible for coordinating most communication
    between the Model, View, and Controller."""
    def __init__(self):
        self.listeners = WeakKeyDictionary()
        self.eventQueue= []
        self.debug = True

    def registerListener(self, listener):
        """
        @type listener: Controller
        @param listener: The name of the listener to register
        """
        self.listeners[listener] = 1

    def unregisterListener(self, listener):
        """
        @type listener: Controller
        @param listener: The name of the listener to unregister
        """
        if listener in self.listeners:
            del self.listeners[listener]

    def post(self, event):
        """
        Notify the registered listeners to a event

        @type event: Event
        @param event: Event to trigger
        """
        listeners = self.listeners.items()

        for listener in listeners:
            listener[0].notify(event)

        del listeners