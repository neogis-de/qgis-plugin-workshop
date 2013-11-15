# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BufferSelection
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from bufferselectionmaptool import BufferSelectionMapTool
import os.path


class BufferSelection:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'bufferselection_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/bufferselection/icon.png"),
            u"Select by buffer", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Buffer selection", self.action)

        self.tool = BufferSelectionMapTool(self.iface.mapCanvas())

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Buffer selection", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        distance, ok = QInputDialog.getDouble(self.iface.mainWindow(), 
                        "Distance", "Enter the radius to use, in map canvas units", min = 0, decimals = 6)
        if ok:
            self.tool.distance = distance
            self.iface.mapCanvas().setMapTool(self.tool)
