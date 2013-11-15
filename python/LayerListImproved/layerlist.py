# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LayerList
                                 A QGIS plugin
 Shows a list of layers
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
import os.path


class LayerList:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'layerlist_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        # Create action that will start plugin configuration
        self.showRasterAction = QAction(
            QIcon(":/plugins/layerlistplugin/raster_icon.png"),
            u"Show list of raster layers", self.iface.mainWindow())        
        self.showRasterAction.triggered.connect(self.showRaster)        
        self.iface.addToolBarIcon(self.showRasterAction)
        self.iface.addPluginToMenu(u"&Layer list", self.showRasterAction)

        self.showVectorAction = QAction(
            QIcon(":/plugins/layerlistplugin/vector_icon.png"),
            u"Show list of vector layers", self.iface.mainWindow())        
        self.showVectorAction.triggered.connect(self.showVector)        
        self.iface.addToolBarIcon(self.showVectorAction)
        self.iface.addPluginToMenu(u"&Layer list", self.showVectorAction)


    def unload(self):
        self.iface.removePluginMenu(u"&Layer list", self.showRasterAction)
        self.iface.removePluginMenu(u"&Layer list", self.showVectorAction)
        self.iface.removeToolBarIcon(self.showRasterAction)
        self.iface.removeToolBarIcon(self.showVectorAction)

    def showVector(self):
        layers = self.iface.legendInterface().layers()
        vectorLayers = [layer for layer in layers if layer.type() == QgsMapLayer.VectorLayer]
        TYPES = ['Point', 'Line', 'Polygon', 'Unknown', 'No geometry']
        s = '\n*'.join(['{}-{} ({})'.format(layer.name(), TYPES[layer.geometryType()], layer.crs().authid()) for layer in vectorLayers])
        QMessageBox.information(self.iface.mainWindow(), "Vector layer list", s)

    def showRaster(self):
        layers = self.iface.legendInterface().layers()
        rasterLayers = [layer for layer in layers if layer.type() == QgsMapLayer.RasterLayer]
        s = "\n*".join(['{} ({})'.format(layer.name(), layer.crs().authid()) for layer in rasterLayers])
        QMessageBox.information(self.iface.mainWindow(), "Raster layer list", s)        