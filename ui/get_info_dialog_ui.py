# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'get_info_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPlainTextEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_GetInfoDialog(object):
    def setupUi(self, GetInfoDialog):
        if not GetInfoDialog.objectName():
            GetInfoDialog.setObjectName(u"GetInfoDialog")
        GetInfoDialog.resize(353, 193)
        self.verticalLayout = QVBoxLayout(GetInfoDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Logo = QLabel(GetInfoDialog)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setPixmap(QPixmap(u"../assets/logo.png"))
        self.Logo.setScaledContents(False)
        self.Logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.Logo)

        self.label = QLabel(GetInfoDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.PlainTextLog = QPlainTextEdit(GetInfoDialog)
        self.PlainTextLog.setObjectName(u"PlainTextLog")

        self.verticalLayout.addWidget(self.PlainTextLog)


        self.retranslateUi(GetInfoDialog)

        QMetaObject.connectSlotsByName(GetInfoDialog)
    # setupUi

    def retranslateUi(self, GetInfoDialog):
        GetInfoDialog.setWindowTitle(QCoreApplication.translate("GetInfoDialog", u"Obteniendo informaci\u00f3n", None))
        self.Logo.setText("")
        self.label.setText(QCoreApplication.translate("GetInfoDialog", u"Cargando informaci\u00f3n", None))
    # retranslateUi

