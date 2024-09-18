# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aftersalesui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(576, 622)
        self.actionActualizar_datos = QAction(MainWindow)
        self.actionActualizar_datos.setObjectName(u"actionActualizar_datos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.CheckSameUser = QCheckBox(self.centralwidget)
        self.CheckSameUser.setObjectName(u"CheckSameUser")

        self.horizontalLayout_4.addWidget(self.CheckSameUser)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.TxtClientName = QLineEdit(self.centralwidget)
        self.TxtClientName.setObjectName(u"TxtClientName")

        self.verticalLayout.addWidget(self.TxtClientName)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.userBox = QGroupBox(self.centralwidget)
        self.userBox.setObjectName(u"userBox")
        self.horizontalLayout_3 = QHBoxLayout(self.userBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.userBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.TxtUserName = QLineEdit(self.userBox)
        self.TxtUserName.setObjectName(u"TxtUserName")

        self.horizontalLayout.addWidget(self.TxtUserName)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.userBox)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.TxtUserPhone = QLineEdit(self.userBox)
        self.TxtUserPhone.setObjectName(u"TxtUserPhone")

        self.horizontalLayout_2.addWidget(self.TxtUserPhone)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.userBox)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.TxtBuyDate = QLineEdit(self.groupBox)
        self.TxtBuyDate.setObjectName(u"TxtBuyDate")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.TxtBuyDate)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.CbxModel = QComboBox(self.groupBox)
        self.CbxModel.setObjectName(u"CbxModel")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.CbxModel)

        self.TxtModel = QLineEdit(self.groupBox)
        self.TxtModel.setObjectName(u"TxtModel")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.TxtModel)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.CbxType = QComboBox(self.groupBox)
        self.CbxType.setObjectName(u"CbxType")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.CbxType)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.TxtProblem = QPlainTextEdit(self.groupBox)
        self.TxtProblem.setObjectName(u"TxtProblem")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.TxtProblem)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.TxtLeftDays = QLineEdit(self.groupBox)
        self.TxtLeftDays.setObjectName(u"TxtLeftDays")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.TxtLeftDays)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.TxtNot = QLineEdit(self.groupBox)
        self.TxtNot.setObjectName(u"TxtNot")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.TxtNot)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.CbxAgent = QComboBox(self.groupBox_2)
        self.CbxAgent.setObjectName(u"CbxAgent")

        self.verticalLayout_3.addWidget(self.CbxAgent)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.BtnSave = QPushButton(self.centralwidget)
        self.BtnSave.setObjectName(u"BtnSave")

        self.verticalLayout_2.addWidget(self.BtnSave)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 576, 33))
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
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"NOTA O FACTURA", None))
        self.CheckSameUser.setText(QCoreApplication.translate("MainWindow", u"Mismo due\u00f1o", None))
        self.userBox.setTitle(QCoreApplication.translate("MainWindow", u"Usuario del dispositivo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fecha de compra", None))
        self.TxtBuyDate.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Modelo del equipo", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tipo de postventa", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n del problema", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"D\u00edas restantes ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nota de venta", None))
        self.TxtNot.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOT00000", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"AGENTE", None))
        self.BtnSave.setText(QCoreApplication.translate("MainWindow", u"Guardar registro", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

