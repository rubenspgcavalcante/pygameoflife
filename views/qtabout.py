# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/qt/about.ui'
#
# Created: Wed May  8 21:11:24 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_aboutWindow(object):
    def setupUi(self, aboutWindow):
        aboutWindow.setObjectName(_fromUtf8("aboutWindow"))
        aboutWindow.resize(500, 275)
        self.label_2 = QtGui.QLabel(aboutWindow)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 321, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.version = QtGui.QLabel(aboutWindow)
        self.version.setGeometry(QtCore.QRect(303, 10, 61, 17))
        self.version.setObjectName(_fromUtf8("version"))
        self.label = QtGui.QLabel(aboutWindow)
        self.label.setGeometry(QtCore.QRect(140, 10, 162, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(aboutWindow)
        self.label_4.setGeometry(QtCore.QRect(120, 60, 301, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textBrowser = QtGui.QTextBrowser(aboutWindow)
        self.textBrowser.setGeometry(QtCore.QRect(20, 90, 471, 161))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(aboutWindow)
        QtCore.QMetaObject.connectSlotsByName(aboutWindow)

    def retranslateUi(self, aboutWindow):
        aboutWindow.setWindowTitle(_translate("aboutWindow", "Form", None))
        self.label_2.setText(_translate("aboutWindow", "Author: Rubens Pinheiro Gonçalves Cavalcante", None))
        self.version.setText(_translate("aboutWindow", "VERSION", None))
        self.label.setText(_translate("aboutWindow", "Pygame of Life - Version", None))
        self.label_4.setText(_translate("aboutWindow", "Email: rubenspgcavalvante@gmail.com", None))
        self.textBrowser.setHtml(_translate("aboutWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This game is based in the <span style=\" font-style:italic;\">\'Game of Life\' </span>or simply <span style=\" font-style:italic;\">\'Life\'</span> proposed by John Conway in a scientific article in 1970. It\'s a celular automaton wich follows a few rules:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">For a space that is \'populated\':</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-style:italic;\">- Each cell with one or no neighbors dies, as if by loneliness. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-style:italic;\">- Each cell with four or more neighbors dies, as if by overpopulation. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-style:italic;\">- Each cell with two or three neighbors survives. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">For a space that is \'empty\' or \'unpopulated\'</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-style:italic;\">- Each cell with three neighbors becomes populated.</span></p></body></html>", None))

