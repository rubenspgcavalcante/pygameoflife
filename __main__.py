import sys

import pygame
from pygame.locals import *

from controllers.display import DisplayController
from models.habitat import Habitat
from config import Config
from resources.manager import Resource

if __name__ == "__main__":

    if "genimg" in sys.argv:
        Resource.generateSprites()
        Resource.generateBg()

    elif "run" in sys.argv:
        displayController = DisplayController()

        screen = displayController.getScreen()

        habitat = Habitat(screen)
        habitat.generateFirstPopulation()
        
        pygame.init()

        while True:
            for event in pygame.event.get():
                if event.type in (QUIT, KEYDOWN):
                    sys.exit()
                    
            displayController.update()

    elif "--help" in sys.argv:
        print "Usage: gameoflife <commands>\n\nCommands:"
        print "genimg: generates the images used in application from sources"
        print "run: run the application"
        print "--help: show this help\n"



    else:
        print "Usage: gameoflife <commands> \n" + \
              "gameoflife --help for more information"
        