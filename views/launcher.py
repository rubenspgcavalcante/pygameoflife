import sys

from PyQt4 import QtCore, QtGui, uic

from config import Config
from resources.manager import Resource
from resources.qtlauncher import Ui_MainWindow

class Launcher(QtGui.QMainWindow):
    def __init__(self, qApp):
        QtGui.QMainWindow.__init__(self)
        self.qApp = qApp

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setDefaults()
        self.loadQss();

        self.center()
        self.show()
        self.setFixedSize(self.size());

        self.connectSignals()


    def connectSignals(self):

        self.connect(self.ui.populationSlider, QtCore.SIGNAL('valueChanged(int)'), self.updatePopLabel)

        # Connect up the buttons.
        self.connect(self.ui.submit, QtCore.SIGNAL("clicked()"), self.runGame)
        self.connect(self.ui.cancel, QtCore.SIGNAL("clicked()"), self.exit)

        #Window close button
        self.closeEvent = self.exit


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
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


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
        self.qApp.quit()
        self.hide()


    def exit(self, event=None):
        sys.exit()


    def updatePopLabel(self, value):
        self.ui.populationValueLabel.setText(str(value) + "%")