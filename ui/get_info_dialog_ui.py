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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_GetInfoDialog(object):
    def setupUi(self, GetInfoDialog):
        if not GetInfoDialog.objectName():
            GetInfoDialog.setObjectName(u"GetInfoDialog")
        GetInfoDialog.resize(515, 188)
        self.label = QLabel(GetInfoDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 481, 50))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LbStatus = QLabel(GetInfoDialog)
        self.LbStatus.setObjectName(u"LbStatus")
        self.LbStatus.setGeometry(QRect(20, 80, 481, 50))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.LbStatus.setFont(font1)
        self.LbStatus.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(GetInfoDialog)

        QMetaObject.connectSlotsByName(GetInfoDialog)
    # setupUi

    def retranslateUi(self, GetInfoDialog):
        GetInfoDialog.setWindowTitle(QCoreApplication.translate("GetInfoDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("GetInfoDialog", u"Cargando informaci\u00f3n de KORDATA", None))
        self.LbStatus.setText(QCoreApplication.translate("GetInfoDialog", u"STATUS", None))
    # retranslateUi

