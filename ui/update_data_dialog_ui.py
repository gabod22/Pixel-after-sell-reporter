# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_data_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 391)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.TxtSellnotePath = QLineEdit(Dialog)
        self.TxtSellnotePath.setObjectName(u"TxtSellnotePath")

        self.horizontalLayout_2.addWidget(self.TxtSellnotePath)

        self.BtnOpenSellnoteFile = QPushButton(Dialog)
        self.BtnOpenSellnoteFile.setObjectName(u"BtnOpenSellnoteFile")

        self.horizontalLayout_2.addWidget(self.BtnOpenSellnoteFile)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TxtInvoicesPath = QLineEdit(Dialog)
        self.TxtInvoicesPath.setObjectName(u"TxtInvoicesPath")

        self.horizontalLayout.addWidget(self.TxtInvoicesPath)

        self.BtnOpenInvoiceFile = QPushButton(Dialog)
        self.BtnOpenInvoiceFile.setObjectName(u"BtnOpenInvoiceFile")

        self.horizontalLayout.addWidget(self.BtnOpenInvoiceFile)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.TxtClienFilePath = QLineEdit(Dialog)
        self.TxtClienFilePath.setObjectName(u"TxtClienFilePath")

        self.horizontalLayout_3.addWidget(self.TxtClienFilePath)

        self.BtnOpenClientFile = QPushButton(Dialog)
        self.BtnOpenClientFile.setObjectName(u"BtnOpenClientFile")

        self.horizontalLayout_3.addWidget(self.BtnOpenClientFile)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.PlantextLog = QPlainTextEdit(Dialog)
        self.PlantextLog.setObjectName(u"PlantextLog")

        self.verticalLayout_4.addWidget(self.PlantextLog)

        self.BtnUpdateData = QPushButton(Dialog)
        self.BtnUpdateData.setObjectName(u"BtnUpdateData")

        self.verticalLayout_4.addWidget(self.BtnUpdateData)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Notas de venta", None))
        self.BtnOpenSellnoteFile.setText(QCoreApplication.translate("Dialog", u"Abrir documento", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Faturas", None))
        self.BtnOpenInvoiceFile.setText(QCoreApplication.translate("Dialog", u"Abrir documento", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Clientes", None))
        self.BtnOpenClientFile.setText(QCoreApplication.translate("Dialog", u"Abrir documento", None))
        self.BtnUpdateData.setText(QCoreApplication.translate("Dialog", u"Actualizar datos", None))
    # retranslateUi

