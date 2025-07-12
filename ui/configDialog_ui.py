# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        if not ConfigDialog.objectName():
            ConfigDialog.setObjectName(u"ConfigDialog")
        ConfigDialog.resize(400, 463)
        self.verticalLayout = QVBoxLayout(ConfigDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(ConfigDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 356, 396))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.TxtKordataUser = QLineEdit(self.groupBox)
        self.TxtKordataUser.setObjectName(u"TxtKordataUser")

        self.verticalLayout_4.addWidget(self.TxtKordataUser)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.TxtKordataPass = QLineEdit(self.groupBox)
        self.TxtKordataPass.setObjectName(u"TxtKordataPass")

        self.verticalLayout_5.addWidget(self.TxtKordataPass)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CheckAutologin = QCheckBox(self.groupBox)
        self.CheckAutologin.setObjectName(u"CheckAutologin")

        self.horizontalLayout.addWidget(self.CheckAutologin)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.BtnConfigDiagSaveKordataInfo = QPushButton(self.groupBox)
        self.BtnConfigDiagSaveKordataInfo.setObjectName(u"BtnConfigDiagSaveKordataInfo")

        self.horizontalLayout.addWidget(self.BtnConfigDiagSaveKordataInfo)

        self.BtnConfigDiagEditKordataInfo = QPushButton(self.groupBox)
        self.BtnConfigDiagEditKordataInfo.setObjectName(u"BtnConfigDiagEditKordataInfo")

        self.horizontalLayout.addWidget(self.BtnConfigDiagEditKordataInfo)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 20, 78, 20))
        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 60, 78, 20))

        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(ConfigDialog)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ConfigDialog)
    # setupUi

    def retranslateUi(self, ConfigDialog):
        ConfigDialog.setWindowTitle(QCoreApplication.translate("ConfigDialog", u"Configuraci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ConfigDialog", u"General", None))
        self.groupBox.setTitle(QCoreApplication.translate("ConfigDialog", u"Informaci\u00f3n inicio Kordata", None))
        self.label.setText(QCoreApplication.translate("ConfigDialog", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("ConfigDialog", u"Contrase\u00f1a", None))
        self.CheckAutologin.setText(QCoreApplication.translate("ConfigDialog", u"Autologin", None))
        self.BtnConfigDiagSaveKordataInfo.setText(QCoreApplication.translate("ConfigDialog", u"Guardar info", None))
        self.BtnConfigDiagEditKordataInfo.setText(QCoreApplication.translate("ConfigDialog", u"Editar Info", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ConfigDialog", u"Funcionalidad", None))
        self.checkBox.setText(QCoreApplication.translate("ConfigDialog", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("ConfigDialog", u"CheckBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ConfigDialog", u"Kordata", None))
    # retranslateUi

