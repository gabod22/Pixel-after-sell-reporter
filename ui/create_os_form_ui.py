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
    QSpinBox, QWidget)

class Ui_create_os_form(object):
    def setupUi(self, create_os_form):
        if not create_os_form.objectName():
            create_os_form.setObjectName(u"create_os_form")
        create_os_form.resize(492, 506)
        self.label_9 = QLabel(create_os_form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(9, 9, 453, 42))
        font = QFont()
        font.setPointSize(22)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QFrame.Shape.Box)
        self.label_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.BtnSaveDevice = QPushButton(create_os_form)
        self.BtnSaveDevice.setObjectName(u"BtnSaveDevice")
        self.BtnSaveDevice.setGeometry(QRect(9, 473, 111, 24))
        self.groupBox = QGroupBox(create_os_form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 120, 474, 231))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.label_11, 3, 2, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_2.addWidget(self.comboBox_2, 1, 3, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 2, 3, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_2.addWidget(self.spinBox, 2, 1, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.gridLayout_2.addWidget(self.plainTextEdit_2, 3, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 2, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_2.addWidget(self.plainTextEdit, 3, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)

        self.groupBox_2 = QGroupBox(create_os_form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 376, 474, 91))
        self.groupBox_3 = QGroupBox(create_os_form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 50, 353, 58))
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.lineEdit_3 = QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout.addWidget(self.lineEdit_3)


        self.retranslateUi(create_os_form)

        QMetaObject.connectSlotsByName(create_os_form)
    # setupUi

    def retranslateUi(self, create_os_form):
        create_os_form.setWindowTitle(QCoreApplication.translate("create_os_form", u"Crear dispositivo", None))
        self.label_9.setText(QCoreApplication.translate("create_os_form", u"Crear Orden de Servicio en Kordata", None))
        self.BtnSaveDevice.setText(QCoreApplication.translate("create_os_form", u"Guardar Dispositivo", None))
        self.groupBox.setTitle(QCoreApplication.translate("create_os_form", u"Informaci\u00f3n del dispositivo", None))
        self.label.setText(QCoreApplication.translate("create_os_form", u"Modelo", None))
        self.label_6.setText(QCoreApplication.translate("create_os_form", u"Dias de diag", None))
        self.label_11.setText(QCoreApplication.translate("create_os_form", u"Comentario", None))
        self.lineEdit_7.setText("")
        self.label_4.setText(QCoreApplication.translate("create_os_form", u"Contrase\u00f1a", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("create_os_form", u"SI", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("create_os_form", u"NO", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("create_os_form", u"REVISAR", None))

        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("create_os_form", u"Seleccionar", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("create_os_form", u"SI", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("create_os_form", u"NO", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("create_os_form", u"REVISAR", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("create_os_form", u"Seleccionar", None))
        self.label_10.setText(QCoreApplication.translate("create_os_form", u"Problema", None))
        self.label_2.setText(QCoreApplication.translate("create_os_form", u"Garrantia", None))
        self.label_5.setText(QCoreApplication.translate("create_os_form", u"Num de serie", None))
        self.label_8.setText(QCoreApplication.translate("create_os_form", u"Respaldo", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("create_os_form", u"Orden de servicio", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("create_os_form", u"Cliente", None))
        self.label_3.setText(QCoreApplication.translate("create_os_form", u"Cliente", None))
        self.label_7.setText(QCoreApplication.translate("create_os_form", u"Tel\u00e9fono", None))
        self.lineEdit_3.setInputMask(QCoreApplication.translate("create_os_form", u"9999999999", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("create_os_form", u"1234567890", None))
    # retranslateUi

