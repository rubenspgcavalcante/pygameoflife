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
from views.notification_sprite import *

from core.resource_manager import *

class DisplayController(Controller):
    def __init__(self, game):
        Controller.__init__(self)
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        pygame.init()

        self.screen = None
        self.speed = None
        self.speedUpNotification = None
        self.speedDownNotification = None
        self.activeNotification = None

        self.layers = []
        self.game = game

        self.bind(GameStartEvent(), self.show)
        self.bind(NewGenerationEvent(), self.getGeneration)
        self.bind(ChangeSpeedEvent(), self.changeSpeed)
        self.bind(CellAddedEvent(), self.setCell)
        self.bind(CellRemovedEvent(), self.delCell)


    def defaultAction(self):
        pass


    def setCell(self, event):
        x, y = event.posx, event.posy
        x = int(x/16)
        y = int(y/16)
        cellSprite = CellSprite(self.screen)
        cellSprite.put((x, y), Resource.get("animation", "frames") - 1)
        pygame.display.flip()


    def delCell(self, event):
        x, y = event.posx, event.posy
        x = int(x/16)
        y = int(y/16)
        cellSprite = CellSprite(self.screen)
        cellSprite.remove((x, y))
        pygame.display.flip()
        

    def updateCells(self):
        cellSprite = CellSprite(self.screen)
        frames = Resource.get("animation", "frames")

        for i in range(self.game.habitat.gridSize[0]):
            for j in range(self.game.habitat.gridSize[1]):
                if self.game.habitat.grid[i][j] == 1:
                    cellSprite.put((i, j), Resource.get("animation", "frames") - 1)
                else:
                    cellSprite.remove((i, j))


    def getGeneration(self, event):
        self.speed = Config().get("game", "speed")
        frames = Resource.get("animation", "frames")

        #Animation loop
        for state in range(frames):
            pygame.time.wait(self.speed)
            self.trigger(DisplayRefreshEvent(0))
            self.updateCells()
            
            pygame.display.flip()


    def changeSpeed(self, event):
        currentSpeed = Config().get("game", "speed")
        diference = currentSpeed + event.delayChange
        
        if event.state == ChangeSpeedEvent.UP:
            self.trigger(ShowNotificationEvent("speedUp"))

        elif event.state == ChangeSpeedEvent.DOWN:
            self.trigger(ShowNotificationEvent("speedDown"))

        if diference < 0 or diference < Config().get("game", "min-delay"):
            currentSpeed = Config().get("game", "min-delay")

        elif diference > Config().get("game", "max-delay"):
            currentSpeed += Config().get("game", "min-delay")

        else:
            currentSpeed = diference

        Config().set("game", "speed", currentSpeed)


    def show(self, event):
        config = Config()
        self.screen = pygame.display.set_mode(config.get("game", "window-size"))
        pygame.display.set_icon(Resource.image("icon", static=True))
        pygame.display.set_caption(Resource.get("display", "title"))

        habitat = HabitatSprite()
        habitat.generate(self.screen)

        self.speedUpNotification = SpeedUpNotification(self.screen)
        self.speedDownNotification = SpeedDownNotification(self.screen)

        self.game.state = Game.STATE_RUNNING
        self.trigger(ScreenAvaibleEvent(self.screen))