# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_randomlayer.ui'
#
# Created: Fri Nov 15 14:00:41 2013
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
        RandomLayer.resize(396, 178)
        self.verticalLayout = QtGui.QVBoxLayout(RandomLayer)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(RandomLayer)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.txtCrs = QtGui.QLineEdit(RandomLayer)
        self.txtCrs.setObjectName(_fromUtf8("txtCrs"))
        self.verticalLayout.addWidget(self.txtCrs)
        self.label_2 = QtGui.QLabel(RandomLayer)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.txtNPoints = QtGui.QLineEdit(RandomLayer)
        self.txtNPoints.setObjectName(_fromUtf8("txtNPoints"))
        self.verticalLayout.addWidget(self.txtNPoints)
        self.label_3 = QtGui.QLabel(RandomLayer)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.txtFilepath = QtGui.QLineEdit(RandomLayer)
        self.txtFilepath.setObjectName(_fromUtf8("txtFilepath"))
        self.verticalLayout.addWidget(self.txtFilepath)
        self.buttonBox = QtGui.QDialogButtonBox(RandomLayer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(RandomLayer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), RandomLayer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), RandomLayer.reject)
        QtCore.QMetaObject.connectSlotsByName(RandomLayer)

    def retranslateUi(self, RandomLayer):
        RandomLayer.setWindowTitle(_translate("RandomLayer", "RandomLayer", None))
        self.label.setText(_translate("RandomLayer", "Crs", None))
        self.label_2.setText(_translate("RandomLayer", "Number of points", None))
        self.label_3.setText(_translate("RandomLayer", "Filepath", None))

