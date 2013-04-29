# -*- coding: utf-8 -*-

import os
import re
import Image
from ctypes import CDLL

import pygame
from lxml import etree
import core.singleton
from core.config import Config

@core.singleton.singleton
class Resource(object):

    def __init__(self):
        self.config = Config()

    def sprite(self, entity):
        """
        Loads a set of images (sprite) which forms a animation that represents
        an entity
        """
        path = os.path.join(self.config.attr.path.resources, self.config.attr.processeddir)
        sprite = pygame.image.load(os.path.join(path, entity + ".png")).convert_alpha()
        images = []
        spriteWidth, spriteHeight = sprite.get_size()
        width, height = getattr(self.config.attr.game, entity).size

        for i in xrange(int(spriteWidth / width)):
            images.append(sprite.subsurface((i * width, 0, width, height)))

        return images


    def image(self, entity, static=False):
        """
        Loads an single image that represents the entity in the game
        """
        path = self.config.attr.path.resources
        if static:
            path = os.path.join(path, self.config.attr.path.staticdir)

        else:
            path = os.path.join(path, self.config.attr.path.processeddir)

        singleImg = pygame.image.load(os.path.join(path, entity + ".png")).convert_alpha()
        return singleImg

    def audio(self, filename, music=False):
        """
        Loads a audio file and return a pygame sound object
        """
        path = os.path.join(self.config.attr.path.resources, self.config.attr.path.audio)
        if music:
            music = pygame.mixer.music
            music.load(os.path.join(path, filename))
            return music

        else:
            return pygame.mixer.Sound(os.path.join(path, filename))

    def dll(self, filename):
        """
        Loads a dinamic library, if in Windows a DLL if in Linux a SO
        """
        path = os.path.join(self.config.attr.path.resources, self.config.attr.path.library)
        extension = ""
        if os.name == "posix":
            extension = ".so"
        elif os.name == "nt":
            extension = ".dll"

        lib = CDLL(path + filename + extension)
        return lib

    def generateSprites(self):
        """
        Generates all the sprites merging the frames in the source directory
        The frames must be in a directory with the name {entity}-frames, where
        entity is the name of the respectively model.
        The frames must be numered XX.png in order of the animation.
        """
        basePath = self.config.attr.path.resources
        src = os.path.join(basePath, self.config.attr.path.sourcedir)
        proccessedDir = os.path.join(basePath, self.config.attr.path.processeddir)

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

    def generateQrcFile(self):
        """
        Generates the qrc xml file, used to compile the files to use in qt
        """
        root = etree.Element("RCC", {"version": "1.0"})
        etree.SubElement(root, "qresource")

        basePath = self.config.attr.path.resources
        qtDir = os.path.join(basePath, self.config.attr.path.qtui)
        qtImages = os.path.join(qtDir, "images")

        #Adds first the Qt CSS file
        qcss = etree.Element("file")
        qcss.text = os.path.join("launcher.qss")
        root[0].append(qcss)

        for imagesFile in os.listdir(qtImages):
            fileTag = etree.Element("file")
            fileTag.text = os.path.join("images", imagesFile)
            root[0].append(fileTag)

        xmlString = etree.tostring(root, pretty_print=True, doctype="<!DOCTYPE RCC>")
        qrcFile = open(os.path.join(qtDir, "resources.qrc"), "w")
        qrcFile.write(xmlString)
        qrcFile.close()
