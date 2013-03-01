import pygame
from pygame.locals import *

from core.event import *
from core.controller import *
from core.event import *
from models.game_model import Game

from config import *
from resources.manager import *

class DisplayController(Controller):
    def __init__(self, game):
        Controller.__init__(self)

        pygame.init()

        self.screen = None
        self.backSprites = pygame.sprite.RenderUpdates()
        self.frontSprites = pygame.sprite.RenderUpdates()
        self.bind(GameStartEvent(), self.show)

        self.game = game
        self.bind(NewGenerationEvent(), self.getGeneration)

    def getGeneration(self, event):
        pass


    def show(self, event):
        config = Config()
        self.screen = pygame.display.set_mode(config.get("game", "window-size"))
        pygame.display.set_icon(Resource.image("icon", static=True))
        pygame.display.set_caption(Resource.get("display", "title"))
        pygame.display.flip()
        self.game.state = Game.STATE_RUNNING

    def defaultAction(self):
        pass

