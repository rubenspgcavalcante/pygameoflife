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

from core.model import Model
from models.habitat_model import Habitat

class Game(Model):

    STATE_PREPARING = 'preparing'
    STATE_READY = 'ready'
    STATE_RUNNING = 'running'
    STATE_PAUSED = 'paused'

    def __init__(self):
        Model.__init__(self)
        self.habitat = Habitat()
        self.state = Game.STATE_PREPARING

    def defaultAction(self):
        pass

    def loadHabitat(self):
        self.habitat.generateFirstPopulation()
        self.state = Game.STATE_READY

    def pause(self):
        if self.state == Game.STATE_RUNNING:
            self.state = Game.STATE_PAUSED

        elif self.state == Game.STATE_PAUSED:
            self.state = Game.STATE_RUNNING

    def nextIteration(self):
        if self.state == Game.STATE_RUNNING:
            self.habitat.nextGeneration()
            return True

        elif self.state == Game.STATE_PAUSED:
            return False

