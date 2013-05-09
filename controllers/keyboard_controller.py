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
from pygame.locals import *

from core.event import *
from core.constants import *
from core.controller import *

class KeyboardController(Controller):

    def __init__(self):
        Controller.__init__(self)
        self.bind(KeyboardEvent(), self.keyMap)

    def defaultAction(self):
        pass

    def keyMap(self, event):
        triggerEvent = None

        ctrlPressed = pygame.key.get_pressed()[K_LCTRL] or pygame.key.get_pressed()[K_RCTRL]

        if event.key == K_ESCAPE:
            triggerEvent = QuitEvent()

        if event.key == K_SPACE:
            triggerEvent = PauseEvent()

        elif event.key == K_UP:
            triggerEvent = ChangeSpeedEvent(DELAY_DOWN)

        elif event.key == K_DOWN:
            triggerEvent = ChangeSpeedEvent(DELAY_UP)

        elif event.key == K_LEFT:
            triggerEvent = ChangeSpeedEvent(DELAY_UP)

        elif event.key == K_RIGHT:
            triggerEvent = ChangeSpeedEvent(DELAY_DOWN)

        elif event.key == K_s and ctrlPressed:
            triggerEvent = SaveEvent()

        elif event.key == K_r and ctrlPressed:
            triggerEvent = LoadEvent()

        if triggerEvent:
            self.trigger(triggerEvent)