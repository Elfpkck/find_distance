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
from find_distance_dialog import FindDistanceDialog
import os.path
import resources
import distance, csvwriter

class FindDistance:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'FindDistance_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = FindDistanceDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Find distance')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'FindDistance')
        self.toolbar.setObjectName(u'FindDistance')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('FindDistance', message)

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
 
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToVectorMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/FindDistance/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u''),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginVectorMenu(
                self.tr(u'&Find distance'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        layers = QgsMapLayerRegistry.instance().mapLayers().values()
        for layer in layers:
            self.dlg.layerFrom.addItem(layer.name(), layer)         
            self.dlg.layerTo.addItem(layer.name(), layer)         
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            layerFromIndex = self.dlg.layerFrom.currentIndex()
            layerFrom = self.dlg.layerFrom.itemData(layerFromIndex)
            
            layerToIndex = self.dlg.layerTo.currentIndex()
            layerTo = self.dlg.layerTo.itemData(layerToIndex)
            a = distance.Distance(layerFrom, layerTo)
            a.check()
            a.find_dist()
            
            for layer in layers:
                self.dlg.layerFrom.addItem(layer.name(), layer)             
                b = csvwriter.CSVwriter(layerFrom, layerTo)
                print b.toFields(), b.fromFields()

        self.dlg.layerFrom.clear()
        self.dlg.layerTo.clear()