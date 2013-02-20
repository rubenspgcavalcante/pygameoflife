# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/qt/launcher.ui'
#
# Created: Tue Feb 19 21:45:14 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setBaseSize(QtCore.QSize(600, 800))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStatusTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.submit = QtGui.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(210, 240, 82, 29))
        self.submit.setMaximumSize(QtCore.QSize(90, 31))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.cancel = QtGui.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(310, 240, 82, 29))
        self.cancel.setMaximumSize(QtCore.QSize(90, 31))
        self.cancel.setAutoDefault(False)
        self.cancel.setDefault(False)
        self.cancel.setFlat(False)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 361, 100))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.form = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.form.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.form.setMargin(0)
        self.form.setObjectName(_fromUtf8("form"))
        self.populationSlider = QtGui.QSlider(self.gridLayoutWidget_2)
        self.populationSlider.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.populationSlider.sizePolicy().hasHeightForWidth())
        self.populationSlider.setSizePolicy(sizePolicy)
        self.populationSlider.setMinimumSize(QtCore.QSize(200, 0))
        self.populationSlider.setMinimum(1)
        self.populationSlider.setMaximum(50)
        self.populationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.populationSlider.setObjectName(_fromUtf8("populationSlider"))
        self.form.addWidget(self.populationSlider, 2, 1, 1, 1)
        self.populationValueLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.populationValueLabel.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.populationValueLabel.sizePolicy().hasHeightForWidth())
        self.populationValueLabel.setSizePolicy(sizePolicy)
        self.populationValueLabel.setMaximumSize(QtCore.QSize(32, 26))
        self.populationValueLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.populationValueLabel.setAutoFillBackground(False)
        self.populationValueLabel.setStyleSheet(_fromUtf8(""))
        self.populationValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.populationValueLabel.setObjectName(_fromUtf8("populationValueLabel"))
        self.form.addWidget(self.populationValueLabel, 2, 2, 1, 1)
        self.resolutionComboBox = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.resolutionComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resolutionComboBox.setAutoFillBackground(False)
        self.resolutionComboBox.setStyleSheet(_fromUtf8(""))
        self.resolutionComboBox.setObjectName(_fromUtf8("resolutionComboBox"))
        self.form.addWidget(self.resolutionComboBox, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.form.addWidget(self.label, 2, 0, 1, 1)
        self.resolutionLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.resolutionLabel.setObjectName(_fromUtf8("resolutionLabel"))
        self.form.addWidget(self.resolutionLabel, 0, 0, 1, 1)
        self.speedComboBox = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.speedComboBox.setObjectName(_fromUtf8("speedComboBox"))
        self.form.addWidget(self.speedComboBox, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.form.addWidget(self.label_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.submit, self.cancel)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyGame of Life", None, QtGui.QApplication.UnicodeUTF8))
        self.submit.setText(QtGui.QApplication.translate("MainWindow", "ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.populationValueLabel.setText(QtGui.QApplication.translate("MainWindow", "1%", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Initial Population", None, QtGui.QApplication.UnicodeUTF8))
        self.resolutionLabel.setText(QtGui.QApplication.translate("MainWindow", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Speed", None, QtGui.QApplication.UnicodeUTF8))

