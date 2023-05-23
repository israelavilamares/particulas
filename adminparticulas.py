from particula import Particula
from algoritmo import distancia_euclidiana
import json
from grafos import Grafo,Nodo,AristaNoDirigida

class Adminparticulas:
    def __init__(self) -> None:
        self.__particulas = []

    
    def agregar_al_final(self,partic:Particula):
        self.__particulas.append(partic)

    def agregar_inicio(self,partic:Particula):
        self.__particulas.insert(0,partic)

    
    # es una funcion que retona una lista
    def get_puntos(self) -> list:
        #creamos una lista
        puntos = []

        for partic in self.__particulas:
            punto1 = (partic.OrigenX,partic.OrigenY,partic.red,partic.gree,partic.blue)
            punto2 = (partic.DestinoX,partic.DestinoY,partic.red,partic.gree,partic.blue)

            puntos.append(punto1)
            puntos.append(punto2)
        return puntos
    
    def get_grafo(self):
        g = Grafo()
        for partic in self.__particulas:
            punto1 = (partic.OrigenX,partic.OrigenY,partic.red,partic.gree,partic.blue)
            punto2 = (partic.DestinoX,partic.DestinoY,partic.red,partic.gree,partic.blue)
            nodo_origen = Nodo(punto1)
            nodo_destino = Nodo(punto2)
            ponderacion = partic.distancia
            arista = AristaNoDirigida(nodo_origen,nodo_destino,ponderacion)
            g.agregar_arista(arista)
        return g
 #  ordenamiento
    def ordenart_id(self):
        self.__particulas.sort(key=lambda particu: particu.id)

    def ordernar_Veloc(self):
       self.__particulas.sort(key=lambda particu: particu.Velocidad)

    def ordenar_Distan(self):
        self.__particulas.sort(key=lambda particu: particu.distancia,reverse=True)

    
    def mostrar(self):
        for p in self.__particulas:
            print(p)
    #sobrecarga para que acepte el tipo de dato
    def __str__(self):
        return "".join(str(p) + "\n" for p in self.__particulas) 
    
    #sobrecarga por que no acepta que metan dentro listas
    def __len__(self):
        return(
            len(self.__particulas)
        )
    
    def __iter__(self):
        self.cont = 0

        return self
    
    def __next__(self):
        if self.cont < len(self.__particulas):
            molecula = self.__particulas[self.cont]
            self.cont += 1
            return molecula
        else:
            raise StopIteration
        
    def Abrir(self,ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
                return 1
        except:
            return 0 
        
    def Guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
                #archivo.write(str(self))
                return 1
        except:
            return 0
