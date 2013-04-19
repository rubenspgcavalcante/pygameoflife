import sys

import controllers.pygame_input_controller
from controllers.keyboard_controller import *
from controllers.mouse_controller import *
from controllers.cpuspinner_controller import *
from controllers.display_controller import *
from controllers.launcher_controller import *
from controllers.notification_controller import *
from controllers.sound_effect_controller import *

from models.game_model import Game

from core.resource_manager import Resource

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
        inputs = controllers.pygame_input_controller.PygameInputController()
        keyboard = KeyboardController()
        mouse = MouseController()
        spinner = CPUSpinnerController()
        launcher = LauncherController()
        notifications = NotificationController()
        sounds = SoundEffectController()

        game = Game()
        display = DisplayController(game)

        spinner.run()