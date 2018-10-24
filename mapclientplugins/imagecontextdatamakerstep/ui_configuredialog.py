# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapclientplugins\imagecontextdatamakerstep\qt\configuredialog.ui'
#
# Created: Thu Oct 25 11:34:52 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QtGui.QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.configGroupBox = QtGui.QGroupBox(ConfigureDialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.identifier_label = QtGui.QLabel(self.configGroupBox)
        self.identifier_label.setObjectName("identifier_label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.identifier_label)
        self.identifier_lineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.identifier_lineEdit.setObjectName("identifier_lineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.identifier_lineEdit)
        self.framesPerSecond_label = QtGui.QLabel(self.configGroupBox)
        self.framesPerSecond_label.setObjectName("framesPerSecond_label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.framesPerSecond_label)
        self.framesPerSecond_spinBox = QtGui.QSpinBox(self.configGroupBox)
        self.framesPerSecond_spinBox.setMinimum(1)
        self.framesPerSecond_spinBox.setProperty("value", 25)
        self.framesPerSecond_spinBox.setObjectName("framesPerSecond_spinBox")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.framesPerSecond_spinBox)
        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "Configure Step", None, QtGui.QApplication.UnicodeUTF8))
        self.identifier_label.setText(QtGui.QApplication.translate("ConfigureDialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.framesPerSecond_label.setText(QtGui.QApplication.translate("ConfigureDialog", "frames per second:  ", None, QtGui.QApplication.UnicodeUTF8))

