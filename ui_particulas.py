# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'particulas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 711)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(230, 244, 255);")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        font1 = QFont()
        font1.setPointSize(11)
        self.actionGuardar.setFont(font1)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionID = QAction(MainWindow)
        self.actionID.setObjectName(u"actionID")
        self.actionDISTANCIA = QAction(MainWindow)
        self.actionDISTANCIA.setObjectName(u"actionDISTANCIA")
        self.actionVELOCIDAD = QAction(MainWindow)
        self.actionVELOCIDAD.setObjectName(u"actionVELOCIDAD")
        self.actionPuntos_Cercanos = QAction(MainWindow)
        self.actionPuntos_Cercanos.setObjectName(u"actionPuntos_Cercanos")
        self.actionObtener_Puntos = QAction(MainWindow)
        self.actionObtener_Puntos.setObjectName(u"actionObtener_Puntos")
        self.actionGrafo = QAction(MainWindow)
        self.actionGrafo.setObjectName(u"actionGrafo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setFamily(u"Verdana")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.tabWidget.setFont(font2)
        self.tabWidget.setStyleSheet(u"background-color: rgb(231, 233, 255);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_8.setFont(font3)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.id_lineEdit_2 = QLineEdit(self.tab)
        self.id_lineEdit_2.setObjectName(u"id_lineEdit_2")
        self.id_lineEdit_2.setFont(font3)
        self.id_lineEdit_2.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout_2.addWidget(self.id_lineEdit_2, 1, 0, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.origen_x_spinBox_3 = QSpinBox(self.tab)
        self.origen_x_spinBox_3.setObjectName(u"origen_x_spinBox_3")
        self.origen_x_spinBox_3.setFont(font3)
        self.origen_x_spinBox_3.setMaximum(500)

        self.gridLayout_2.addWidget(self.origen_x_spinBox_3, 3, 0, 1, 1)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)

        self.origten_y_spinBox_4 = QSpinBox(self.tab)
        self.origten_y_spinBox_4.setObjectName(u"origten_y_spinBox_4")
        self.origten_y_spinBox_4.setFont(font3)
        self.origten_y_spinBox_4.setMaximum(500)

        self.gridLayout_2.addWidget(self.origten_y_spinBox_4, 5, 0, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)

        self.destino_x_spinBox_2 = QSpinBox(self.tab)
        self.destino_x_spinBox_2.setObjectName(u"destino_x_spinBox_2")
        self.destino_x_spinBox_2.setFont(font3)
        self.destino_x_spinBox_2.setMaximum(500)

        self.gridLayout_2.addWidget(self.destino_x_spinBox_2, 7, 0, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.gridLayout_2.addWidget(self.label, 8, 0, 1, 1)

        self.destino_y_spinBox = QSpinBox(self.tab)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setFont(font3)
        self.destino_y_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.destino_y_spinBox, 9, 0, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.gridLayout_2.addWidget(self.label_4, 10, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.tab)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setFont(font3)
        self.red_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.red_spinBox, 11, 0, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.gridLayout_2.addWidget(self.label_5, 12, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.tab)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setFont(font3)
        self.green_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.green_spinBox, 13, 0, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.gridLayout_2.addWidget(self.label_6, 14, 0, 1, 1)

        self.blue_spinBox = QSpinBox(self.tab)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setFont(font3)
        self.blue_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.blue_spinBox, 15, 0, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.gridLayout_2.addWidget(self.label_2, 16, 0, 1, 1)

        self.velocidad_lineEdit = QLineEdit(self.tab)
        self.velocidad_lineEdit.setObjectName(u"velocidad_lineEdit")
        self.velocidad_lineEdit.setFont(font3)
        self.velocidad_lineEdit.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout_2.addWidget(self.velocidad_lineEdit, 17, 0, 1, 1)

        self.agregar_final_pushButton_2 = QPushButton(self.tab)
        self.agregar_final_pushButton_2.setObjectName(u"agregar_final_pushButton_2")
        self.agregar_final_pushButton_2.setFont(font3)
        self.agregar_final_pushButton_2.setStyleSheet(u"background-color: rgb(181, 213, 255);")

        self.gridLayout_2.addWidget(self.agregar_final_pushButton_2, 17, 1, 1, 1)

        self.agregar_inicio_pushButton = QPushButton(self.tab)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")
        self.agregar_inicio_pushButton.setFont(font3)
        self.agregar_inicio_pushButton.setStyleSheet(u"background-color: rgb(181, 213, 255);")

        self.gridLayout_2.addWidget(self.agregar_inicio_pushButton, 18, 1, 1, 1)

        self.Mostrar_pushButton_3 = QPushButton(self.tab)
        self.Mostrar_pushButton_3.setObjectName(u"Mostrar_pushButton_3")
        self.Mostrar_pushButton_3.setBaseSize(QSize(0, 0))
        self.Mostrar_pushButton_3.setFont(font3)
        self.Mostrar_pushButton_3.setStyleSheet(u"border-bottom-color: rgb(3, 3, 255);\n"
"background-color: rgb(181, 213, 255);")

        self.gridLayout_2.addWidget(self.Mostrar_pushButton_3, 19, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFont(font3)
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(231, 233, 255);")

        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 1, 17, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget = QTableWidget(self.tab_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(190, 236, 255);\n"
"font: italic 8pt \"MS Sans Serif\";\n"
"font: 11pt \"MS Shell Dlg 2\";")

        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")
        self.buscar_lineEdit.setFont(font1)

        self.gridLayout_3.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")
        self.buscar_pushButton.setFont(font)

        self.gridLayout_3.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton_2 = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton_2.setObjectName(u"mostrar_tabla_pushButton_2")
        self.mostrar_tabla_pushButton_2.setFont(font)

        self.gridLayout_3.addWidget(self.mostrar_tabla_pushButton_2, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar = QPushButton(self.tab_3)
        self.dibujar.setObjectName(u"dibujar")
        self.dibujar.setFont(font1)

        self.gridLayout_4.addWidget(self.dibujar, 1, 0, 1, 1)

        self.limpiar = QPushButton(self.tab_3)
        self.limpiar.setObjectName(u"limpiar")
        self.limpiar.setFont(font1)

        self.gridLayout_4.addWidget(self.limpiar, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.mostrarGrafo = QPlainTextEdit(self.tab_4)
        self.mostrarGrafo.setObjectName(u"mostrarGrafo")

        self.gridLayout_5.addWidget(self.mostrarGrafo, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 750, 23))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuOrdenamientos = QMenu(self.menubar)
        self.menuOrdenamientos.setObjectName(u"menuOrdenamientos")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        self.menuAlgoritmos.setFont(font)
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuOrdenamientos.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addSeparator()
        self.menuOrdenamientos.addAction(self.actionID)
        self.menuOrdenamientos.addAction(self.actionDISTANCIA)
        self.menuOrdenamientos.addAction(self.actionVELOCIDAD)
        self.menuAlgoritmos.addAction(self.actionPuntos_Cercanos)
        self.menuAlgoritmos.addSeparator()
        self.menuAlgoritmos.addAction(self.actionGrafo)
        self.menuVer.addAction(self.actionObtener_Puntos)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionID.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.actionDISTANCIA.setText(QCoreApplication.translate("MainWindow", u"DISTANCIA", None))
        self.actionVELOCIDAD.setText(QCoreApplication.translate("MainWindow", u"VELOCIDAD", None))
        self.actionPuntos_Cercanos.setText(QCoreApplication.translate("MainWindow", u"Puntos Cercanos", None))
        self.actionObtener_Puntos.setText(QCoreApplication.translate("MainWindow", u"Obtener Puntos", None))
        self.actionGrafo.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"origen x", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"origen y", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"destino x", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"destino y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"red", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"green", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"blue", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"velocidad", None))
        self.agregar_final_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.Mostrar_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.plainTextEdit.setPlaceholderText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agrega", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identificador de Particula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"visualizacion", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Texto Grafo", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuOrdenamientos.setTitle(QCoreApplication.translate("MainWindow", u"Ordenamientos", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
    # retranslateUi

