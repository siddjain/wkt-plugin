# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WKTBulkLoader
                                 A QGIS plugin
 A plugin to bulk load WKT files
                             -------------------
        begin                : 2015-11-03
        copyright            : (C) 2015 by Siddharth Jain
        email                : siddjain@live.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WKTBulkLoader class from file WKTBulkLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from wkt_bulk_loader import WKTBulkLoader
    return WKTBulkLoader(iface)
