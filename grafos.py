from pprint import pprint, pformat
class Nodo:
    def __init__(self,dato) -> None:
        self.dato  = dato
#para hecer comparaciones
    def __eq__(self, other) -> bool:
        return self.dato == other.dato  
    
    def __str__(self) -> str:
        return f"dato : {self.dato}"
    #retorne el string y no el la direcion de memoria
    def __repr__(self) -> str:
        return f"Nodo({self.dato})"
    #para que no cambie en diccionario las llaves
    def __hash__(self) -> int:
        return hash(self.dato)
    
class Arista:
    def __init__(self,origen:Nodo ,destino:Nodo, ponderacion) -> None:
        self.origen = origen
        self.destino = destino
        self.distancia = ponderacion
    
    def __str__(self) -> str:
        return f"({self.origen}-------- {self.distancia} -------- ({self.desti}))"
    
    #hacer comparaciones
    def __eq__(self, other) -> bool:
        return self.origen == other.orige and self.destino == other.desti 
    
    def __repr__(self) -> str:
        return f"{repr(self.origen)} ------ {self.distancia} ------ {repr(self.desti)}"
class AristaNoDirigida(Arista):
    pass

class Grafo:
    def __init__(self) -> None:
        self.aristas = []
        #diccionario
        self.listaadya = {}
    def agregar_arista(self, arista:Arista):
        if arista not in self.aristas:
            self.aristas.append(arista)

    def elimina_arista(self,arista:Arista):
        self.aristas.remove(arista)

    def __str__(self) -> str:
        return str([arista for arista in self.aristas])

    def get_ListaAyd(self):
        self.listaadya.clear()
        grafo_noDirigido = {
            "Nodo origen": [["Nodo destino",'ponderacion']],
            "Nodo destino": [["Nodo origen",'ponderacion_']]

        }
        for arista in self.aristas:
            nodo_origen = arista.origen
            nodo_destino = arista.destino
            ponderacion = arista.ponderacion
            self.agregarDict(nodo_origen,nodo_destino,ponderacion)
            self.agregarDict(nodo_destino,nodo_origen,ponderacion)
        return self.listaadya


    def agregarDict(self,nodo_origen,nodo_destino,ponderacion):
        if nodo_origen not in self.listaadya:
            self.listaadya[nodo_origen] =  [[nodo_destino,ponderacion]]
        else: 
            self.listaadya[nodo_origen].append([nodo_destino,ponderacion])
    def print_list_adyacencia(self):
        self.listaadya.clear()
        self.get_ListaAyd()
        pprint(self.listaadya)
    def grafo_to_str(self):
        self.listaadya.clear()
        self.get_ListaAyd()
        s = pformat(self.listaadya)
        return s
    
