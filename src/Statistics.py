import pandas as pd

class Statistics:
    def __init__(self):
        self.df = pd.DataFrame(columns=['Día', 'Tiempo esperado total','Tiempo minimo esperado','Tiempo maximo esperado', 'Parqueos Libres', 'Carros sin antender','Almorzaron','Cantidad alumnos','Cantidad parqueos','Salidas por periodos libres','Parametros'])
        self.libres = 0
        self.df_replicar_carros = pd.DataFrame(columns=['Hora inicio','Hora fin','Inicio tiempo libre','Fin tiempo libre','Parametros'])
        
    def replicar_carros(self,carros):

        for c in carros:
            hora_inicio = c.tiempo_entrada
            hora_fin = c.tiempo_salida
            inicio_libre = 0
            fin_libre = 0
            if c.TiemposLibres != []:
                inicio_libre = c.TiemposLibres[0]
                fin_libre = c.TiemposLibres[1]
            
            self.df_replicar_carros.loc[len(self.df_replicar_carros)] = [hora_inicio,hora_fin,inicio_libre,fin_libre,self.colores]
        
        self.df_replicar_carros.to_csv('src/StudentsCreation.csv', index=False,mode= 'a',header=False, encoding='utf-8')            
        
        

    def get_almorzaron(self,carros,dia):
        contador = 0
        for c in carros:
            if c.offsetSalidaAlmuerzo > 0:
                contador +=1
        
        return contador
    
    def get_tiempo_esperado(self,carros,dia):
        tiempo_esperado = 0
        tiempo_minimo = 1440
        tiempo_maximo = 0
        for c in carros:
            valor = c.get_tiempo_esperado_por_dia(dia)
            self.libres += 1 if c.salir_tiempo_libre else 0
            tiempo_esperado += valor
            
            if valor < tiempo_minimo and valor != 0:
                tiempo_minimo = valor
            
            if valor > tiempo_maximo:
                tiempo_maximo = valor
        
        if tiempo_minimo == 1440:
            tiempo_minimo = 0
        return (tiempo_esperado,tiempo_minimo,tiempo_maximo)
    
    def get_parqueos_libres(self,parqueo):
        return parqueo.get_parqueos_libres()

    def get_carros_fuera(self,parqueo):
        return parqueo.get_carros_fuera()

    def get_color(self,carros):
        colores = {}
        
        for c in carros:
            if c.color not in colores:
                colores[c.color] = 1
            else:
                colores[c.color] += 1
        
        self.colores = colores

    def insertar_fila(self,dia,carros,parqueos):

        tiempo_esperado,tiempo_minimo,tiempo_maximo = self.get_tiempo_esperado(carros,dia)
        parqueos_libres = self.get_parqueos_libres(parqueos)
        carros_fuera = self.get_carros_fuera(parqueos)
        almorzaron = self.get_almorzaron(carros,dia)
        cantidad_carros = len(carros)
        cantidad_parqueos = len(parqueos)
        parametros = self.colores
        libres = self.libres
        
        #self.df = pd.DataFrame(columns=['Día', 'Tiempo esperado total','Tiempo minimo esperado','Tiempo maximo esperado', 'Parqueos Libres', 'Carros sin antender','Almorzaron','Cantidad alumnos','Cantidad parqueos','Parametros'])
        self.df.loc[len(self.df)] = [dia, tiempo_esperado,tiempo_minimo,tiempo_maximo, parqueos_libres, carros_fuera,almorzaron,cantidad_carros,cantidad_parqueos,libres,parametros]
        self.libres = 0
        
    def transform_to_csv(self):
        self.df.to_csv('src/Statistics.csv', index=False, mode='a', header= False, encoding='utf-8')


