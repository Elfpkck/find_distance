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
from qgis.core import *
#import csv_unicode
import csv

class Engine(object):
    """Data processing for FindDistance."""

    def __init__(self, layer1, layer2, layer1Text, layer2Text):
        self.layer1 = layer1
        self.layer2 = layer2
        self.layer1Text = layer1Text
        self.layer2Text = layer2Text
        
        self.layers = [self.layer1, self.layer2]
        self.layersText = [self.layer1Text, self.layer2Text]
        
    def run(self):
        #self.attr(self.layer1, self.layer1Text)
        #self.attr(self.layer2, self.layer2Text)
        map(self.attr, self.layers, self.layersText)
        self.writeCSV()
        
    def attr(self, layer, layerText):
        temp_lst = []
        #for field in layer.pendingFields():
            #print field.name(), field.typeName()
        for item in layer.getFeatures():
            for field in layer.pendingFields(): 
                try:
                    if field.name() == layerText and field.typeName() == 'String':
                        temp_lst.append(item[layerText])
                    else:
                        temp_lst.append(item[layerText])                    
                except AttributeError:
                    pass
        return temp_lst
  
    def dist(self, layer1, layer2):   
        for item1 in layer1.getFeatures():
            for item2 in layer2.getFeatures():
                distance = item1.geometry().distance(item2.geometry())
                distance = int(distance)
                print distance
                
    def writeCSV(self):
        with open("D:\distances.csv", "wb") as output_file:
            wrtr = csv.writer(output_file)
            print self.layer1.objectName
            print self.layer2.FileName
            wrtr.writerows([
            [self.layer1],
            self.attr(self.layer1, self.layer1Text),          
            ])    