# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QSizePolicy, QSpinBox, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.identifier_label = QLabel(self.configGroupBox)
        self.identifier_label.setObjectName(u"identifier_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.identifier_label)

        self.identifier_lineEdit = QLineEdit(self.configGroupBox)
        self.identifier_lineEdit.setObjectName(u"identifier_lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.identifier_lineEdit)

        self.framesPerSecond_label = QLabel(self.configGroupBox)
        self.framesPerSecond_label.setObjectName(u"framesPerSecond_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.framesPerSecond_label)

        self.framesPerSecond_spinBox = QSpinBox(self.configGroupBox)
        self.framesPerSecond_spinBox.setObjectName(u"framesPerSecond_spinBox")
        self.framesPerSecond_spinBox.setMinimum(1)
        self.framesPerSecond_spinBox.setValue(25)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.framesPerSecond_spinBox)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Step", None))
        self.configGroupBox.setTitle("")
        self.identifier_label.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.framesPerSecond_label.setText(QCoreApplication.translate("ConfigureDialog", u"frames per second:  ", None))
    # retranslateUi

