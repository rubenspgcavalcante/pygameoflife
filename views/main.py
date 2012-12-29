import sys

import pygame
from pygame.locals import *

from config import Config
from resources.manager import Resource
from helpers.singleton import singleton

@singleton
class MainView(object):

    def load(self, displayController, args):

        """
        Load the main screen

        arguments;
        displayController: DisplayController instance
        args: Dict with arguments to the view
        """

        pygame.init()

        while True:
            for event in pygame.event.get():
                if event.type in (QUIT, KEYDOWN):
                    sys.exit()
                    
            displayController.update()