from PyQt4.uic.Compiler.qtproxies import QtCore
import sys

from PyQt4 import QtCore, QtGui

from core.controller import *
from core.event import *
from core.config import Config
from helpers.qtresources import *

from views.qtlauncher import Ui_MainWindow


class LauncherController(QtGui.QMainWindow, Controller):
    def __init__(self):
        self.qApp = QtGui.QApplication(sys.argv)

        QtGui.QMainWindow.__init__(self)
        Controller.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setDefaults()
        self.loadQss()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

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

        #Title bar
        self.connect(self.ui.customTitleBar, QtCore.SIGNAL('mouseMove()'), self.mouseMoveEvent)
        self.connect(self.ui.customTitleBar, QtCore.SIGNAL('mouseMove()'), self.mousePressEvent)

        # Connect up the buttons.
        self.connect(self.ui.keyMap, QtCore.SIGNAL("clicked()"), self.showKeyMap)
        self.connect(self.ui.submit, QtCore.SIGNAL("clicked()"), self.runGame)
        self.connect(self.ui.cancel, QtCore.SIGNAL("clicked()"), self.exit)

        #Window close button
        self.closeEvent = self.exit


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.ui.customTitleBar.moving = True
            self.ui.customTitleBar.offset = event.pos()


    def mouseMoveEvent(self, event):
        if self.ui.customTitleBar.moving:
            self.move(event.globalPos() - self.ui.customTitleBar.offset)


    def loadQss(self):
        css = QtCore.QFile(':/launcher.qss')
        css.open(QtCore.QIODevice.ReadOnly)

        if css.isOpen():
            self.setStyleSheet(QtCore.QVariant(css.readAll()).toString())
            css.close()
            return True
        else:
            return False


    def center(self):
        windowFrame = self.frameGeometry()
        centerPosition = QtGui.QDesktopWidget().availableGeometry().center()
        windowFrame.moveCenter(centerPosition)
        self.move(windowFrame.topLeft())


    def setDefaults(self):
        for item in Config().get("setup", "resolutions"):
            text = str(item[0]) + " x " + str(item[1])
            self.ui.resolutionComboBox.addItem(text, item)

        for speed in Config().get("setup", "speed"):
            value = Config().get("setup", "speed")[speed]
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


    def runGame(self):
        resolution = self.ui.resolutionComboBox.itemData(self.ui.resolutionComboBox.currentIndex()).toPyObject()
        speed = self.ui.speedComboBox.itemData(self.ui.speedComboBox.currentIndex()).toPyObject()

        initialPop = float(self.ui.populationSlider.value()) / 100
        fxVol = float(self.ui.soundFxSlider.value()) / 100
        musicVol = float(self.ui.musicSlider.value()) / 100

        Config().set("game", "window-size", resolution)
        Config().set("population", "first-percentage", initialPop)
        Config().set("game", "effects-volume", fxVol)
        Config().set("game", "music-volume", musicVol)
        Config().set("game", "speed", speed)
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