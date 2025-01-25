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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 202)
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

        self.verticalLayout.addWidget(self.TxtPassword)


        self.verticalLayout_3.addLayout(self.verticalLayout)

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
        self.TxtPassword.setPlaceholderText(QCoreApplication.translate("Dialog", u"password", None))
        self.BtnSubmit.setText(QCoreApplication.translate("Dialog", u"Iniciar sesi\u00f3n", None))
    # retranslateUi

