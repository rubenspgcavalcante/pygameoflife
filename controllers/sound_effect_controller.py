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

from core.controller import Controller
from core.resource_manager import Resource
from core.event import *
from core.config import Config

class SoundEffectController(Controller):

    def __init__(self):
        Controller.__init__(self)
        pygame.mixer.init()
        resource = Resource()
        self.config = Config()
        self.musicOn = False

        self.effects = {
            "bubble": resource.audio("bubble.wav"),
            "click": resource.audio("click.wav"),
            "delete":resource.audio("delete.wav"),
        }

        self.bgSound = resource.audio("bg.wav", music=True)

        self.bind(CellAddedEvent(), self.onCellAddedDoBubble)
        self.bind(CellRemovedEvent(), self.onCellRemovedDoDelete)
        self.bind(PauseEvent(), self.onPauseDoClick)
        self.bind(GameStartEvent(), self.onGameStartDoBackground)

    def defaultAction(self):
        pass


    def onCellAddedDoBubble(self, event):
        self.effects["bubble"].stop()
        self.effects["bubble"].play()


    def onCellRemovedDoDelete(self, event):
        self.effects["delete"].stop()
        self.effects["delete"].play()


    def onPauseDoClick(self, event):
        self.effects["click"].stop()
        self.effects["click"].play()

        if self.musicOn:
            self.bgSound.pause()
            self.musicOn = False

        else:
            self.bgSound.unpause()
            self.musicOn = True


    def onGameStartDoBackground(self, event):
        pygame.mixer.music.set_volume(self.config.attr.game.volume.music)
        fxVol = self.config.attr.game.volume.fx
        
        for i in self.effects:
            self.effects[i].set_volume(fxVol)

        self.bgSound.play()
        self.musicOn = True