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

from weakref import WeakKeyDictionary
import controllers
from core.event import Event, TickEvent

from core.singleton import singleton

@singleton
class Mediator(object):
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