# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BufferSelectionDialog
                                 A QGIS plugin
 Select features using a fixed radius
                             -------------------
        begin                : 2013-11-15
        copyright            : (C) 2013 by Boundless
        email                : volaya@boundlessgeo.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from qgis.core import *
from ui_randomlayer import Ui_RandomLayer
# create the dialog for zoom to point


class RandomLayerDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_RandomLayer()
        self.ui.setupUi(self)
        self.ok = False

    def accept(self):
        self.filepath = self.ui.txtFilepath.text()
        authid = self.ui.txtCrs.text()
        self.crs = QgsCoordinateReferenceSystem(authid)
        if not self.crs.isValid():
            self.setYellowBackground(self.ui.txtCrs)
            return
        try:
            self.npoints = int(self.ui.txtNPoints.text())
        except ValueError:
            self.setYellowBackground(self.ui.txtNPoints)
            return
        if self.npoints < 1:
            self.setYellowBackground(self.ui.txtNPoints)
            return

        self.ok = True      
        QtGui.QDialog.accept(self)        
        
    def reject(self):       
        self.ok = False
        QtGui.QDialog.reject(self)   

    def setYellowBackground(self, widget):
        widget.setStyleSheet("QLineEdit{background: yellow}")       