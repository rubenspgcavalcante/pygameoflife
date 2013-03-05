import sys

from core.event import *
from core.mediator import *

from controllers.keyboard_controller import *
from controllers.cpuspinner_controller import *
from controllers.display_controller import *
from controllers.launcher_controller import *
from models.game_model import Game

from resources.manager import Resource
from resources import qtresources

if __name__ == "__main__":

    if "genimg" in sys.argv:
            Resource.generateSprites()

    elif "--help" in sys.argv:
        print "Usage: run-pygameoflife <commands>\n\nCommands:"
        print "genimg: generates the images used in application from sources"
        print "--help: show this help\n"

    else:
        keybd = KeyboardController()
        spinner = CPUSpinnerController()
        launcher = LauncherController()

        game = Game()
        display = DisplayController(game)

        spinner.run()