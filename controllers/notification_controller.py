#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Rubens Pinheiro Gonçalves Cavalcante"
__date__ = "08/05/13 19:18"
__licence__ = "GPLv3"
__email__ = "rubenspgcavalcante@gmail.com"

from core.controller import Controller
from core.event import *
from views.notification_sprite import *

class NotificationController(Controller):

    def __init__(self):
        Controller.__init__(self)
        self.activeNotification = None
        self.enabled = False
        self.notificationLib = None
        self.errorNotificationLib = None

        self.bind(ScreenAvaibleEvent(), self.initNotifications)
        self.bind(ShowNotificationEvent(), self.show)
        self.bind(DisplayRefreshEvent(), self.update)
        self.bind(PauseEvent(), self.removeNotification)

    def initNotifications(self, event):
        self.enabled = True
        self.notificationLib = {
            "speedUp": SpeedUpNotification(event.screen),
            "speedDown": SpeedDownNotification(event.screen),
            "save": SaveNotification(event.screen),
            "load": LoadNotification(event.screen),
        }

        self.errorNotificationLib = {
            "load": LoadErrorNotification(event.screen)
        }

    def defaultAction(self):
        pass

    def show(self, event):
        if not self.enabled:
            return False

        if self.activeNotification is not None:
            self.activeNotification.remove()

        try:
            if event.error:
                self.activeNotification = self.errorNotificationLib[event.notification]

            else:
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