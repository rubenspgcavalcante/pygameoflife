from core.constants import CALLBACK_TYPE
from core.event import *
from core.event import Event
from core.mediator import Mediator

class MVCCommons:
    def __init__(self):

        #
        # The mediator is a singleton, so every mediator api instance
        # will have the same mediator reference.
        #
        self.eventManager = Mediator()
        self.eventManager.registerListener(self)
        self.registeredEvents = {}

    def notify(self, event):
        """
        Call the callback function associated to the event
        @private
        @type event: Event
        @param event: The event used to trigger the callback
        """
        if isinstance(event, TickEvent):
            self.defaultAction()

        else:
            try:
                self.registeredEvents[event.name](event)

            except KeyError as e:
                pass

    def defaultAction(self):
        """
        Default action called at every TickEvent triggered
        Is like a interface forcing the developer to implement this method
        """
        raise Exception(self.__class__.__name__ + " class must implement defaultAction method")

    def bind(self, event, callback):
        """
        Mark to wait the event to be triggered and execute the callback if it does

        @type event: Event
        @param event: The event to wait

        @type callback: CALLBACK_TYPE
        @param callback: The callback function to call when the event occurs

        """
        self.registeredEvents.update({event.name: callback})