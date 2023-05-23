import math

# x1 = origen1
# x2 = origen2
# y1 = destino1
# y2 = destino2
def distancia_euclidiana(x1,y1,x2,y2):

    calcula = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return calcula

def get_poit_near(list_particulas)-> list:
        resultado  = []

        for punto_i in list_particulas:
            x1 = punto_i[0]
            y1 = punto_i[1]
            min = 1000 
            cercano = (0,0)
            for punto_j in list_particulas:
                if punto_i != punto_j:
                    x2 = punto_j[0] 
                    y2 = punto_j[1]
                    d =  distancia_euclidiana(x1, y1, x2, y2)
                    if d < min:
                        min = d
                        cercano = (x2, y2)
            resultado.append((punto_i, cercano))            
        return resultado