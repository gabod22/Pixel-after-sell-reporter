# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kordata_login.ui'
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

class Ui_Kordata_Login(object):
    def setupUi(self, Kordata_Login):
        if not Kordata_Login.objectName():
            Kordata_Login.setObjectName(u"Kordata_Login")
        Kordata_Login.resize(424, 236)
        self.verticalLayout_3 = QVBoxLayout(Kordata_Login)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Kordata_Login)
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
        self.label_3 = QLabel(Kordata_Login)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.TxtEmail = QLineEdit(Kordata_Login)
        self.TxtEmail.setObjectName(u"TxtEmail")

        self.verticalLayout_2.addWidget(self.TxtEmail)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Kordata_Login)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.TxtPassword = QLineEdit(Kordata_Login)
        self.TxtPassword.setObjectName(u"TxtPassword")
        self.TxtPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.TxtPassword)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CheckAutoClose = QCheckBox(Kordata_Login)
        self.CheckAutoClose.setObjectName(u"CheckAutoClose")

        self.horizontalLayout.addWidget(self.CheckAutoClose)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.CheckRemember = QCheckBox(Kordata_Login)
        self.CheckRemember.setObjectName(u"CheckRemember")

        self.horizontalLayout.addWidget(self.CheckRemember)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.BtnSubmit = QPushButton(Kordata_Login)
        self.BtnSubmit.setObjectName(u"BtnSubmit")

        self.verticalLayout_3.addWidget(self.BtnSubmit)


        self.retranslateUi(Kordata_Login)

        QMetaObject.connectSlotsByName(Kordata_Login)
    # setupUi

    def retranslateUi(self, Kordata_Login):
        Kordata_Login.setWindowTitle(QCoreApplication.translate("Kordata_Login", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Kordata_Login", u"KORDATA LOGIN", None))
        self.label_3.setText(QCoreApplication.translate("Kordata_Login", u"Correo", None))
        self.TxtEmail.setPlaceholderText(QCoreApplication.translate("Kordata_Login", u"example@pixel-lap.com", None))
        self.label_2.setText(QCoreApplication.translate("Kordata_Login", u"Contrase\u00f1a", None))
        self.TxtPassword.setInputMask("")
        self.TxtPassword.setText("")
        self.TxtPassword.setPlaceholderText(QCoreApplication.translate("Kordata_Login", u"password", None))
        self.CheckAutoClose.setText(QCoreApplication.translate("Kordata_Login", u"Cerrar Sesiones autom\u00e1ticamente", None))
        self.CheckRemember.setText(QCoreApplication.translate("Kordata_Login", u"Recordar cuenta", None))
        self.BtnSubmit.setText(QCoreApplication.translate("Kordata_Login", u"Iniciar sesi\u00f3n", None))
    # retranslateUi

