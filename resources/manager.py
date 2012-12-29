import os
import sys
import Image
from zipfile import ZipFile
from cStringIO import StringIO

import pygame

from config import Config
from helpers.struct import Struct

class Resource(object):

    @staticmethod
    def get(obj, attr=None):

        #If calling directly the __main__.py, don't put a absolute basePath
        if sys.argv[0] not in ("__main__.py", "__main__.pyc"):
            basePath = os.path.dirname(sys.argv[0])+"/"
        else:
            basePath = "./"

        resource = {
                "general":{
                    "basePath": basePath,
                    "rootdir": "resources/",
                    "sourcedir": "src/",
                    "processeddir": "data/"
                },

                "display":{
                    "icon": "",
                    "icon-size": (64, 64),
                    "title": "PyGame of the Life",
                    "sleep": 50
                },
                
                "cell": {
                    "size": (16, 16),
                    "frames": 11,
                },

                "habitat": {
                    "filename": "habitat.png",
                    "size": Config.get("game", "window-size"),
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

        path =  Resource.get("general", "basePath") + \
                Resource.get("general", "rootdir") + \
                Resource.get("general", "processeddir")

        try:
            sprite = pygame.image.load(path + entity + ".png").convert_alpha()

        except pygame.error:
            #If the file wasn't found, probaly the software is in the zip package
            #So we'll try to load into the zip file

            #Path in the zip file
            path =  Resource.get("general", "rootdir") + \
                    Resource.get("general", "processeddir")

            zipPack = ZipFile(os.getcwd() + "/pygame-of-life.zip")
            data = zipPack.read(path + entity + ".png")
            data_io = StringIO(data)
            
            sprite = pygame.image.load(data_io, entity + ".png").convert_alpha()

        finally:
            images = []
            spriteWidth, spriteHeight = sprite.get_size()
            width, height =  Resource.get(entity, "size")

            for i in xrange(int(spriteWidth / width)):
                images.append(sprite.subsurface((i * width, 0, width, height)))

            return images

    @staticmethod
    def image(entity):
        """
        Loads an single image that represents the entity in the game
        """

        path =  Resource.get("general", "basePath") + \
                Resource.get("general", "rootdir") + \
                Resource.get("general", "processeddir")

        try:
            singleImg = pygame.image.load(path + entity + ".png").convert_alpha()

        except pygame.error:
            #Path in the zip file
            path =  Resource.get("general", "rootdir") + \
                    Resource.get("general", "processeddir")

            zipPack = ZipFile(os.getcwd() + "/pygame-of-life.zip")
            data = zipPack.read(path + entity + ".png")
            data_io = StringIO(data)
            
            singleImg = pygame.image.load(data_io, entity + ".png").convert_alpha()

        finally:
            return singleImg


    @staticmethod
    def generateSprites():
        """
        Generates all the sprites merging the frames in the source directory
        The frames must be in a directory with the name {entity}-frames, where
        entity is the name of the respectively model.
        The frames must be numered XX.png in order of the animation.
        """

        basePath = Resource.get("general", "rootdir")
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
        basePath = Resource.get("general", "rootdir")
        src = basePath + Resource.get("general", "sourcedir")
        proccessedDir = basePath + Resource.get("general", "processeddir")

        sqr = Image.open(src + "background/block.png")
        blank = Image.new("RGBA", (1024, 768))

        for i in range(64):
            for j in range(48):
                blank.paste(sqr, (i*16, j*16))

        print "generating background"
        blank.save(proccessedDir + Resource.get("habitat", "filename"))

