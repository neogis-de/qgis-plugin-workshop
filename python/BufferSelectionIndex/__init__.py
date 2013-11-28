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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load BufferSelection class from file BufferSelection
    from bufferselection import BufferSelection
    return BufferSelection(iface)
