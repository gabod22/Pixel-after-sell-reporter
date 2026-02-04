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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(567, 785)
        self.actionActualizar_datos = QAction(MainWindow)
        self.actionActualizar_datos.setObjectName(u"actionActualizar_datos")
        self.actionGuardar_contacto = QAction(MainWindow)
        self.actionGuardar_contacto.setObjectName(u"actionGuardar_contacto")
        self.actionConfiguracion = QAction(MainWindow)
        self.actionConfiguracion.setObjectName(u"actionConfiguracion")
        self.accionLoginKordata = QAction(MainWindow)
        self.accionLoginKordata.setObjectName(u"accionLoginKordata")
        self.actionNueva_Orden_Servicio = QAction(MainWindow)
        self.actionNueva_Orden_Servicio.setObjectName(u"actionNueva_Orden_Servicio")
        self.actionIniciar_sesion = QAction(MainWindow)
        self.actionIniciar_sesion.setObjectName(u"actionIniciar_sesion")
        self.actionActualizar_datos_2 = QAction(MainWindow)
        self.actionActualizar_datos_2.setObjectName(u"actionActualizar_datos_2")
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
        self.TxtSearch.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.TxtSearch)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 547, 622))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.userBox = QGroupBox(self.scrollAreaWidgetContents)
        self.userBox.setObjectName(u"userBox")
        self.userBox.setEnabled(True)
        self.userBox.setFlat(False)
        self.verticalLayout_17 = QVBoxLayout(self.userBox)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_12 = QLabel(self.userBox)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_5.addWidget(self.label_12)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.TxtClientName = QLineEdit(self.userBox)
        self.TxtClientName.setObjectName(u"TxtClientName")
        self.TxtClientName.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.TxtClientName)

        self.BtnCopyClientName = QPushButton(self.userBox)
        self.BtnCopyClientName.setObjectName(u"BtnCopyClientName")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.BtnCopyClientName.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.BtnCopyClientName)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_12.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_11 = QLabel(self.userBox)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_6.addWidget(self.label_11)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.TxtClientPhone = QLineEdit(self.userBox)
        self.TxtClientPhone.setObjectName(u"TxtClientPhone")
        self.TxtClientPhone.setMaximumSize(QSize(100, 16777215))
        self.TxtClientPhone.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.TxtClientPhone)

        self.BtnCopyClientPhone = QPushButton(self.userBox)
        self.BtnCopyClientPhone.setObjectName(u"BtnCopyClientPhone")
        self.BtnCopyClientPhone.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.BtnCopyClientPhone)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_12.addLayout(self.verticalLayout_6)

        self.CheckRegisterClient = QCheckBox(self.userBox)
        self.CheckRegisterClient.setObjectName(u"CheckRegisterClient")
        self.CheckRegisterClient.setEnabled(True)
        self.CheckRegisterClient.setCheckable(False)
        self.CheckRegisterClient.setChecked(False)

        self.horizontalLayout_12.addWidget(self.CheckRegisterClient)

        self.horizontalLayout_12.setStretch(0, 2)

        self.verticalLayout_17.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_3 = QLabel(self.userBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_15.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.TxtUserName = QLineEdit(self.userBox)
        self.TxtUserName.setObjectName(u"TxtUserName")
        self.TxtUserName.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.TxtUserName)

        self.BtnCopyUser = QPushButton(self.userBox)
        self.BtnCopyUser.setObjectName(u"BtnCopyUser")
        self.BtnCopyUser.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.BtnCopyUser)


        self.verticalLayout_15.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_10 = QLabel(self.userBox)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_16.addWidget(self.label_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TxtUserPhone = QLineEdit(self.userBox)
        self.TxtUserPhone.setObjectName(u"TxtUserPhone")
        self.TxtUserPhone.setMaximumSize(QSize(100, 16777215))
        self.TxtUserPhone.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.TxtUserPhone)

        self.BtnCopyUserPhone = QPushButton(self.userBox)
        self.BtnCopyUserPhone.setObjectName(u"BtnCopyUserPhone")
        self.BtnCopyUserPhone.setIcon(icon)

        self.horizontalLayout.addWidget(self.BtnCopyUserPhone)


        self.verticalLayout_16.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_16)

        self.CheckRegisterUser = QCheckBox(self.userBox)
        self.CheckRegisterUser.setObjectName(u"CheckRegisterUser")

        self.horizontalLayout_3.addWidget(self.CheckRegisterUser)

        self.horizontalLayout_3.setStretch(0, 2)

        self.verticalLayout_17.addLayout(self.horizontalLayout_3)


        self.verticalLayout_14.addWidget(self.userBox)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.TxtSellNote = QLineEdit(self.groupBox)
        self.TxtSellNote.setObjectName(u"TxtSellNote")
        self.TxtSellNote.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.TxtSellNote)

        self.BtnCopyNote = QPushButton(self.groupBox)
        self.BtnCopyNote.setObjectName(u"BtnCopyNote")
        self.BtnCopyNote.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.BtnCopyNote)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_13.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.TxtSeller = QLineEdit(self.groupBox)
        self.TxtSeller.setObjectName(u"TxtSeller")
        self.TxtSeller.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.TxtSeller)

        self.BtnCopySeller = QPushButton(self.groupBox)
        self.BtnCopySeller.setObjectName(u"BtnCopySeller")
        self.BtnCopySeller.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.BtnCopySeller)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_13.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_9.addWidget(self.label)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.TxtBuyDate = QLineEdit(self.groupBox)
        self.TxtBuyDate.setObjectName(u"TxtBuyDate")
        self.TxtBuyDate.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.TxtBuyDate)

        self.BtnCopyBuyDate = QPushButton(self.groupBox)
        self.BtnCopyBuyDate.setObjectName(u"BtnCopyBuyDate")
        self.BtnCopyBuyDate.setIcon(icon)

        self.horizontalLayout_9.addWidget(self.BtnCopyBuyDate)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_13.addLayout(self.verticalLayout_9)


        self.verticalLayout_18.addLayout(self.horizontalLayout_13)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_18.addWidget(self.line)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_10.addWidget(self.label_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.CbxModel = QComboBox(self.groupBox)
        self.CbxModel.setObjectName(u"CbxModel")
        self.CbxModel.setAutoFillBackground(True)
        self.CbxModel.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.CbxModel)

        self.TxtModel = QLineEdit(self.groupBox)
        self.TxtModel.setObjectName(u"TxtModel")
        self.TxtModel.setAutoFillBackground(True)
        self.TxtModel.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.TxtModel)


        self.horizontalLayout_11.addLayout(self.verticalLayout_2)

        self.BtnCopyModel = QPushButton(self.groupBox)
        self.BtnCopyModel.setObjectName(u"BtnCopyModel")
        self.BtnCopyModel.setMaximumSize(QSize(28, 24))
        self.BtnCopyModel.setIcon(icon)

        self.horizontalLayout_11.addWidget(self.BtnCopyModel)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_14.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_11.addWidget(self.label_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.LbLeftDays = QLabel(self.groupBox)
        self.LbLeftDays.setObjectName(u"LbLeftDays")
        font1 = QFont()
        font1.setPointSize(18)
        self.LbLeftDays.setFont(font1)

        self.horizontalLayout_10.addWidget(self.LbLeftDays)

        self.BtnCopyLeftDays = QPushButton(self.groupBox)
        self.BtnCopyLeftDays.setObjectName(u"BtnCopyLeftDays")
        self.BtnCopyLeftDays.setMaximumSize(QSize(30, 16777215))
        self.BtnCopyLeftDays.setIcon(icon)

        self.horizontalLayout_10.addWidget(self.BtnCopyLeftDays)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_14.addLayout(self.verticalLayout_11)

        self.horizontalLayout_14.setStretch(0, 4)
        self.horizontalLayout_14.setStretch(1, 1)

        self.verticalLayout_18.addLayout(self.horizontalLayout_14)


        self.verticalLayout_14.addWidget(self.groupBox)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_13.addWidget(self.label_7)

        self.CbxType = QComboBox(self.scrollAreaWidgetContents)
        self.CbxType.setObjectName(u"CbxType")
        self.CbxType.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.CbxType)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.CbxAgent = QComboBox(self.groupBox_2)
        self.CbxAgent.setObjectName(u"CbxAgent")
        self.CbxAgent.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.CbxAgent)


        self.verticalLayout_13.addWidget(self.groupBox_2)


        self.horizontalLayout_15.addLayout(self.verticalLayout_13)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_12.addWidget(self.label_8)

        self.TxtProblem = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.TxtProblem.setObjectName(u"TxtProblem")
        self.TxtProblem.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.TxtProblem)


        self.horizontalLayout_15.addLayout(self.verticalLayout_12)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 2)

        self.verticalLayout_14.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.BtnSave = QPushButton(self.centralwidget)
        self.BtnSave.setObjectName(u"BtnSave")

        self.verticalLayout_4.addWidget(self.BtnSave)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 567, 33))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuKordata = QMenu(self.menubar)
        self.menuKordata.setObjectName(u"menuKordata")
        self.menuGoogle = QMenu(self.menubar)
        self.menuGoogle.setObjectName(u"menuGoogle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuKordata.menuAction())
        self.menubar.addAction(self.menuGoogle.menuAction())
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionConfiguracion)
        self.menuKordata.addAction(self.actionActualizar_datos_2)
        self.menuKordata.addAction(self.actionNueva_Orden_Servicio)
        self.menuKordata.addSeparator()
        self.menuKordata.addAction(self.accionLoginKordata)
        self.menuKordata.addSeparator()
        self.menuGoogle.addAction(self.actionGuardar_contacto)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Registro de postventas", None))
        self.actionActualizar_datos.setText(QCoreApplication.translate("MainWindow", u"Actualizar datos", None))
        self.actionGuardar_contacto.setText(QCoreApplication.translate("MainWindow", u"Guardar contacto", None))
        self.actionConfiguracion.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.accionLoginKordata.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.actionNueva_Orden_Servicio.setText(QCoreApplication.translate("MainWindow", u"Nueva OS", None))
        self.actionIniciar_sesion.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesion", None))
        self.actionActualizar_datos_2.setText(QCoreApplication.translate("MainWindow", u"Actualizar datos", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"NOTA O FACTURA", None))
        self.CheckManualMode.setText(QCoreApplication.translate("MainWindow", u"Modo manual", None))
        self.CheckSameUser.setText(QCoreApplication.translate("MainWindow", u"Mismo due\u00f1o", None))
        self.userBox.setTitle(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nombre Cliente", None))
        self.BtnCopyClientName.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.TxtClientPhone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234567890", None))
        self.BtnCopyClientPhone.setText("")
        self.CheckRegisterClient.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.BtnCopyUser.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.TxtUserPhone.setInputMask(QCoreApplication.translate("MainWindow", u"9999999999", None))
        self.TxtUserPhone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234567890", None))
        self.BtnCopyUserPhone.setText("")
        self.CheckRegisterUser.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Venta", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nota de venta", None))
        self.TxtSellNote.setInputMask(QCoreApplication.translate("MainWindow", u"AAA09999", None))
        self.TxtSellNote.setText("")
        self.TxtSellNote.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOT00000", None))
        self.BtnCopyNote.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Vendedor", None))
        self.TxtSeller.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PANCHO VILLA", None))
        self.BtnCopySeller.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fecha de compra", None))
        self.TxtBuyDate.setInputMask(QCoreApplication.translate("MainWindow", u"99/99/9999", None))
        self.TxtBuyDate.setText(QCoreApplication.translate("MainWindow", u"01/25/2025", None))
        self.TxtBuyDate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MM/DD/YYYY", None))
        self.BtnCopyBuyDate.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Modelo del equipo", None))
        self.BtnCopyModel.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"D\u00edas restantes ", None))
        self.LbLeftDays.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.BtnCopyLeftDays.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tipo de postventa", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"AGENTE", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n del problema", None))
        self.BtnSave.setText(QCoreApplication.translate("MainWindow", u"Guardar registro", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuKordata.setTitle(QCoreApplication.translate("MainWindow", u"Kordata", None))
        self.menuGoogle.setTitle(QCoreApplication.translate("MainWindow", u"Google", None))
    # retranslateUi

