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

from abc import abstractmethod
from core.event import Event, TickEvent
from core.mediator import Mediator


class Controller(object):
    def __init__(self):
        #
        # The mediator is a singleton, so every controller instance
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

    @abstractmethod
    def defaultAction(self):
        """
        Default action called at every TickEvent triggered
        """
        raise NotImplementedError(self.__class__.__name__ + " class must implement defaultAction method")

    def bind(self, event, callback):
        """
        Mark to wait the event to be triggered and execute the callback if it does

        @type event: Event
        @param event: The event to wait

        @type callback: CALLBACK_TYPE
        @param callback: The callback function to call when the event occurs

        """
        self.registeredEvents.update({event.name: callback})

    def trigger(self, event):
        """
        Triggers a event to the observer. Objects whose bind the event will be called
        @type event:Event
        @param event: The event to be triggered
        """
        self.eventManager.post(event)