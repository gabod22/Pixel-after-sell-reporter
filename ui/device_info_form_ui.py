# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'device_info_form.ui'
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
    QGridLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_create_device_form(object):
    def setupUi(self, create_device_form):
        if not create_device_form.objectName():
            create_device_form.setObjectName(u"create_device_form")
        create_device_form.resize(492, 340)
        self.gridLayout = QGridLayout(create_device_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_7 = QLineEdit(create_device_form)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 4, 1, 1, 1)

        self.label_5 = QLabel(create_device_form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 4, 2, 1, 1)

        self.label_8 = QLabel(create_device_form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 7, 2, 1, 1)

        self.label = QLabel(create_device_form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.comboBox_2 = QComboBox(create_device_form)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 7, 3, 1, 1)

        self.label_7 = QLabel(create_device_form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(create_device_form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 4, 3, 1, 1)

        self.lineEdit_4 = QLineEdit(create_device_form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 7, 1, 1, 1)

        self.spinBox = QSpinBox(create_device_form)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 11, 1, 1, 1)

        self.label_4 = QLabel(create_device_form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.label_6 = QLabel(create_device_form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 11, 0, 1, 1)

        self.label_9 = QLabel(create_device_form)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(22)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QFrame.Shape.Box)
        self.label_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 4)

        self.label_2 = QLabel(create_device_form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 11, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(create_device_form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 3, 1, 1)

        self.label_3 = QLabel(create_device_form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(create_device_form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.comboBox = QComboBox(create_device_form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 11, 3, 1, 1)

        self.label_10 = QLabel(create_device_form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_10, 13, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(create_device_form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 13, 1, 1, 1)

        self.label_11 = QLabel(create_device_form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_11, 13, 2, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(create_device_form)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.gridLayout.addWidget(self.plainTextEdit_2, 13, 3, 1, 1)

        self.BtnSaveDevice = QPushButton(create_device_form)
        self.BtnSaveDevice.setObjectName(u"BtnSaveDevice")

        self.gridLayout.addWidget(self.BtnSaveDevice, 14, 3, 1, 1)


        self.retranslateUi(create_device_form)

        QMetaObject.connectSlotsByName(create_device_form)
    # setupUi

    def retranslateUi(self, create_device_form):
        create_device_form.setWindowTitle(QCoreApplication.translate("create_device_form", u"Crear dispositivo", None))
        self.lineEdit_7.setText("")
        self.label_5.setText(QCoreApplication.translate("create_device_form", u"Num de serie", None))
        self.label_8.setText(QCoreApplication.translate("create_device_form", u"Respaldo", None))
        self.label.setText(QCoreApplication.translate("create_device_form", u"Modelo", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("create_device_form", u"SI", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("create_device_form", u"NO", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("create_device_form", u"REVISAR", None))

        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("create_device_form", u"Seleccionar", None))
        self.label_7.setText(QCoreApplication.translate("create_device_form", u"Tel\u00e9fono", None))
        self.label_4.setText(QCoreApplication.translate("create_device_form", u"Contrase\u00f1a", None))
        self.label_6.setText(QCoreApplication.translate("create_device_form", u"Dias de diag", None))
        self.label_9.setText(QCoreApplication.translate("create_device_form", u"Crear dispositivo en Kordata", None))
        self.label_2.setText(QCoreApplication.translate("create_device_form", u"Garrantia", None))
        self.lineEdit_3.setInputMask(QCoreApplication.translate("create_device_form", u"9999999999", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("create_device_form", u"1234567890", None))
        self.label_3.setText(QCoreApplication.translate("create_device_form", u"Cliente", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("create_device_form", u"SI", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("create_device_form", u"NO", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("create_device_form", u"REVISAR", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("create_device_form", u"Seleccionar", None))
        self.label_10.setText(QCoreApplication.translate("create_device_form", u"Problema", None))
        self.label_11.setText(QCoreApplication.translate("create_device_form", u"Comentario", None))
        self.BtnSaveDevice.setText(QCoreApplication.translate("create_device_form", u"Guardar Dispositivo", None))
    # retranslateUi

