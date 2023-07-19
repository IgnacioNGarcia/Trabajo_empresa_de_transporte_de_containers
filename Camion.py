class Camion():
    def __init__(self, id):
        self.__disponible = True
        self.__id = id # GenerarId.generar_numeros_distintos()
        self.__contenedor = None
    ''
    'Getters y setters:'
    def get_disponible(self):
        return self.__disponible
    def set_disponible(self,d):
        self.__disponible = d
    disponible = property(get_disponible,set_disponible)
    
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id = id
    id = property(get_id,set_id)
    
    def get_contenedor(self):
        return self.__contenedor
    def set_contenedor(self,cont):
        self.__disponible = False
        self.__contenedor = cont
    contenedor = property(get_contenedor,set_contenedor)
    'Fin Getters y setters:'
    
    
    def viajar(self):
        self.set_disponible(True)

    def descargar(self):
        self.set_contenedor(None)