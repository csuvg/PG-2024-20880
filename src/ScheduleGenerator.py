import random
from Vehiculo import Vehiculo
from utils import insertar_vehiuclo_csv

def generateVehicleSchedule(Horarios,epsilon,Cantidad_vehiculos,unidadtiempo = 10,periodo = 40,horario_color={}):
    #Horarios: Lista con los horarios de los vehiculos
    #Distribucion: Lista con la distribucion de los vehiculos
    #porcentajes: Lista con los porcentajes de los vehiculos
    #Retorna una lista con los horarios de los vehiculos
    random.seed(42)
    Vehiculos = []
    
    inicio = 0
    for h in Horarios:
        fin = inicio + int(Cantidad_vehiculos*h[2])
            
        for i in range(inicio,fin):
            tiempo_entrada = h[0]
            tiempo_salida = h[1]
            tiempo_entradaf = int(random.randint(tiempo_entrada,tiempo_entrada+(epsilon*unidadtiempo))//unidadtiempo*unidadtiempo)
            tiempo_salidaf = int(random.randint(tiempo_salida-(epsilon*unidadtiempo),tiempo_salida)//unidadtiempo*unidadtiempo)
            tiempolibres = generar_periodos(tiempo_entradaf, tiempo_salidaf,unidadtiempo,periodo)
            Vehiculos.append(Vehiculo(str(i), tiempo_entradaf, tiempo_salidaf,epsilon,unidadtiempo,tiempolibres,horario_color))
        inicio = fin
        
            
    return Vehiculos
    
    
    

def generar_periodos(limite_inferior, limite_superior,unidadtiempo,periodo):
    # Generar un número aleatorio entre los límites dados
    limite_inferior =  limite_inferior + periodo
    iniciolibre = random.uniform(limite_inferior, limite_superior)
    iniciolibre = int(iniciolibre // unidadtiempo) * unidadtiempo
    # Redondear al múltiplo de 10 más cercano
    numero_redondeado = round(iniciolibre / unidadtiempo) * unidadtiempo
    
    # Generar un valor aleatorio entre 1 y 5 con distribución uniforme
    cant_periodos = random.randint(1, 5)
    
    if iniciolibre + periodo * cant_periodos > limite_superior:
        # Si el tiempo de salida es mayor al límite superior, se ajusta el tiempo de salida
        regreso = limite_superior - periodo - unidadtiempo
    else:
        regreso = iniciolibre + periodo * cant_periodos
    
    prob = random.randint(1, 5)
    if prob == 3:
        
        return [iniciolibre, regreso] 
    else:
        return []

