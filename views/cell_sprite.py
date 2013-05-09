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

from core.view import *
from core.resource_manager import Resource

class CellSprite(View):
    def __init__(self, screen):
        View.__init__(self, screen)
        resource = Resource()
        self.cell = resource.image("cell", True)
        self.background = resource.image("bg", True)

    def put(self, position):
        x, y = position[0] * 16, position[1] * 16
        self.screen.blit(self.background, (x,y))
        self.screen.blit(self.cell, (x,y))

    def remove(self, position):
        x, y = position[0] * 16, position[1] * 16
        self.screen.blit(self.background, (x,y))