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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load LayerList class from file LayerList
    from layerlist import LayerList
    return LayerList(iface)
