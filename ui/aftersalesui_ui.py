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
        MainWindow.resize(533, 703)
        self.actionActualizar_datos = QAction(MainWindow)
        self.actionActualizar_datos.setObjectName(u"actionActualizar_datos")
        self.actionGuardar_contacto = QAction(MainWindow)
        self.actionGuardar_contacto.setObjectName(u"actionGuardar_contacto")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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

        self.CheckManualMode = QCheckBox(self.centralwidget)
        self.CheckManualMode.setObjectName(u"CheckManualMode")

        self.horizontalLayout_4.addWidget(self.CheckManualMode)

        self.CheckSameUser = QCheckBox(self.centralwidget)
        self.CheckSameUser.setObjectName(u"CheckSameUser")

        self.horizontalLayout_4.addWidget(self.CheckSameUser)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.TxtSearch = QLineEdit(self.centralwidget)
        self.TxtSearch.setObjectName(u"TxtSearch")

        self.verticalLayout.addWidget(self.TxtSearch)


        self.verticalLayout_4.addLayout(self.verticalLayout)

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


        self.verticalLayout_4.addWidget(self.userBox)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.TxtClientName = QLineEdit(self.groupBox)
        self.TxtClientName.setObjectName(u"TxtClientName")

        self.horizontalLayout_5.addWidget(self.TxtClientName)

        self.BtnCopyClientName = QPushButton(self.groupBox)
        self.BtnCopyClientName.setObjectName(u"BtnCopyClientName")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.BtnCopyClientName.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.BtnCopyClientName)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.TxtClientPhone = QLineEdit(self.groupBox)
        self.TxtClientPhone.setObjectName(u"TxtClientPhone")

        self.horizontalLayout_6.addWidget(self.TxtClientPhone)

        self.BtnCopyClientPhone = QPushButton(self.groupBox)
        self.BtnCopyClientPhone.setObjectName(u"BtnCopyClientPhone")
        self.BtnCopyClientPhone.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.BtnCopyClientPhone)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.TxtNot = QLineEdit(self.groupBox)
        self.TxtNot.setObjectName(u"TxtNot")

        self.horizontalLayout_7.addWidget(self.TxtNot)

        self.BtnCopyNote = QPushButton(self.groupBox)
        self.BtnCopyNote.setObjectName(u"BtnCopyNote")
        self.BtnCopyNote.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.BtnCopyNote)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.TxtSeller = QLineEdit(self.groupBox)
        self.TxtSeller.setObjectName(u"TxtSeller")

        self.horizontalLayout_8.addWidget(self.TxtSeller)

        self.BtnCopySeller = QPushButton(self.groupBox)
        self.BtnCopySeller.setObjectName(u"BtnCopySeller")
        self.BtnCopySeller.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.BtnCopySeller)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.TxtBuyDate = QLineEdit(self.groupBox)
        self.TxtBuyDate.setObjectName(u"TxtBuyDate")

        self.horizontalLayout_9.addWidget(self.TxtBuyDate)

        self.BtnCopyBuyDate = QPushButton(self.groupBox)
        self.BtnCopyBuyDate.setObjectName(u"BtnCopyBuyDate")
        self.BtnCopyBuyDate.setIcon(icon)

        self.horizontalLayout_9.addWidget(self.BtnCopyBuyDate)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_9)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.TxtLeftDays = QLineEdit(self.groupBox)
        self.TxtLeftDays.setObjectName(u"TxtLeftDays")

        self.horizontalLayout_10.addWidget(self.TxtLeftDays)

        self.BtnCopyLeftDays = QPushButton(self.groupBox)
        self.BtnCopyLeftDays.setObjectName(u"BtnCopyLeftDays")
        self.BtnCopyLeftDays.setIcon(icon)

        self.horizontalLayout_10.addWidget(self.BtnCopyLeftDays)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_10)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.CbxModel = QComboBox(self.groupBox)
        self.CbxModel.setObjectName(u"CbxModel")

        self.verticalLayout_2.addWidget(self.CbxModel)

        self.TxtModel = QLineEdit(self.groupBox)
        self.TxtModel.setObjectName(u"TxtModel")

        self.verticalLayout_2.addWidget(self.TxtModel)


        self.horizontalLayout_11.addLayout(self.verticalLayout_2)

        self.BtnCopyModel = QPushButton(self.groupBox)
        self.BtnCopyModel.setObjectName(u"BtnCopyModel")
        self.BtnCopyModel.setMaximumSize(QSize(28, 24))
        self.BtnCopyModel.setIcon(icon)

        self.horizontalLayout_11.addWidget(self.BtnCopyModel)


        self.formLayout.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout_11)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_7)

        self.CbxType = QComboBox(self.groupBox)
        self.CbxType.setObjectName(u"CbxType")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.CbxType)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_8)

        self.TxtProblem = QPlainTextEdit(self.groupBox)
        self.TxtProblem.setObjectName(u"TxtProblem")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.TxtProblem)

        self.CheckRegisterContact = QCheckBox(self.groupBox)
        self.CheckRegisterContact.setObjectName(u"CheckRegisterContact")
        self.CheckRegisterContact.setChecked(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.CheckRegisterContact)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.CbxAgent = QComboBox(self.groupBox_2)
        self.CbxAgent.setObjectName(u"CbxAgent")

        self.verticalLayout_3.addWidget(self.CbxAgent)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.BtnSave = QPushButton(self.centralwidget)
        self.BtnSave.setObjectName(u"BtnSave")

        self.verticalLayout_4.addWidget(self.BtnSave)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 533, 33))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionActualizar_datos)
        self.menuArchivo.addAction(self.actionGuardar_contacto)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Registro de postventas", None))
        self.actionActualizar_datos.setText(QCoreApplication.translate("MainWindow", u"Actualizar datos", None))
        self.actionGuardar_contacto.setText(QCoreApplication.translate("MainWindow", u"Guardar contacto", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"NOTA O FACTURA", None))
        self.CheckManualMode.setText(QCoreApplication.translate("MainWindow", u"Modo manual", None))
        self.CheckSameUser.setText(QCoreApplication.translate("MainWindow", u"Mismo due\u00f1o", None))
        self.userBox.setTitle(QCoreApplication.translate("MainWindow", u"Usuario del dispositivo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nombre Cliente", None))
        self.BtnCopyClientName.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.BtnCopyClientPhone.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nota de venta", None))
        self.TxtNot.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOT00000", None))
        self.BtnCopyNote.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Vendedor", None))
        self.BtnCopySeller.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fecha de compra", None))
        self.TxtBuyDate.setPlaceholderText("")
        self.BtnCopyBuyDate.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"D\u00edas restantes ", None))
        self.BtnCopyLeftDays.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Modelo del equipo", None))
        self.BtnCopyModel.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tipo de postventa", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n del problema", None))
        self.CheckRegisterContact.setText(QCoreApplication.translate("MainWindow", u"Guardar contacto", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"AGENTE", None))
        self.BtnSave.setText(QCoreApplication.translate("MainWindow", u"Guardar registro", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

