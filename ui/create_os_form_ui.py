# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_os_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_create_os_form(object):
    def setupUi(self, create_os_form):
        if not create_os_form.objectName():
            create_os_form.setObjectName(u"create_os_form")
        create_os_form.resize(548, 594)
        self.verticalLayout_5 = QVBoxLayout(create_os_form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(create_os_form)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(22)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QFrame.Shape.Box)
        self.label_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_9)

        self.groupBox_3 = QGroupBox(create_os_form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.TxtClientName = QLineEdit(self.groupBox_3)
        self.TxtClientName.setObjectName(u"TxtClientName")

        self.horizontalLayout.addWidget(self.TxtClientName)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.TxtClientPhone = QLineEdit(self.groupBox_3)
        self.TxtClientPhone.setObjectName(u"TxtClientPhone")

        self.horizontalLayout.addWidget(self.TxtClientPhone)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(create_os_form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.CbxDeviceWarranty = QComboBox(self.groupBox)
        self.CbxDeviceWarranty.addItem("")
        self.CbxDeviceWarranty.addItem("")
        self.CbxDeviceWarranty.addItem("")
        self.CbxDeviceWarranty.setObjectName(u"CbxDeviceWarranty")

        self.gridLayout_2.addWidget(self.CbxDeviceWarranty, 2, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.TxtDevicePass = QLineEdit(self.groupBox)
        self.TxtDevicePass.setObjectName(u"TxtDevicePass")

        self.gridLayout_2.addWidget(self.TxtDevicePass, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 2, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.SpinDeviceDaigDays = QSpinBox(self.groupBox)
        self.SpinDeviceDaigDays.setObjectName(u"SpinDeviceDaigDays")

        self.gridLayout_2.addWidget(self.SpinDeviceDaigDays, 2, 1, 1, 1)

        self.TxtDeviceSerial = QLineEdit(self.groupBox)
        self.TxtDeviceSerial.setObjectName(u"TxtDeviceSerial")

        self.gridLayout_2.addWidget(self.TxtDeviceSerial, 0, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)

        self.CbxDeviceBackup = QComboBox(self.groupBox)
        self.CbxDeviceBackup.addItem("")
        self.CbxDeviceBackup.addItem("")
        self.CbxDeviceBackup.addItem("")
        self.CbxDeviceBackup.setObjectName(u"CbxDeviceBackup")

        self.gridLayout_2.addWidget(self.CbxDeviceBackup, 1, 3, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)

        self.TxtDeviceModel = QLineEdit(self.groupBox)
        self.TxtDeviceModel.setObjectName(u"TxtDeviceModel")

        self.gridLayout_2.addWidget(self.TxtDeviceModel, 0, 1, 1, 1)

        self.TxtDevicePeripherials = QLineEdit(self.groupBox)
        self.TxtDevicePeripherials.setObjectName(u"TxtDevicePeripherials")

        self.gridLayout_2.addWidget(self.TxtDevicePeripherials, 3, 3, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_15, 3, 2, 1, 1)

        self.TxtDeviceProblem = QPlainTextEdit(self.groupBox)
        self.TxtDeviceProblem.setObjectName(u"TxtDeviceProblem")

        self.gridLayout_2.addWidget(self.TxtDeviceProblem, 4, 1, 1, 3)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(create_os_form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_12)

        self.TxtOsEjecutive = QLineEdit(self.groupBox_2)
        self.TxtOsEjecutive.setObjectName(u"TxtOsEjecutive")

        self.verticalLayout.addWidget(self.TxtOsEjecutive)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_14)

        self.SpinOsProcessDays = QSpinBox(self.groupBox_2)
        self.SpinOsProcessDays.setObjectName(u"SpinOsProcessDays")

        self.verticalLayout_2.addWidget(self.SpinOsProcessDays)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_3.addWidget(self.label_13)

        self.TxtOsSolution = QPlainTextEdit(self.groupBox_2)
        self.TxtOsSolution.setObjectName(u"TxtOsSolution")

        self.verticalLayout_3.addWidget(self.TxtOsSolution)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.BtnCreateOs = QPushButton(create_os_form)
        self.BtnCreateOs.setObjectName(u"BtnCreateOs")

        self.verticalLayout_5.addWidget(self.BtnCreateOs)


        self.retranslateUi(create_os_form)

        QMetaObject.connectSlotsByName(create_os_form)
    # setupUi

    def retranslateUi(self, create_os_form):
        create_os_form.setWindowTitle(QCoreApplication.translate("create_os_form", u"Crear dispositivo", None))
        self.label_9.setText(QCoreApplication.translate("create_os_form", u"Crear Orden de Servicio en Kordata", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("create_os_form", u"Cliente", None))
        self.label_3.setText(QCoreApplication.translate("create_os_form", u"Cliente", None))
        self.label_7.setText(QCoreApplication.translate("create_os_form", u"Tel\u00e9fono", None))
        self.TxtClientPhone.setInputMask(QCoreApplication.translate("create_os_form", u"9999999999", None))
        self.TxtClientPhone.setPlaceholderText(QCoreApplication.translate("create_os_form", u"1234567890", None))
        self.groupBox.setTitle(QCoreApplication.translate("create_os_form", u"Informaci\u00f3n del dispositivo", None))
        self.label.setText(QCoreApplication.translate("create_os_form", u"Modelo", None))
        self.CbxDeviceWarranty.setItemText(0, QCoreApplication.translate("create_os_form", u"SI", None))
        self.CbxDeviceWarranty.setItemText(1, QCoreApplication.translate("create_os_form", u"NO", None))
        self.CbxDeviceWarranty.setItemText(2, QCoreApplication.translate("create_os_form", u"REVISAR", None))

        self.CbxDeviceWarranty.setPlaceholderText(QCoreApplication.translate("create_os_form", u"Seleccionar", None))
        self.label_4.setText(QCoreApplication.translate("create_os_form", u"Contrase\u00f1a", None))
        self.label_5.setText(QCoreApplication.translate("create_os_form", u"Num de serie", None))
        self.label_2.setText(QCoreApplication.translate("create_os_form", u"Garrantia", None))
        self.label_6.setText(QCoreApplication.translate("create_os_form", u"Dias de diag", None))
        self.label_8.setText(QCoreApplication.translate("create_os_form", u"Respaldo", None))
        self.CbxDeviceBackup.setItemText(0, QCoreApplication.translate("create_os_form", u"SI", None))
        self.CbxDeviceBackup.setItemText(1, QCoreApplication.translate("create_os_form", u"NO", None))
        self.CbxDeviceBackup.setItemText(2, QCoreApplication.translate("create_os_form", u"REVISAR", None))

        self.CbxDeviceBackup.setPlaceholderText(QCoreApplication.translate("create_os_form", u"Seleccionar", None))
        self.label_10.setText(QCoreApplication.translate("create_os_form", u"Problema", None))
        self.TxtDeviceModel.setText("")
        self.label_15.setText(QCoreApplication.translate("create_os_form", u"Perifericos", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("create_os_form", u"Orden de servicio", None))
        self.label_12.setText(QCoreApplication.translate("create_os_form", u"Ejecutvio", None))
        self.label_14.setText(QCoreApplication.translate("create_os_form", u"Dias de procesamiento", None))
        self.label_13.setText(QCoreApplication.translate("create_os_form", u"Soluci\u00f3n", None))
        self.BtnCreateOs.setText(QCoreApplication.translate("create_os_form", u"Guardar Dispositivo", None))
    # retranslateUi

