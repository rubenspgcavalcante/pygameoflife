import os

import pygame
from pygame.locals import *

from core.event import *
from core.controller import *
from core.event import *
from core.constants import *
from core.config import *

from models.game_model import Game
from views.cell_sprite import CellSprite
from views.habitat_sprite import HabitatSprite
from views.notification_sprite import NotificationSprite

from resources.manager import *

class DisplayController(Controller):
    def __init__(self, game):
        Controller.__init__(self)
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        pygame.init()

        self.screen = None
        self.speed = None
        self.speedNotification = None
        self.layers = []

        self.bind(GameStartEvent(), self.show)

        self.game = game

        self.bind(NewGenerationEvent(), self.getGeneration)
        self.bind(ChangeSpeedEvent(), self.changeSpeed)
        self.bind(SetCellEvent(), self.setCell)


    def defaultAction(self):
        pass

    def setCell(self, event):
        x, y = event.posx, event.posy
        x = int(x/16)
        y = int(y/16)
        cellSprite = CellSprite(self.screen)
        cellSprite.put((x, y), Resource.get("animation", "frames") - 1)
        pygame.display.flip()

    def orderedUpdate(self):
        self.speedNotification.clean()
        self.speedNotification.update()
        pygame.display.flip()


    def getGeneration(self, event):
        cellSprite = CellSprite(self.screen)
        frames = Resource.get("animation", "frames")
        self.speed = Config().get("game", "speed")

        #Animation loop
        for state in range(frames):
            pygame.time.wait(self.speed)
            for position in event.whitelist:
                cellSprite.put(position, state)

            for position in event.blacklist:
                cellSprite.remove(position)
            
            #Stables
            for position in event.stables:
                cellSprite.put(position, frames-1)

            self.orderedUpdate()



    def changeSpeed(self, event):
        currentSpeed = Config().get("game", "speed")
        diference = currentSpeed + event.delayChange

        if diference < 0 or diference < Config().get("game", "min-delay"):
            currentSpeed = Config().get("game", "min-delay")
        elif diference > Config().get("game", "max-delay"):
            currentSpeed += Config().get("game", "min-delay")
        else:
            currentSpeed = diference

        Config().set("game", "speed", currentSpeed)
        self.speedNotification.put()


    def show(self, event):
        config = Config()
        self.screen = pygame.display.set_mode(config.get("game", "window-size"))
        pygame.display.set_icon(Resource.image("icon", static=True))
        pygame.display.set_caption(Resource.get("display", "title"))

        habitat = HabitatSprite()
        habitat.generate(self.screen)

        self.speedNotification = NotificationSprite(self.screen, "speed")

        self.game.state = Game.STATE_RUNNING