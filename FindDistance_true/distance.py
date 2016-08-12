#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import QVariant
from qgis.core import *
from qgis.utils import *

class Distance():
       
    def __init__(self, layerFrom, layerTo):
        self.layerFrom = layerFrom
        self.layerTo = layerTo
        
    def check(self):   
        for point in self.layerTo.getFeatures():
            try:
                point['dist']
                break
            except KeyError:
                self.layerTo.dataProvider().addAttributes([QgsField("dist", QVariant.Int)])
                break
                
    def find_dist(self):   
        with edit(self.layerTo): 
            for line in self.layerFrom.getFeatures():
                for point in self.layerTo.getFeatures():
                    distance = line.geometry().distance(point.geometry())
                    print distance
                    distance = int(distance)
                    point['dist'] = distance
                    self.layerTo.updateFeature(point)

                    