import os

import pygame
from pygame.locals import *

from core.event import *
from core.controller import *
from core.event import *
from core.constants import *

from models.game_model import Game
from views.cell_sprite import CellSprite
from views.habitat_sprite import HabitatSprite

from config import *
from resources.manager import *

class DisplayController(Controller):
    def __init__(self, game):
        Controller.__init__(self)
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        pygame.init()

        self.screen = None
        self.speed = None

        self.backSprites = pygame.sprite.RenderUpdates()
        self.frontSprites = pygame.sprite.RenderUpdates()
        self.bind(GameStartEvent(), self.show)

        self.game = game

        self.bind(NewGenerationEvent(), self.getGeneration)
        self.bind(ChangeSpeedEvent(), self.changeSpeed)

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

            pygame.display.flip()

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

    def show(self, event):
        config = Config()
        self.screen = pygame.display.set_mode(config.get("game", "window-size"))
        pygame.display.set_icon(Resource.image("icon", static=True))
        pygame.display.set_caption(Resource.get("display", "title"))
        habitat = HabitatSprite()
        habitat.generate(self.screen)
        self.game.state = Game.STATE_RUNNING

    def defaultAction(self):
        pass

