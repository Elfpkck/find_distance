# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FindDistance
                                 A QGIS plugin
 This plugin finds distances between features
                              -------------------
        begin                : 2016-07-20
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Andrey Lekarev
        email                : elfpkck@gmail.com
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

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

import resources
import find_distance_gui

class FindDistance:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
 
    def initGui(self):
        # create action 
        self.action = QAction(
            QIcon(':/plugins/FindDistance/icon.png'),
            'FindDistance',
            self.iface.mainWindow()
        )
        self.action.setWhatsThis('Create polygons and lines from vertices.')
        QObject.connect(self.action, SIGNAL('triggered()'), self.run)
        # add toolbar button and menu item
        self.iface.addVectorToolBarIcon(self.action)
        self.iface.addPluginToVectorMenu('&FindDistance', self.action)            

    def unload(self):
        """Removes the plugin menu item and icon"""
        self.iface.removePluginVectorMenu('&FindDistance',self.action)
        self.iface.removeVectorToolBarIcon(self.action)


    def run(self):
        dialog = find_distance_gui.FindDistance(self.iface)
        dialog.exec_()    
