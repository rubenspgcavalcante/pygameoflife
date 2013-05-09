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
from core.controller import *

class PygameInputController(Controller):

    def __init__(self):
        Controller.__init__(self)

    def defaultAction(self):
        for pygameEvent in pygame.event.get():
            event = None
            if pygameEvent.type == QUIT:
                event = QuitEvent()

            elif pygameEvent.type == KEYDOWN:
                event = KeyboardEvent(pygameEvent.key)

            elif pygameEvent.type == pygame.MOUSEBUTTONDOWN:
                event = MouseEvent(pygameEvent.button)

            if event:
                self.trigger(event)