# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'find_distance_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(356, 401)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 133))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.layer1 = gui.QgsMapLayerComboBox(Dialog)
        self.layer1.setGeometry(QtCore.QRect(70, 200, 160, 27))
        self.layer1.setObjectName(_fromUtf8("layer1"))
        self.layer1Field = gui.QgsFieldComboBox(Dialog)
        self.layer1Field.setGeometry(QtCore.QRect(70, 240, 160, 27))
        self.layer1Field.setObjectName(_fromUtf8("layer1Field"))
        self.layer2Field = gui.QgsFieldComboBox(Dialog)
        self.layer2Field.setGeometry(QtCore.QRect(70, 320, 160, 27))
        self.layer2Field.setObjectName(_fromUtf8("layer2Field"))
        self.layer2 = gui.QgsMapLayerComboBox(Dialog)
        self.layer2.setGeometry(QtCore.QRect(70, 280, 160, 27))
        self.layer2.setObjectName(_fromUtf8("layer2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.layer1, QtCore.SIGNAL(_fromUtf8("layerChanged(QgsMapLayer*)")), self.layer1Field.setLayer)
        QtCore.QObject.connect(self.layer2, QtCore.SIGNAL(_fromUtf8("layerChanged(QgsMapLayer*)")), self.layer2Field.setLayer)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "Select layer from", None))
        self.label.setText(_translate("Dialog", "Select  layer to", None))

from qgis import gui