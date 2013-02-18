import os
import sys
import re
import Image

import pygame
from PyQt4 import uic

from config import Config
from helpers.struct import Struct

class Resource(object):

    @staticmethod
    def get(obj, attr=None):

        path = os.path.dirname(os.path.abspath(__file__))+"/"

        if not os.path.exists(path):
            #If compiled, the binarie is represented like a dir, so we must remove it
            path = re.sub(r'((/|\\)run-pygameoflife(.exe)?)', "", path).replace("/manager.pyc", "")

        resource = {
                "general":{
                    "resourcesPath": path,
                    "sourcedir": "src/",
                    "processeddir": "cache/",
                    "staticdir": "static/",
                    "qtui": "qt/",
                },

                "display":{
                    "icon": "",
                    "icon-size": (64, 64),
                    "title": "PyGame of the Life",
                    "sleep": 0,
                },
                
                "cell": {
                    "size": (16, 16),
                    "frames": 11,
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

        path =  Resource.get("general", "resourcesPath") + \
                Resource.get("general", "processeddir")

        sprite = pygame.image.load(path + entity + ".png").convert_alpha()

        images = []
        spriteWidth, spriteHeight = sprite.get_size()
        width, height =  Resource.get(entity, "size")

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
            path += Resource.get("general", "staticdir")

        else:
            path += Resource.get("general", "processeddir")

        singleImg = pygame.image.load(path + entity + ".png").convert_alpha()
        return singleImg

    @staticmethod
    def getQtUI(uiName):
        """
        Loads a Qt UI file
        """
        path =  Resource.get("general", "resourcesPath") + \
                Resource.get("general", "qtui")

        qtUI = uic.loadUi(path + uiName + ".ui")

        return qtUI

    @staticmethod
    def getQss(uiName):
        """
        Loads a Qt Style Sheet file
        """
        path =  Resource.get("general", "resourcesPath") + \
                Resource.get("general", "qtui")

        basePath = Resource.get("general", "resourcesPath")

        cssFile = open(path + uiName + ".qss", "r")
        qtCSS = cssFile.read().replace("\n", "").replace("%path%", basePath)
        cssFile.close()

        return qtCSS

    @staticmethod
    def generateSprites():
        """
        Generates all the sprites merging the frames in the source directory
        The frames must be in a directory with the name {entity}-frames, where
        entity is the name of the respectively model.
        The frames must be numered XX.png in order of the animation.
        """

        basePath = Resource.get("general", "resourcesPath")
        src = basePath + Resource.get("general", "sourcedir")
        proccessedDir = basePath + Resource.get("general", "processeddir")

        for _dir in os.listdir(src):

            if "frames" in _dir:
                entity = _dir.split("-")[0]
                resource = Resource.get(entity)
                width = resource["size"][0] * resource["frames"]

                size = (width, resource["size"][0])
                final = Image.new("RGBA", size)
                
                sortedFiles = os.listdir(src + _dir)
                sortedFiles.sort()

                for index, _file in enumerate(sortedFiles):
                    path = src + _dir + "/" + _file
                    frame = Image.open(path)


                    final.paste(frame, (index*16, 0))

                
                entity = _dir.split("-")[0];

                print "generating: " + entity + ".png"
                final.save(proccessedDir + entity + ".png")
                
    @staticmethod
    def generateBg():
        """
        Generates the background grid of the game, made up from a
        16x16 image.
        """
        basePath = Resource.get("general", "resourcesPath")
        src = basePath + Resource.get("general", "sourcedir")
        proccessedDir = basePath + Resource.get("general", "processeddir")

        sqr = Image.open(src + "background/block.png")

        size = Config().get("game", "window-size")
        blank = Image.new("RGBA", size)

        lin = size[0]/16
        col = size[0]/16

        for i in range(lin):
            for j in range(col):
                blank.paste(sqr, (i*16, j*16))

        print "generating background"
        blank.save(proccessedDir + Resource.get("habitat", "filename"))

