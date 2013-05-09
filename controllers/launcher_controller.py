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
from views.qtabout import Ui_aboutWindow

__author__ = "Rubens Pinheiro Gonçalves Cavalcante"
__date__ = "08/05/13 19:18"
__licence__ = "GPLv3"
__email__ = "rubenspgcavalcante@gmail.com"

import sys

from PyQt4 import QtCore, QtGui

from core.controller import *
from core.event import *
from core.config import Config
from models.frameless_window_model import FramelessWindowModel

class LauncherController(FramelessWindowModel, Controller):
    def __init__(self):
        Controller.__init__(self)
        FramelessWindowModel.__init__(self)
        self.config = Config()
        self.setWindowIcon(QtGui.QIcon(":images/icon.png"))
        self.setDefaults()
        self.loadQss("launcher.qss")
        self.center()
        self.show()
        self.setFixedSize(self.size())
        self.connectSignals()
        self.bind(AppStartEvent(), self.appExec)

    def appExec(self, event):
        self.qApp.exec_()

    def defaultAction(self):
        pass

    def connectSignals(self):

        #Sliders
        self.connect(self.ui.populationSlider, QtCore.SIGNAL('valueChanged(int)'), self.updatePopLabel)
        self.connect(self.ui.soundFxSlider, QtCore.SIGNAL('valueChanged(int)'), self.updateSoundLabel)
        self.connect(self.ui.musicSlider, QtCore.SIGNAL('valueChanged(int)'), self.updateMusicLabel)

        # Connect up the buttons.
        self.connect(self.ui.keyMap, QtCore.SIGNAL("clicked()"), self.showKeyMap)
        self.connect(self.ui.about, QtCore.SIGNAL("clicked()"), self.showAbout)
        self.connect(self.ui.submit, QtCore.SIGNAL("clicked()"), self.runGame)

        self.connect(self.ui.closeButton, QtCore.SIGNAL("clicked()"), self.exit)
        self.connect(self.ui.cancel, QtCore.SIGNAL("clicked()"), self.exit)

        #Window close button
        self.closeEvent = self.exit

    def center(self):
        windowFrame = self.frameGeometry()
        centerPosition = QtGui.QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(centerPosition)
        self.move(windowFrame.topLeft())

    def setDefaults(self):
        resolutions = self.config.attr.setup.resolution
        for size in ('small', 'medium', 'large'):
            item = getattr(resolutions, size)
            text = str(item[0]) + " x " + str(item[1])
            self.ui.resolutionComboBox.addItem(text, item)

        speeds = self.config.attr.setup.speed
        for speed in ('slow', 'medium', 'fast'):
            value = getattr(speeds, speed)
            self.ui.speedComboBox.addItem(speed, value)

    def showKeyMap(self):
        self.ui.keyMapWindow = QtGui.QWidget()
        self.ui.keyMapWindow.setWindowTitle("Key map")
        self.ui.keyMapWindow.setFixedSize(QtCore.QSize(800, 240))
        windowFrame = self.ui.keyMapWindow.frameGeometry()
        centerPosition = QtGui.QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(centerPosition)
        self.ui.keyMapWindow.move(windowFrame.topLeft())

        picture = QtGui.QLabel(self.ui.keyMapWindow)
        picture.setGeometry(0, 0, 800, 240)
        picture.setPixmap(QtGui.QPixmap(":/images/keymap.png"))

        self.ui.keyMapWindow.show()

    def showAbout(self):
        self.ui.aboutWindow = QtGui.QWidget()
        aboutUi = Ui_aboutWindow()
        aboutUi.setupUi(self.ui.aboutWindow)
        aboutUi.version.setText(self.config.attr.game.version)

        self.ui.aboutWindow.setWindowTitle("About")
        self.ui.aboutWindow.setFixedSize(QtCore.QSize(500, 275))

        windowFrame = self.ui.aboutWindow.frameGeometry()
        centerPosition = QtGui.QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(centerPosition)
        self.ui.aboutWindow.move(windowFrame.topLeft())
        self.ui.aboutWindow.show()

    def runGame(self):
        resolution = self.ui.resolutionComboBox.itemData(self.ui.resolutionComboBox.currentIndex()).toPyObject()
        speed = self.ui.speedComboBox.itemData(self.ui.speedComboBox.currentIndex()).toPyObject()

        initialPop = float(self.ui.populationSlider.value()) / 100
        fxVol = float(self.ui.soundFxSlider.value()) / 100
        musicVol = float(self.ui.musicSlider.value()) / 100

        self.config.attr.game.window.size = resolution
        self.config.attr.game.population.percentage = initialPop
        self.config.attr.game.volume.fx = fxVol
        self.config.attr.game.volume.music =  musicVol
        self.config.attr.game.speed = speed

        self.qApp.quit()
        self.hide()
        self.trigger(GameStartEvent())

    def exit(self, event=None):
        self.trigger(QuitEvent())
        sys.exit()

    def updatePopLabel(self, value):
        self.ui.populationValueLabel.setText(str(value) + "%")

    def updateSoundLabel(self, value):
        self.ui.soundFxValueLabel.setText(str(value) + "%")

    def updateMusicLabel(self, value):
        self.ui.musicValueLabel.setText(str(value) + "%")