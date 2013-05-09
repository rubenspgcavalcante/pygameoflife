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

from core.view import *
from core.resource_manager import *

class NotificationSprite(View):
    def __init__(self, screen):
        """
        Loads the notification image with the same name of the class
        """
        View.__init__(self, screen)
        resource = Resource()
        self.position = (0,0)
        self.wait = 1
        self.tick = 0
        self.active = False

        self.image = resource.image(self.__class__.__name__, True)
        self.bg = resource.image("bg", True)


    def defaultAction(self):
        pass


    def put(self):
        self.active = True
        self.tick = pygame.time.get_ticks()
        self.screen.blit(self.image, self.position)


    def remove(self):
        self.clean()
        self.active = False


    def update(self):
        if self.active:
            timePassed = (pygame.time.get_ticks() - self.tick)/1000
            if timePassed < self.wait:
                self.screen.blit(self.image, self.position)
            else:
                self.remove()


    def clean(self):
        width, height = self.image.get_size()
        for x in range(width)[::16]:
            for y in range(height)[::16]:
                self.screen.blit(self.bg, (x, y))


class SpeedUpNotification(NotificationSprite):
    def __init__(self, screen):
        NotificationSprite.__init__(self, screen)


class SpeedDownNotification(NotificationSprite):
    def __init__(self, screen):
        NotificationSprite.__init__(self, screen)

class SaveNotification(NotificationSprite):
    def __init__(self, screen):
        NotificationSprite.__init__(self, screen)

class LoadNotification(NotificationSprite):
    def __init__(self, screen):
        NotificationSprite.__init__(self, screen)

class LoadErrorNotification(NotificationSprite):
    def __init__(self, screen):
        NotificationSprite.__init__(self, screen)