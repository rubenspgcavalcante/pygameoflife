from core.mvc_commons import MVCCommons

class Controller(MVCCommons):
    def __init__(self):
        MVCCommons.__init__(self)

    def trigger(self, event):
        """
        Triggers a event to the observer. Objects whose bind the event will be called
        :param event:core.event.Event The event to be triggered
        """
        self.eventManager.post(event)