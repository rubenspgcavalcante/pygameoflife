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

import pygame

from core.event import *
from core.controller import *

class MouseController(Controller):

    def __init__(self):
        Controller.__init__(self)
        self.pushed = False
        self.bind(MouseEvent(), self.buttonMap)

    def defaultAction(self):
        #User, keeps the mouse button pressed
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            self.trigger(SetCellEvent(pos[0], pos[1]))

        elif pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            self.trigger(DelCellEvent(pos[0], pos[1]))

    def buttonMap(self, event):
        triggerEvent = None

        if event.button == 1:
            pos = pygame.mouse.get_pos()
            triggerEvent = SetCellEvent(pos[0], pos[1])

        if event.button == 3:
            pos = pygame.mouse.get_pos()
            triggerEvent = DelCellEvent(pos[0], pos[1])

        if triggerEvent:
            self.trigger(triggerEvent)