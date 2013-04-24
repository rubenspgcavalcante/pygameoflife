from core.event import *
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
        if isinstance(event, TickEvent):
            self.defaultAction()

        else:
            try:
                self.registeredEvents[event.name](event)

            except KeyError as e:
                pass

    def defaultAction(self):
        raise Exception(self.__class__.__name__ + " class must implement defaultAction method")

    def bind(self, event, callback):
        """
        Mark to wait the event to be triggered and execute the callback if it does
        :param event: core.event.Event
        :param callback: Function The callback function
        """
        self.registeredEvents.update({event.name: callback})