import sys

from controllers.display import DisplayController

from resources.manager import Resource
from resources import qtresources

if __name__ == "__main__":

    if "genimg" in sys.argv:
            Resource.generateSprites()
            Resource.generateBg()

    elif "--help" in sys.argv:
        print "Usage: gameoflife <commands>\n\nCommands:"
        print "genimg: generates the images used in application from sources"
        print "run: run the application"
        print "--help: show this help\n"


    else:
        display = DisplayController()
        display.loadView()