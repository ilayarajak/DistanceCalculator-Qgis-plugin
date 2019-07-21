# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DistanceCalculator
                                 A QGIS plugin
 This plugin helps to calculate the distance between two points on the Earth
                             -------------------
        begin                : 2019-07-19
        copyright            : (C) 2019 by ilayaraja
        email                : ilayaraja22@gmail.com
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
    """Load DistanceCalculator class from file DistanceCalculator.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .distance_calculator import DistanceCalculator
    return DistanceCalculator(iface)
