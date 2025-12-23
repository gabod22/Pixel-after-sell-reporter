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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDialog, QGroupBox, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

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
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.CbxAgents = QComboBox(self.groupBox_3)
        self.CbxAgents.setObjectName(u"CbxAgents")
        self.CbxAgents.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.CbxAgents)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 301, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 356, 366))
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

        self.ChkAutoLogin = QCheckBox(self.groupBox)
        self.ChkAutoLogin.setObjectName(u"ChkAutoLogin")

        self.verticalLayout_6.addWidget(self.ChkAutoLogin)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.dateKordataStartDate = QDateEdit(self.groupBox_2)
        self.dateKordataStartDate.setObjectName(u"dateKordataStartDate")

        self.verticalLayout_5.addWidget(self.dateKordataStartDate)

        self.ChkDialogCreateOS = QCheckBox(self.groupBox_2)
        self.ChkDialogCreateOS.setObjectName(u"ChkDialogCreateOS")

        self.verticalLayout_5.addWidget(self.ChkDialogCreateOS)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.BtnSaveConfig = QPushButton(ConfigDialog)
        self.BtnSaveConfig.setObjectName(u"BtnSaveConfig")

        self.verticalLayout.addWidget(self.BtnSaveConfig)


        self.retranslateUi(ConfigDialog)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ConfigDialog)
    # setupUi

    def retranslateUi(self, ConfigDialog):
        ConfigDialog.setWindowTitle(QCoreApplication.translate("ConfigDialog", u"Configuraci\u00f3n", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ConfigDialog", u"Agente por defecto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ConfigDialog", u"General", None))
        self.groupBox.setTitle(QCoreApplication.translate("ConfigDialog", u"Informaci\u00f3n inicio Kordata", None))
        self.label.setText(QCoreApplication.translate("ConfigDialog", u"Correo Kordata", None))
        self.ChkAutoLogin.setText(QCoreApplication.translate("ConfigDialog", u"Cerrar sesiones automaticamente", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ConfigDialog", u"Funcionalidad", None))
        self.label_2.setText(QCoreApplication.translate("ConfigDialog", u"Fecha inicio de extraci\u00f3n de datos", None))
        self.ChkDialogCreateOS.setText(QCoreApplication.translate("ConfigDialog", u"Solicitar creaci\u00f3n de OS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ConfigDialog", u"Kordata", None))
        self.BtnSaveConfig.setText(QCoreApplication.translate("ConfigDialog", u"Guardar", None))
    # retranslateUi

