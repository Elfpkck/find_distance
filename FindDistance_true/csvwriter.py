#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import QVariant
from qgis.core import *
from qgis.utils import *
import csv
import distance

class CSVwriter(distance.Distance):
    
    def fromFields(self):
        return [field.name() for field in self.layerFrom.pendingFields()]
        
    def toFields(self):
        return [field.name() for field in self.layerTo.pendingFields()]
