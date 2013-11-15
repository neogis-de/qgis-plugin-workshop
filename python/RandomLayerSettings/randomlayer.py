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
from qgis.gui import *
from randomlayerdialog import RandomLayerDialog
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

    def run(self):
        dlg = RandomLayerDialog()
        dlg.exec_()
        if dlg.ok:
            try:
                self.writeLayerFile(dlg.filepath, dlg.npoints, dlg.crs)
            except Exception, e:
                print e
                self.iface.messageBar().pushMessage("Error creating layer", unicode(e),
                                              level = QgsMessageBar.CRITICAL)
                return

            self.iface.addVectorLayer(dlg.filepath, "Random points layer", "ogr")            

    def writeLayerFile(self, filepath, npoints, crs):     
        try:
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            extent = self.iface.mapCanvas().extent()            
            
            #First we generate the point coordinates
            coords = []
            for i in xrange(npoints):
                x = random.uniform(extent.xMinimum(), extent.xMaximum())
                y = random.uniform(extent.yMinimum(), extent.yMaximum())
                coords.append((x,y))
                self.iface.mainWindow().statusBar().showMessage("Points computed: " + str(i))

            #Then we write the layer             
            fields = QgsFields()            
            fields.append(QgsField("id", QVariant.Int))
            encoding = QSettings().value('/UI/encoding', 'System')
            writer = QgsVectorFileWriter(filepath, encoding, fields, QGis.WKBPoint, crs, "ESRI Shapefile")            
            projectCrs = self.iface.mapCanvas().mapRenderer().destinationCrs()
            #and we populate it, reprojecting points if needed
            crsTransform = QgsCoordinateTransform(projectCrs, crs) 
            doReproject = projectCrs.authid() != crs.authid()
            for i, coord in enumerate(coords):
                x,y = coord
                pt = QgsGeometry.fromPoint(QgsPoint(x,y))
                if doReproject:
                    pt.transform(crsTransform)
                feature = QgsFeature()
                feature.setGeometry(pt)
                feature.setAttributes([i])
                writer.addFeature(feature)        
                self.iface.mainWindow().statusBar().showMessage("Points written to layer file: " + str(i))
        finally:
            QApplication.restoreOverrideCursor()          
            self.iface.mainWindow().statusBar().clearMessage()