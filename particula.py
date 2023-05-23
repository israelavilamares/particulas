from algoritmo import distancia_euclidiana


class Particula:
    def __init__(self, id = 0,origen_x = 0,origen_y = 0,destino_x = 0,destino_y = 0, velocidad = 0, red = 0 ,gree = 0,blue = 0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red 
        self.__gree = gree  
        self.__blue = blue 
        self.distancia = distancia_euclidiana(origen_x,destino_x,origen_y,destino_y)

    #retorna las salida de los datos en string la funciono str 
    def __str__(self) -> str:
        return(
            
            "id: " + str(self.__id) + "\n"
            "origen_x: " + str(self.__origen_x) + "\n" +
            "origen_y: " + str(self.__origen_y) + "\n" +
            "destino_x: " + str(self.__destino_x) + "\n" +
            "destino_y: " + str(self.__destino_y) + "\n" +
            "velocidad: " + str(self.__velocidad) + "\n" +
            "red: " + str(self.__red) + "\n" + 
            "gree: " + str(self.__gree) + "\n" +
            "blue: " + str(self.__blue) + "\n" + 
            "distancia: " + str(self.distancia) + "\n"
        )
    @property
    def id(self):
        return self.__id
    @property
    def OrigenX(self):
        return self.__origen_x
    @property
    def OrigenY(self):
        return self.__origen_y
    @property
    def DestinoX(self):
        return self.__destino_x
    @property
    def DestinoY(self):
        return self.__destino_y
    @property
    def Velocidad(self):
        return self.__velocidad
    @property
    def red(self):
        return self.__red
    @property
    def gree(self):
        return self.__gree
    @property
    def blue(self):
        return self.__blue
    

    #convierte los valores a diccionario se utiliza para 
    #hacer un archivo JSON  
    def to_dict(self):
        return{
            "id": self.__id,
            "origen_x": self.__origen_x,
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "gree": self.__gree,
            "blue": self.__blue
        }
    