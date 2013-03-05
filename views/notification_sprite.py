import time

import pygame
from pygame.locals import *

from core.view import *
from resources.manager import *

class NotificationSprite(View):
    def __init__(self, screen, notification):
        View.__init__(self)

        self.screen = screen
        self.position = (0,0)
        self.wait = 1
        self.tick = 0
        self.active = False

        self.notification = notification
        self.image = Resource.image(self.notification, True)
        self.bg = Resource.image("bg", True)

    def defaultAction(self):
        pass

    def put(self):
        self.active = True
        self.tick = pygame.time.get_ticks()
        self.screen.blit(self.image, self.position)

    def update(self):
        if self.active:
            timePassed = (pygame.time.get_ticks() - self.tick)/1000
            if timePassed < self.wait:  
                self.screen.blit(self.image, self.position)

            else:
                width, height = self.image.get_size()
                for x in range(width)[::16]:
                    for y in range(height)[::16]:
                        self.screen.blit(self.bg, (x, y))
                self.active = False