from BarcosDirectorio.Barcos import Barco
from Camion import Camion
from Contenedores import Contenedor
from Estados import EstadoMenor100, EstadoMenor1000, EstadoMas10000, EstadoMenor10000
from Pedidos import Pedidos
from Excepciones.exceptions import *

from typing import List
import random

"""
ESTA CLASE CONTIENE LOS DATOS IMPORTANTES DE EMPRESA A USAR. COMO LOS BARCOS, CAMIONES, Y CONTENEDORES A
DISPOCISION, JUNTO CON METODOS COMO actualizar_barco_trotamundo_o_sedentario() POR EJEMPLO, PARA
RESOLVER COSAS QUE SE PIDEN EXPLICITAMENTE PARA LA APLICACION.
"""


class EmpresaData():
    def __init__(self, barcos: List[Barco], camiones: List[Camion]):
        self.__camiones = camiones
        self.__barcos = barcos
        
        
        # para puntos 3 y 4 de SE PIDE
        self.__barco_con_mas_km = None
        self.__barco_con_menos_km = None
        
        self.__contenedores = []
        
        


    'Getters y Setters'
    
    
    def get_contenedores(self):
        return self.__contenedores
    
    def set_contenedores(self, contenedores):
        self.__contenedores = contenedores
    contenedores = property(get_contenedores,set_contenedores)
    
    def get_barcos(self):
        return self.__barcos
    
    def set_barcos(self, barcos):
        self.__barcos = barcos
    barcos = property(get_barcos,set_barcos)
    
    def get_camiones(self):
        return self.__camiones
    
    def set_camiones(self, camiones):
        self.__camiones = camiones
    camiones = property(get_camiones,set_camiones)

    
    def get_barco_con_mas_km(self):
        
        return self.__barco_con_mas_km
    
    def set_barco_con_mas_km(self, barcos):
        self.__barco_con_mas_km = barcos
    barco_con_mas_km = property(get_barco_con_mas_km,set_barco_con_mas_km)


    
    def get_barco_con_menos_km(self):
      
        return self.__barco_con_menos_km
    
    def set_barco_con_menos_km(self, barcos):
        self.__barco_con_menos_km = barcos
    barco_con_menos_km = property(get_barco_con_menos_km,set_barco_con_menos_km)
    
    def devolver_un_barco_disponible(self):          
        for barco in self.get_barcos():
            if (barco.get_disponible()):
                #segun la teoria, esto afecta a la lista de empresa de self.camiones en cualquier parte del codigo
                barco.set_disponible = False
                return barco
        # falta ver donde se catchea esta excepcion (sacar este comentario cuando ya este)
        raise No_hay_barcos_disponibles("En este momento no hay barcos disponibles")
    
    
    
    def devolver_un_camion_disponible(self):          
        for camion in self.get_camiones():
            if (camion.get_disponible()):
                #segun la teoria, esto afecta a la lista de empresa de self.camiones en cualquier parte del codigo
                camion.set_disponible = False
                return camion
        # falta ver donde se catchea esta excepcion (sacar este comentario cuando ya este)
        raise No_hay_camiones_disponibles("En este momento no hay camiones disponibles")
    
    
    def actualizar_barco_trotamundo_o_sedentario(self):
        
        bmenos = self.get_barco_con_menos_km()
        bmas = self.get_barco_con_mas_km()
        
        for barco in self.get_barcos():
            # actualizo barco sedentario
            if barco.get_km_recorridos() < bmenos or bmenos.get_km_recorridos() == 0:
                self.set_barco_con_menos_km(barco)
            
            # actualizo barco trotamundo
            if barco.get_km_recorridos() > bmas:
                self.set_barco_con_mas_km(barco)
        
        return
    
                
           
    #El container que mayor cantidad de veces viajó completo con una única carga.
    def container_con_mas_viajes_con_una_carga(self):
        container_mas_viajes = Contenedor()
        aux = 0

        for contenedor in self.contenedores:
            if contenedor.get_cant_de_veces_comple_y_carga_unica() > aux:
                aux = contenedor.get_cant_de_veces_comple_y_carga_unica()
                container_mas_viajes = contenedor
        
        return container_mas_viajes