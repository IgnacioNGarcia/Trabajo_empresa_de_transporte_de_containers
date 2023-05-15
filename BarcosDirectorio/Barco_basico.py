from Excepciones.exceptions import *
from BarcosDirectorio.Barcos import Barco
import sys
sys.path.insert(0,'ContenedoresDirectorio\Contenedor_basico_interfaz.py')
from ContenedoresDirectorio.Contenedor_basico_interfaz import Cont_basico_interfaz

class Barco_basico(Barco):
    def __init__(self, id, peso_max, cant_contenedores_max, lleva_mat_esp):
        super().__init__(id, peso_max, cant_contenedores_max, lleva_mat_esp)
    
    def puede_cargar_esta_carga(self, carga):
        if not (isinstance(carga, Cont_basico_interfaz)):
            raise Contenedor_no_aceptado_exception("Este barco solo puede llevar contenedores básicos")
        #Hay que ver como manejamos en la carga si lleva alguna carga especial o no.
        if not self.lleva_mat_esp and carga.get_mat_especial():
            raise Material_no_compatible_con_barco_Exceptionn("Este barco no puede llevar el material que se intenta cargar.")
        return True
        
    def tiene_lugar(self, carga):
        if self.contenedores.size() == self.cant_contenedores_max:
            raise Cantidad_contenedores_maxima_alcanzada_exception("El barco está lleno. No es posible cargar el contenedor.")
        
        if ( carga.get_peso() + self.obtener_peso_actual() )> self.peso_max:
            raise Peso_excedido_exception(f"Este peso es mucho para el barco. Sobran {self.obtener_peso_actual() + carga.get_peso() - self.peso_max} kgs")
        return True
    
    def cargar(self, carga):
        if self.puede_cargar_esta_carga(carga) and self.tiene_lugar(carga):
            self.contenedores.append(carga)
        
    