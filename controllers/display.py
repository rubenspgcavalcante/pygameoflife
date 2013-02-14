import sys

import pygame
from PyQt4 import QtGui

from views.main import MainView
from views.launcher import Launcher

from models.habitat import Habitat

from config import Config
from resources.manager import Resource

class DisplayController(object):

    """Manages the display"""

    def __init__(self):
        config = Config()
        self.launch()

        self.view = MainView()
        self.screen = pygame.display.set_mode(config.get("game", "window-size"))
        pygame.display.set_icon(Resource.image("icon", static=True))
        pygame.display.set_caption(Resource.get("display", "title"))

        self.habitat = Habitat(self.screen)

    def launch(self):
        app = QtGui.QApplication(sys.argv)
        window = Launcher(app)
        app.exec_()

    def getScreen(self):
        return self.screen
        

    def update(self):
        self.habitat.nextGeneration()


    def loadView(self):
        
        self.habitat.generateFirstPopulation()

        self.view.load(self, args=None)
