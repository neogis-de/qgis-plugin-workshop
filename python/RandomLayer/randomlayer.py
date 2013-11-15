# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RandomLayer
                                 A QGIS plugin
 Create a random points layer
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
import random


class RandomLayer:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'randomlayer_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/randomlayer/icon.png"),
            u"Create random layer...", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Random layer", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Random layer", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        npoints, ok = QInputDialog.getInt(self.iface.mainWindow(), "Number of points", "Enter number of points to add to layer", min = 1)
        if ok:
            #First we generate the point coordinates
            extent = self.iface.mapCanvas().extent()            
            coords = []
            for i in xrange(npoints):
                x = random.uniform(extent.xMinimum(), extent.xMaximum())
                y = random.uniform(extent.yMinimum(), extent.yMaximum())
                coords.append((x,y))
            
            #Then we create the layer
            uri = 'Point?crs=epsg:4326&field=id:integer'
            memLayer = QgsVectorLayer(uri, "Random points layer", 'memory')
            writer = memLayer.dataProvider()            

            features = []
            #and we populate it
            for i, coord in enumerate(coords):
                x,y = coord
                feature = QgsFeature()
                feature.setGeometry(QgsGeometry.fromPoint(QgsPoint(x,y)))
                feature.setAttributes([i])
                features.append(feature)

            writer.addFeatures(features)


            #And then we add the layer to the current project
            QgsMapLayerRegistry.instance().addMapLayers([memLayer])