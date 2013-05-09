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

from core.config import Config
from core.view import *
from core.resource_manager import Resource

class HabitatSprite(View):
    def __init__(self, screen):
        View.__init__(self, screen)
        resource = Resource()
        self.config = Config()
        self.background = resource.image("bg", True)

    def generate(self):
        size = self.config.attr.game.habitat.size
        for x in range(size[0]):
            for y in range(size[1]):
                self.screen.blit(self.background, (x*16, y*16))

    def defaultAction(self):
        pass