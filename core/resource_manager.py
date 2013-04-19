# -*- coding: utf-8 -*-

import os
import re
import Image
from ctypes import CDLL

import pygame

from core.config import Config

class Resource(object):

    @staticmethod
    def get(obj, attr=None):

        path = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))

        if not os.path.exists(path + "/"):
            #If compiled, the binarie is represented like a dir, so we must remove it
            path = re.sub(r'((/|\\)run-pygameoflife(.exe)?)', "", path).replace("/resource_manager.pyc", "")

        resource = {
                "general":{
                    "resourcesPath": path + "/resources/",
                    "sourcedir": "src/",
                    "audio": "audio/",
                    "library": "library/",
                    "processeddir": "cache/",
                    "staticdir": "static/",
                    "qtui": "qt/",
                },

                "display":{
                    "icon": "",
                    "icon-size": (64, 64),
                    "title": "PyGame of the Life",
                },

                "animation": {
                    "frames": 4,
                },
                
                "cell": {
                    "size": (16, 16),
                },

                "habitat": {
                    "filename": "habitat.png",
                    "size": Config().get("game", "window-size"),
                    "frames": 1,
                },

            }

        try:
            if attr is None:
                return resource[obj]

            else:
                return resource[obj][attr]

        except KeyError:
            return None


    @staticmethod
    def sprite(entity):
        """
        Loads a set of images (sprite) wich forms a animation that represents
        an entity
        """

        path = os.path.join(Resource.get("general", "resourcesPath"), Resource.get("general", "processeddir"))

        sprite = pygame.image.load(os.path.join(path, entity + ".png")).convert_alpha()

        images = []
        spriteWidth, spriteHeight = sprite.get_size()
        width, height = Resource.get(entity, "size")

        for i in xrange(int(spriteWidth / width)):
            images.append(sprite.subsurface((i * width, 0, width, height)))

        return images


    @staticmethod
    def image(entity, static=False):
        """
        Loads an single image that represents the entity in the game
        """

        path = Resource.get("general", "resourcesPath")
        if static:
            path = os.path.join(path, Resource.get("general", "staticdir"))

        else:
            path = os.path.join(path, Resource.get("general", "processeddir"))

        singleImg = pygame.image.load(os.path.join(path, entity + ".png")).convert_alpha()
        return singleImg

    @staticmethod
    def audio(filename, music=False):
        """
        Loads a audio file and return a pygame sound object
        """
        path = os.path.join(Resource.get("general", "resourcesPath"), Resource.get("general", "audio"))
        if music:
            music = pygame.mixer.music
            music.load(os.path.join(path, filename))
            return music

        else:
            return pygame.mixer.Sound(os.path.join(path, filename))


    @staticmethod
    def dll(filename):
        """
        Loads a dinamic library, if in Windows a DLL if in Linux a SO
        """
        path = os.path.join(Resource.get("general", "resourcesPath"), Resource.get("general", "library"))
        if os.name == "posix":
            extension = ".so"
        elif os.name == "nt":
            extension = ".dll"

        lib = CDLL(path + filename + extension)
        return lib



    @staticmethod
    def generateSprites():
        """
        Generates all the sprites merging the frames in the source directory
        The frames must be in a directory with the name {entity}-frames, where
        entity is the name of the respectively model.
        The frames must be numered XX.png in order of the animation.
        """

        basePath = Resource.get("general", "resourcesPath")
        src = os.path.join(basePath, Resource.get("general", "sourcedir"))
        proccessedDir = os.path.join(basePath, Resource.get("general", "processeddir"))

        for _dir in os.listdir(src):
            if "frames" in _dir:
                sortedFiles = os.listdir(src + _dir)
                sortedFiles.sort()

                #
                # Opens the first file and get the template size based on the
                # width and number of images
                #
                sprite = Image.open(os.path.join(src, _dir, sortedFiles[0]))
                width = sprite.size[0] * len(sortedFiles)
                size = (width, sprite.size[1])

                final = Image.new("RGBA", size)

                for index, _file in enumerate(sortedFiles):

                    if re.search(r'^[0-9]+(.png)$', _file):
                        path = src + _dir + "/" + _file
                        frame = Image.open(path)
                        final.paste(frame, (index*16, 0))

                    else:
                        print _file + " is not a valid type, not using it"

                
                entity = _dir.split("-")[0]

                print "generating: " + entity + ".png"
                final.save(os.path.join(proccessedDir , entity + ".png"))

