import sys

from PyQt4 import QtCore, QtGui, uic

from config import Config
from resources.manager import Resource

class Launcher(QtGui.QMainWindow):
    def __init__(self, qApp):
        QtGui.QMainWindow.__init__(self)
        self.qApp = qApp

        # Set up the user interface from Designer.
        self.ui = Resource.getQtUI("launcher")
        self.setDefaults()

        self.center()
        self.ui.show()
        self.ui.setFixedSize(self.ui.size());

        self.connect(self.ui.populationSlider, QtCore.SIGNAL('valueChanged(int)'), self.updatePopLabel)

        # Connect up the buttons.
        self.connect(self.ui.submit, QtCore.SIGNAL("clicked()"), self.runGame)
        self.connect(self.ui.cancel, QtCore.SIGNAL("clicked()"), self.exit)

        #Window close button
        self.ui.closeEvent = self.exit

    def center(self):
        qr = self.ui.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.ui.move(qr.topLeft())

    def setDefaults(self):
        for item in Config().get("setup", "resolutions"):
            text = str(item[0]) + " x " + str(item[1])
            self.ui.resolutionComboBox.addItem(text, item)

        for speed in Config().get("setup", "speed"):
            value = Config().get("setup", "speed")[speed]
            self.ui.speedComboBox.addItem(speed, value)

    def runGame(self):
        resolution = self.ui.resolutionComboBox.itemData(self.ui.resolutionComboBox.currentIndex()).toPyObject()
        speed = self.ui.speedComboBox.itemData(self.ui.speedComboBox.currentIndex()).toPyObject()
        initialPop = float(self.ui.populationSlider.value())/100

        Config().set("game", "window-size", resolution)
        Config().set("population", "first-percentage", initialPop)
        self.ui.destroy()
        self.qApp.quit()

    def exit(self, event=None):
        sys.exit()

    def updatePopLabel(self, value):
        self.ui.populationValueLabel.setText(str(value) + "%")