from PySide2.QtWidgets import QMainWindow,QFileDialog,QMessageBox,QTableWidgetItem,QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from ui_particulas import Ui_MainWindow
from adminparticulas import Adminparticulas
from particula import Particula
from pprint import pprint
from algoritmo import get_poit_near
from grafos import Grafo

# Rserva memria para mostrar ventana
class MainWindow(QMainWindow):
    def __init__(self): 
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.adminpart = Adminparticulas()
        self.listpart = []
        #------------------------------------ conexiones-------------------------------------------
        #------------------------------------------------------------------------------------------------------
        #------------------------------------------------------------------------------------------------------
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.agregar_final_pushButton_2.clicked.connect(self.click_agregar_final)
        self.ui.Mostrar_pushButton_3.clicked.connect(self.click_mostrar_plait)
        #los widgets estan alrevez abrir es guardar 
       
        self.ui.mostrar_tabla_pushButton_2.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.busca)
        self.ui.limpiar.clicked.connect(self.limpiaGraf)
        self.ui.dibujar.clicked.connect(self.dibujaGraf)
        # actionGuardar = actionAbrir y al  revez con actionAbrir
        self.ui.actionGuardar.triggered.connect(self.click_guardar)
        self.ui.actionAbrir.triggered.connect(self.click_abrir)
       
        #algoritmo de ordenamientos
        self.ui.actionID.triggered.connect(self.ordenar_Id)
        self.ui.actionDISTANCIA.triggered.connect(self.Ordenar_Distancia)
        self.ui.actionVELOCIDAD.triggered.connect(self.Ordenar_Velocidad)
        # Algoritmo de fuerza bruta
        self.ui.actionObtener_Puntos.triggered.connect(self.dibuja_Puntos)
        self.ui.actionPuntos_Cercanos.triggered.connect(self.obten_Puntos_cercanos)
        #grafo conexiones
        self.ui.actionGrafo.triggered.connect(self.Grafo_)
        #__________________________fin de conceiones_______________________________________________---
       #----------------------------------------------------------------------------------------------
       #----------------------------------------------------------------------------------------------
        # instanciamos lo que es la clase
        self.scene = QGraphicsScene()
        #nombre del widget se asigna todos los atributos scene
        self.ui.graphicsView.setScene(self.scene)

        #instancia de grafo
        
    #--------------------------------------------------------------------------------------
    #--------------------------------FUNCIONES---------------------------------------------
    

    @Slot()
    def dibuja_Puntos(self):
        self.listpart = self.adminpart.get_puntos()
        #quitar los colores si hay error
        
        for punt in self.listpart:
            punto1 = punt[0]
            punto2 = punt[1]
            red = punt[2]
            gree = punt[3]
            blue = punt[4]
            ##darle color
            color = QColor(red,gree,blue)
            pen = QPen()
            pen.setColor(color)
            pen.setWidth(5)
            self.scene.addEllipse(punto1,punto2,6,6,pen)
        
    @Slot()
    def obten_Puntos_cercanos(self):
        resultado = get_poit_near(self.listpart)
        pen = QPen() 
        r = 95
        g = 158
        b = 160

        color = QColor(r,g,b)
        pen.setColor(color)
        pen.setWidth(3)
        pprint(resultado)
        for punto1, punto2 in resultado:
            x1 = punto1 [0]
            y1 = punto1 [1]
            x2 = punto2 [0]
            y2 = punto2 [1]

            self.scene.addLine(x1, y1, x2, y2,pen)



    @Slot()
    def ordenar_Id(self):
        self.adminpart.ordenart_id()
        
    @Slot()
    def Ordenar_Distancia(self):
        self.adminpart.ordenar_Distan()

    @Slot()
    def Ordenar_Velocidad(self):
        self.adminpart.ordernar_Veloc()


    def wheelEvent(self, event):
        print(event.delta())
        if event.delta()>0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def limpiaGraf(self):
        self.scene.clear()
    @Slot()
    def dibujaGraf(self):
        #pincel
        pen = QPen()
        pen.setWidth(3)
        for particula in self.adminpart:
            #origen
            x1 = particula.OrigenX
            x2 = particula.OrigenY
            #destino
            y1= particula.DestinoX
            y2 = particula.DestinoY
            #colores
            red = particula.red
            gree = particula.gree
            blue = particula.blue
            #darle color
            color = QColor(red,gree,blue)
            pen.setColor(color)
            #puntos y lineas
            self.scene.addEllipse(x1,x2,3,3,pen)
            self.scene.addEllipse(y1,y2,3,3,pen)
            self.scene.addLine(x1+3,x2+3,y1+3,y2+3,pen)


    @Slot()
    def busca(self):
        id = int(self.ui.buscar_lineEdit.text())
        encontrado = False
        for particula in self.adminpart:
            if id == particula.id:
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setRowCount(1)
                id_witget = QTableWidgetItem(str(particula.id))
                OrigenX_witget = QTableWidgetItem(str(particula.OrigenX))
                OrigenY_witget = QTableWidgetItem(str(particula.OrigenY))
                DestinoX_witget = QTableWidgetItem(str(particula.DestinoX))
                DestinoY_witget = QTableWidgetItem(str(particula.DestinoY))
                Velocidad_witget =QTableWidgetItem(str(particula.Velocidad)) 
                red_witget =QTableWidgetItem(str(particula.red))
                gree_witget =QTableWidgetItem(str(particula.gree))
                blue_witget =QTableWidgetItem(str(particula.blue))
                #distancia no ocupa property por que atributo publico
                distancia_witget =QTableWidgetItem(str(particula.distancia))

                self.ui.tableWidget.setItem(0,0, id_witget)
                self.ui.tableWidget.setItem(0,1, OrigenX_witget)
                self.ui.tableWidget.setItem(0,2, OrigenY_witget)
                self.ui.tableWidget.setItem(0,3, DestinoX_witget)
                self.ui.tableWidget.setItem(0,4, DestinoY_witget)
                self.ui.tableWidget.setItem(0,5, Velocidad_witget)
                self.ui.tableWidget.setItem(0,6, red_witget)
                self.ui.tableWidget.setItem(0,7, gree_witget)
                self.ui.tableWidget.setItem(0,8, blue_witget)
                self.ui.tableWidget.setItem(0,9, distancia_witget)
                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(self,"Atencion",f"La Particula con La identificacion '{id}' no Fue Encontrada")



    @Slot()
    def mostrar_tabla(self):
        self.ui.tableWidget.setColumnCount(10)
        headers = ("ID", "OrigenX", "OrigenY", "DestinoX","DestinoY","Velocidad","red", "gree", "blue","distancia")
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget.setRowCount(len(self.adminpart))
        row = 0
        for particula in self.adminpart:
            id_witget = QTableWidgetItem(str(particula.id))
            OrigenX_witget = QTableWidgetItem(str(particula.OrigenX))
            OrigenY_witget = QTableWidgetItem(str(particula.OrigenY))
            DestinoX_witget = QTableWidgetItem(str(particula.DestinoX))
            DestinoY_witget = QTableWidgetItem(str(particula.DestinoY))
            Velocidad_witget =QTableWidgetItem(str(particula.Velocidad)) 
            red_witget =QTableWidgetItem(str(particula.red))
            gree_witget =QTableWidgetItem(str(particula.gree))
            blue_witget =QTableWidgetItem(str(particula.blue))
            #distancia no ocupa property por que atributo publico
            distancia_witget =QTableWidgetItem(str(particula.distancia))

            self.ui.tableWidget.setItem(row,0, id_witget)
            self.ui.tableWidget.setItem(row,1, OrigenX_witget)
            self.ui.tableWidget.setItem(row,2, OrigenY_witget)
            self.ui.tableWidget.setItem(row,3, DestinoX_witget)
            self.ui.tableWidget.setItem(row,4, DestinoY_witget)
            self.ui.tableWidget.setItem(row,5, Velocidad_witget)
            self.ui.tableWidget.setItem(row,6, red_witget)
            self.ui.tableWidget.setItem(row,7, gree_witget)
            self.ui.tableWidget.setItem(row,8, blue_witget)
            self.ui.tableWidget.setItem(row,9, distancia_witget)
            row+=1  

    @Slot()
    def click_agregar_inicio(self):
        
        id = self.ui.id_lineEdit_2.text()
        origen_x = self.ui.origen_x_spinBox_3.value()
        origen_y = self.ui.origten_y_spinBox_4.value()
        destino_x = self.ui.destino_x_spinBox_2.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        gree = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(int(id),origen_x,origen_y,
                              destino_x,destino_y,int(velocidad),
                              red,gree,blue)

        self.adminpart.agregar_inicio(particula)
        QMessageBox.information(self,"","Agregado al Inicio")

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id_lineEdit_2.text()
        origen_x = self.ui.origen_x_spinBox_3.value()
        origen_y = self.ui.origten_y_spinBox_4.value()
        destino_x = self.ui.destino_x_spinBox_2.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        
        red = self.ui.red_spinBox.value()
        gree = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        particula = Particula(int(id),origen_x,origen_y,
                              destino_x,destino_y,int(velocidad),
                              red,gree,blue)
        self.adminpart.agregar_al_final(particula)
        QMessageBox.information(self,"","Agregado al Final")
           
    
    @Slot()
    def click_mostrar_plait(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.adminpart))

    @Slot()
    def click_abrir(self):
        ubicacion = QFileDialog.getOpenFileName(
            self, "Abrir archivo",".","JSON (*.json)"
        )[0]
        self.adminpart.Abrir(ubicacion)

    @Slot()
    def click_guardar(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar Archivo",
            ".",
            "JSON (*.json)"
        )[0]
        print(ubicacion)
        if self.adminpart.Guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "El archivo Fue Creado" + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )
    @Slot()
    def Grafo_(self):
        g = self.adminpart.get_grafo()
       # g.print_list_adyacencia()
        s = g.grafo_to_str()
        self.ui.mostrarGrafo.setPlainText(s)
