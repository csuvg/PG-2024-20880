import random
import numpy as np
from datetime import timedelta
from utils import *


class Vehiculo:
    def __init__(self, id, tiempo_entrada, tiempo_salida,epsilon,unidadtiempo = 10,tiemposLibres = [], horario_color ={}):
        # random.seed(42)
        np.random.seed(42)
        self.tiempo_espera = 0
        self.tiempo_dentro = 0
        self.id = "P"+id
        self.offsetSalidaAlmuerzo = 0
        self.salir_tiempo_libre = False
        self.TiemposLibres = tiemposLibres
        self.tiempo_entrada = tiempo_entrada
        self.tiempo_salida = tiempo_salida
        self.unidadtiempo = unidadtiempo
        self.tiempo_entrada_back_up = self.tiempo_entrada
        self.tiempo_salida_back_up = self.tiempo_salida
        self.horario_color = horario_color
        
        #print(f"El vehiculo {self.id} entra a las {convertir_tiempo(self.tiempo_entrada,0)} y sale a las {convertir_tiempo(self.tiempo_salida,0)}")
        
        
        self.ya_salio = False
        self.ya_entro = False
        self.almuerzoinf = self.hora_a_minutos("11:30:00")
        
        self.almuerzosup = self.hora_a_minutos("15:00:00")
        
        
        self.tiempo_esperado_diccionario = {}
        self.acciones = {}
        self.acciones[0] = ""
        self.acciones[1] = ""
        
        self.calculated_color()
        
        if self.almuerzoinf <= self.tiempo_salida <= self.almuerzosup:
            self.Almorzar(dia=0,p=0.5)
        
        
    
    def nuevo_dia(self,dia):
        self.ya_salio = False
        self.ya_entro = False
        self.salir_tiempo_libre = False
        self.tiempo_espera = 0
        self.tiempo_dentro = 0
        
        self.tiempo_entrada = self.tiempo_entrada_back_up
        self.tiempo_salida = self.tiempo_salida_back_up
        self.calculated_color()
        self.acciones[dia+1] = ""
        
        
        if self.almuerzoinf <= self.tiempo_salida <= self.almuerzosup:
            self.Almorzar(dia=dia)
        
    def get_tiempo_esperado_por_dia(self,dia):
        if dia not in self.tiempo_esperado_diccionario:
            return 0
        else:
            return self.tiempo_esperado_diccionario[dia]
    
    def get_acciones(self,dia):
        if dia not in self.acciones:
            return ""
        else:
            return self.acciones[dia]
    
    def tiempo_esperado(self,dia,tiempo):
        if dia not in self.tiempo_esperado_diccionario:
            self.tiempo_esperado_diccionario[dia] = tiempo
        else:
            self.tiempo_esperado_diccionario[dia] += tiempo
        
        self.tiempo_espera += tiempo
    
        
    def hora_a_minutos(self,hora):
        h, m, s = map(int, hora.split(':'))
        tiempo = timedelta(hours=h, minutes=m, seconds=s)
        return int(tiempo.total_seconds()/60)
        
    def Almorzar(self,dia,p= 0.5):
        # Distribución de Bernoulli utilizando la distribución binomial con un solo ensayo
        quedarse = np.random.binomial(1,p) 
        quedarse = True if quedarse == 1 else False
        if quedarse:
            self.offsetSalidaAlmuerzo = 60 #minutos
            self.acciones[dia] += f"El vehiculo {self.id} se quedo ha almorzar sale 1 hora más tarde el día {dia}\n"
            self.edgecolor= "green"
        else:
            self.offsetSalidaAlmuerzo = 0 #minutos
    
    def realizar_acciones(self,tiempo,duracionPeriodo,dia):
        self.TiempoLibre(tiempo,duracionPeriodo,dia)
    
    def TiempoLibre(self,tiempo,duracionPeriodo,dia,p=0.3,):
        
        if self.TiemposLibres == []:
            return
        
        Libre = False
        periodos_libres = 0
        

        if  self.TiemposLibres[0] == tiempo + self.unidadtiempo * 2:
            periodos_libres = int((self.TiemposLibres[1]-self.TiemposLibres[0])/duracionPeriodo)
            Libre = True
    
                
        if Libre:
            Decision = np.random.geometric(p)
            if Decision <= periodos_libres:
                
                self.tiempo_entrada = self.TiemposLibres[1]
                self.tiempo_salida = self.TiemposLibres[0]
                
                self.salir_tiempo_libre =  True
                self.ya_entro = False
                self.acciones[dia] += f"El vehiculo {self.id} se fue en un periodo libre a las {convertir_tiempo(tiempo,dia)}\n"
                self.acciones[dia] += f"El vehiculo {self.id} deberia de entrar nuevamente a las {convertir_tiempo(self.tiempo_entrada,dia)}\n"
                
                self.edgecolor ="purple"
            
            
        
    
    def tiempo_transcurrido(self,tiempo):
        self.tiempo_dentro = tiempo
    
    def Listo_salir(self):   
        
        if self.salir_tiempo_libre:
            return self.tiempo_dentro >= self.tiempo_salida
        
        return ((self.tiempo_dentro >= self.tiempo_salida + self.offsetSalidaAlmuerzo) and not self.ya_salio)
    
    def return_color(self):
        return self.color
    
    def return_edgecolor(self):
        return self.edgecolor
    
    
    def calculated_color(self):
        if self.horario_color == {}:
            self.default_calculated_color()
        else:
            for key in self.horario_color:
                horario = self.horario_color[key]
                if self.tiempo_entrada >= horario[0] and self.tiempo_salida <= horario[1]:
                    self.color = key
                    self.edgecolor = key
                    break
            
    def default_calculated_color(self):
        
        #Yellow 6:30 - 13:00
        if self.tiempo_entrada >= 390 and self.tiempo_salida <=780:
            self.color = 'yellow'
            self.edgecolor = 'yellow'
        #Orange 10:00 - 16:30
        elif self.tiempo_entrada >= 600 and self.tiempo_salida <= 990:
            self.color = 'orange'
            self.edgecolor = 'orange'
        #Red 15:30 - 22:00
        elif self.tiempo_entrada >= 930 and self.tiempo_salida <= 1320:
            self.color = 'red'
            self.edgecolor = 'red'
        else:
            self.color = 'skyblue'
            self.edgecolor = 'skyblue'
        
        
        

