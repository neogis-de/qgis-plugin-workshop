# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_randomlayer.ui'
#
# Created: Fri Nov 15 12:21:44 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_RandomLayer(object):
    def setupUi(self, RandomLayer):
        RandomLayer.setObjectName(_fromUtf8("RandomLayer"))
        RandomLayer.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(RandomLayer)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(RandomLayer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), RandomLayer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), RandomLayer.reject)
        QtCore.QMetaObject.connectSlotsByName(RandomLayer)

    def retranslateUi(self, RandomLayer):
        RandomLayer.setWindowTitle(_translate("RandomLayer", "RandomLayer", None))

