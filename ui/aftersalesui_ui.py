# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aftersalesui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(570, 559)
        self.actionActualizar_datos = QAction(MainWindow)
        self.actionActualizar_datos.setObjectName(u"actionActualizar_datos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.TxtClientName = QLineEdit(self.centralwidget)
        self.TxtClientName.setObjectName(u"TxtClientName")

        self.horizontalLayout_4.addWidget(self.TxtClientName)

        self.CheckSameUser = QCheckBox(self.centralwidget)
        self.CheckSameUser.setObjectName(u"CheckSameUser")

        self.horizontalLayout_4.addWidget(self.CheckSameUser)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.TxtUserName = QLineEdit(self.groupBox)
        self.TxtUserName.setObjectName(u"TxtUserName")

        self.horizontalLayout.addWidget(self.TxtUserName)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.TxtUserPhone = QLineEdit(self.groupBox)
        self.TxtUserPhone.setObjectName(u"TxtUserPhone")

        self.horizontalLayout_2.addWidget(self.TxtUserPhone)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.TxtNot = QLineEdit(self.centralwidget)
        self.TxtNot.setObjectName(u"TxtNot")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.TxtNot)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.TxtOS = QLineEdit(self.centralwidget)
        self.TxtOS.setObjectName(u"TxtOS")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.TxtOS)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.CbxType = QComboBox(self.centralwidget)
        self.CbxType.addItem("")
        self.CbxType.addItem("")
        self.CbxType.addItem("")
        self.CbxType.addItem("")
        self.CbxType.setObjectName(u"CbxType")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.CbxType)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.TxtProblem = QPlainTextEdit(self.centralwidget)
        self.TxtProblem.setObjectName(u"TxtProblem")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.TxtProblem)

        self.CbxModel = QComboBox(self.centralwidget)
        self.CbxModel.setObjectName(u"CbxModel")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.CbxModel)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.BtnSave = QPushButton(self.centralwidget)
        self.BtnSave.setObjectName(u"BtnSave")

        self.verticalLayout_2.addWidget(self.BtnSave)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 570, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionActualizar_datos)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Registro de postventas", None))
        self.actionActualizar_datos.setText(QCoreApplication.translate("MainWindow", u"Actualizar datos", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Cliente Kordata", None))
        self.CheckSameUser.setText(QCoreApplication.translate("MainWindow", u"Mismo due\u00f1o", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Usuario de computadora", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nota de venta", None))
        self.TxtNot.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOT00000", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Modelo del equipo", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Orden servicio", None))
        self.TxtOS.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SERV00000", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tipo de postventa", None))
        self.CbxType.setItemText(0, QCoreApplication.translate("MainWindow", u"Garant\u00eda", None))
        self.CbxType.setItemText(1, QCoreApplication.translate("MainWindow", u"Reparaci\u00f3n", None))
        self.CbxType.setItemText(2, QCoreApplication.translate("MainWindow", u"Consulta", None))
        self.CbxType.setItemText(3, QCoreApplication.translate("MainWindow", u"Soporte", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n del problema", None))
        self.BtnSave.setText(QCoreApplication.translate("MainWindow", u"Guardar registro", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

