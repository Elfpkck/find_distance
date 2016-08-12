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
from qgis.utils import *
from find_distance_dialog_base import Ui_Dialog
from find_distance_engine import Engine

class FindDistance(QDialog, Ui_Dialog):

    def __init__(self, iface):
        QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)    

        self.layer1Field.setLayer(self.layerFirst())
        self.layer1Field.setCurrentIndex(0)
        self.layer2Field.setLayer(self.layerSecond())
        self.layer2Field.setCurrentIndex(0)
    
        self.show()
        
    def layerFirst(self):
        """Return the selected input layer as a QgsMapLayer instance."""
        return self.layer1.currentLayer()

    def layerSecond(self):
        """Return the selected input layer as a QgsMapLayer instance."""
        return self.layer2.currentLayer()

    def layerFirstField(self):
        """Return the name of the layer1 field."""
        return unicode(self.layer1Field.currentText())
            
    def layerSecondField(self):
        """Return the name of the layer2 field."""
        return unicode(self.layer2Field.currentText())
            
    def _accept(self):        
        layer1 = self.layerFirst()        
        layer2 = self.layerSecond()
        layer1Text = self.layerFirstField()
        layer2Text = self.layerSecondField()
        engine = Engine(
            layer1,
            layer2,
            layer1Text,
            layer2Text
        )
        engine.run()
        
    def accept(self):
        self._accept()
     