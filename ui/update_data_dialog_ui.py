# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_data_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(424, 236)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.TxtEmail = QLineEdit(Dialog)
        self.TxtEmail.setObjectName(u"TxtEmail")

        self.verticalLayout_2.addWidget(self.TxtEmail)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.TxtPassword = QLineEdit(Dialog)
        self.TxtPassword.setObjectName(u"TxtPassword")
        self.TxtPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.TxtPassword)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CheckAutoClose = QCheckBox(Dialog)
        self.CheckAutoClose.setObjectName(u"CheckAutoClose")

        self.horizontalLayout.addWidget(self.CheckAutoClose)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.CheckRemember = QCheckBox(Dialog)
        self.CheckRemember.setObjectName(u"CheckRemember")

        self.horizontalLayout.addWidget(self.CheckRemember)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.BtnSubmit = QPushButton(Dialog)
        self.BtnSubmit.setObjectName(u"BtnSubmit")

        self.verticalLayout_3.addWidget(self.BtnSubmit)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"KORDATA LOGIN", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Correo", None))
        self.TxtEmail.setPlaceholderText(QCoreApplication.translate("Dialog", u"example@pixel-lap.com", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a", None))
        self.TxtPassword.setInputMask("")
        self.TxtPassword.setText("")
        self.TxtPassword.setPlaceholderText(QCoreApplication.translate("Dialog", u"password", None))
        self.CheckAutoClose.setText(QCoreApplication.translate("Dialog", u"Cerrar Sesiones autom\u00e1ticamente", None))
        self.CheckRemember.setText(QCoreApplication.translate("Dialog", u"Recordar cuenta", None))
        self.BtnSubmit.setText(QCoreApplication.translate("Dialog", u"Iniciar sesi\u00f3n", None))
    # retranslateUi

