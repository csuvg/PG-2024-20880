from Simulacion import *
from ScheduleGenerator import *


# Parámetros de la simulación
# Las llaves deben de ir en orden ascecendente
horario_color = {"yellow": [390,780], "orange": [600,990], "red": [930,1320],"skyblue": [390,1320]}
Cantidad_estacionamientos = 25
inicio_simulacion = 390 
graficarbandera = False
una_iteracion = False
Tiempo_habil = 1330
unidadtiempo = 10
epsilon = 2
Dias = 1

# Parámetros para generar combinaciones
rango = 0.05  # Paso de 5%
limiteSup = 0.40 # Límite superior
limiteInf = 0.10 # Límite inferior
num_elementos = 4  # Número de proporciones (elementos) a combinar

combinaciones = generar_combinaciones(rango,limiteSup,limiteInf, num_elementos)

print("Cantidad de combinaciones",len(combinaciones))

Horarios = []
horario_color_cantidad={}

amplificador = 2.5
salto = 4
total_iteraciones = len(combinaciones)*(int(Cantidad_estacionamientos*amplificador+1) - Cantidad_estacionamientos )// salto

print("Total de iteraciones: ",total_iteraciones)

#Para depurar
# Cantidad_estacionamientos = 20
# graficarbandera = True
# combinaciones = [[0.25,0.25,0.25,0.25]]
# total_iteraciones = 1
# Dias = 2
# una_iteracion = True
#----------------------------
cont_ite = 0
print ("Cantidad maxima de alumnos: ",Cantidad_estacionamientos*amplificador)
limpiar_log()
for combinacion in combinaciones:
    cont = 0
    Horarios = []
    for color in horario_color:
        Horarios.append((horario_color[color][0],horario_color[color][1],combinacion[cont]))   
        cont += 1
    
             
    for cv in range(Cantidad_estacionamientos,int(Cantidad_estacionamientos*amplificador)+1,salto):
        Cantidad_vehiculos = cv
        
        cont = 0
        for color in horario_color:
            horario_color_cantidad[color] = int(combinacion[cont] * Cantidad_vehiculos)
            cont += 1
        
        Vehiculos = generateVehicleSchedule(Horarios,epsilon,Cantidad_vehiculos,unidadtiempo,horario_color=horario_color)
        
    
        Simular(inicio_simulacion, Tiempo_habil, unidadtiempo, Cantidad_vehiculos, Cantidad_estacionamientos,Vehiculos,Dias,graficarbandera)
        cont_ite += 1
        porcentaje = int(cont_ite/total_iteraciones*100)
        if cont_ite % 100 == 0:
            print(f"Progreso: {cont_ite}/{total_iteraciones} ({porcentaje}%)")
        
        if una_iteracion:
            break
    
    # {yellow: [390,780], orange: [600,990], red: [930,1320], skyblue: [390,1320]}
    # {'yellow': 15, 'orange': 15, 'red': 25, 'skyblue': 45}
    # 6:30 - 13:00 : 15, 10:00 - 16:30: 15, 15:30 - 22:00: 25, 6:30 - 22:00: 45