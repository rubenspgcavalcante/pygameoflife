from core.model import Model
from core.event import *

from views.notification_sprite import *

class NotificationController(Model):

    def __init__(self):
        Model.__init__(self)
        self.activeNotification = None
        self.enabled = False
        self.notificationLib = None

        self.bind(ScreenAvaibleEvent(), self.initNotifications)
        self.bind(ShowNotificationEvent(), self.show)
        self.bind(DisplayRefreshEvent(), self.update)
        self.bind(PauseEvent(), self.removeNotification)

    def initNotifications(self, event):
        self.enabled = True
        self.notificationLib = {
            "speedUp": SpeedUpNotification(event.screen),

            "speedDown": SpeedDownNotification(event.screen)
        }


    def defaultAction(self):
        pass


    def show(self, event):
        if not self.enabled:
            return False

        if self.activeNotification is not None:
            self.activeNotification.remove()

        try:
            self.activeNotification = self.notificationLib[event.notification]
            self.activeNotification.put()
            return True

        except KeyError:
            print "Notification " + event.name + " doesn't exits"
            return False

    def removeNotification(self, event):
        if self.activeNotification is not None and self.activeNotification.active:
            self.activeNotification.remove()
            self.activeNotification = None

    def update(self, event):
        if self.activeNotification is not None and self.enabled:
            if event.layer == 0:
                self.activeNotification.clean()

            elif event.layer == 3:
                self.activeNotification.update()