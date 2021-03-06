#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Rubens Pinheiro Gonçalves Cavalcante"
__date__ = "08/05/13 19:18"
__licence__ = "GPLv3"
__email__ = "rubenspgcavalcante@gmail.com"

import logging

import os
import re
import Image
from ctypes import CDLL

import pygame
from lxml import etree
from core.singleton import singleton
from core.config import Config

@singleton
class Resource(object):

    def __init__(self):
        self.config = Config()

    def sprite(self, entity):
        """
        Loads a set of images (sprite) which forms a animation that represents
        an entity
        """
        path = os.path.join(self.config.attr.path.resources, self.config.attr.cache)
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
            path = os.path.join(path, self.config.attr.path.static)

        else:
            path = os.path.join(path, self.config.attr.path.cache)

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
        proccessedDir = os.path.join(basePath, self.config.attr.path.cache)

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

    def logFile(self, level=logging.INFO):
        if level == logging.INFO:
            fileName = Config().attr.logger.info

        elif level == logging.DEBUG:
            fileName = Config().attr.logger.debug

        elif level == logging.ERROR:
            fileName = Config().attr.logger.error

        else:
            raise TypeError("Use logging level enumeration as 'level' parameter")

        logFile = os.path.join(Config().attr.path.base + Config().attr.path.log, fileName)
        return logFile