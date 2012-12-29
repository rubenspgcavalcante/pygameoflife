import sys

from controllers.display import DisplayController

from resources.manager import Resource

if __name__ == "__main__":
    
    if "genimg" in sys.argv:
            Resource.generateSprites()
            Resource.generateBg()

    elif "run" in sys.argv:
        display = DisplayController()
        display.loadView()

    elif "--help" in sys.argv:
        print "Usage: gameoflife <commands>\n\nCommands:"
        print "genimg: generates the images used in application from sources"
        print "run: run the application"
        print "--help: show this help\n"



    else:
        print "Usage: gameoflife <commands> \n" + \
              "gameoflife --help for more information"
        