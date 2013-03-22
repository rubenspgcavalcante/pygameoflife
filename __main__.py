import sys

from core.event import *
from core.mediator import *

from controllers.pygame_input_controller import *
from controllers.keyboard_controller import *
from controllers.mouse_controller import *
from controllers.cpuspinner_controller import *
from controllers.display_controller import *
from controllers.launcher_controller import *
from controllers.notification_controller import *
from models.game_model import Game

from core.resource_manager import Resource
from helpers import qtresources

if __name__ == "__main__":

    if "genimg" in sys.argv:
            Resource.generateSprites()

    elif "--version" in sys.argv:
            print Config().get("game", "version")

    elif "--help" in sys.argv:
        print "Usage: run-pygameoflife <commands>\n\nCommands:"
        print "'genimg'  generates the images used in application from sources"
        print "'--version' show the game version"
        print "'--help' show this help\n"

    else:
        inputs = PygameInputController()
        keyboard = KeyboardController()
        mouse = MouseController()
        spinner = CPUSpinnerController()
        launcher = LauncherController()
        notifications = NotificationController()

        game = Game()
        display = DisplayController(game)

        spinner.run()