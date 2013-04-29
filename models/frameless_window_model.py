from PyQt4 import QtGui, QtCore
import sys
from views.qtlauncher import Ui_MainWindow
from helpers.qtresources import *


class FramelessWindowModel(QtGui.QMainWindow):
    """
    Custom frameless window
    """
    def __init__(self):
        self.qApp = QtGui.QApplication(sys.argv)
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.connect(self.ui.customTitleBar, QtCore.SIGNAL('mouseMove()'), self.mouseMoveEvent)
        self.connect(self.ui.customTitleBar, QtCore.SIGNAL('mousePress()'), self.mousePressEvent)
        self.connect(self.ui.customTitleBar, QtCore.SIGNAL('mouseRelease()'), self.mouseReleaseEvent)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.DragMoveCursor))
            self.ui.customTitleBar.moving = True
            self.ui.customTitleBar.offset = event.pos()

    def mouseMoveEvent(self, event):
        if hasattr(self.ui.customTitleBar, "moving") and self.ui.customTitleBar.moving:
            self.move(event.globalPos() - self.ui.customTitleBar.offset)

    def mouseReleaseEvent(self, event):
        QtGui.QApplication.restoreOverrideCursor()

    def loadQss(self, filename):
        """
        Loads a qcss filed avalible in qrc virtual env
        :param filename: String Name of the file
        :return: Boolean Loaded sucefully or not
        """
        css = QtCore.QFile(':/'+filename)
        css.open(QtCore.QIODevice.ReadOnly)

        if css.isOpen():
            self.setStyleSheet(QtCore.QVariant(css.readAll()).toString())
            css.close()
            return True
        else:
            return False