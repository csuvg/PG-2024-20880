import matplotlib.pyplot as plt
import math
import os
from matplotlib.patches import Rectangle
import pandas as pd


import itertools

def limpiar_log():
    with open('src/log.txt', 'w',encoding='utf-8') as file:
        file.write('')
        
    df = pd.DataFrame(columns=['Día', 'Tiempo esperado total','Tiempo minimo esperado','Tiempo maximo esperado', 'Parqueos Libres', 'Carros sin antender','Almorzaron','Cantidad alumnos','Cantidad parqueos','Salidas por periodos libres','Parametros'])
    df.to_csv('src/Statistics.csv',index=False)    
    df = pd.DataFrame(columns=['Hora inicio','Hora fin','Inicio tiempo libre','Fin tiempo libre','Parametros'])
    df.to_csv('src/StudentsCreation.csv',index=False)

def insertar_vehiuclo_csv(hora_inicio,hora_fin,inicio_tiempo_libre,fin_tiempo_libre,parametros):
    df = pd.read_csv('src/StudentsCreation.csv')
    
    # Crea un nuevo DataFrame con la nueva fila
    nuevo_registro = pd.DataFrame([{
        'Hora inicio': hora_inicio,
        'Hora fin': hora_fin,
        'Inicio tiempo libre': inicio_tiempo_libre,
        'Fin tiempo libre': fin_tiempo_libre,
        'Parametros': parametros
    }])

    # Concatenar el nuevo registro al DataFrame existente
    df = pd.concat([df, nuevo_registro], ignore_index=True)
    df.to_csv('src/StudentsCreation.csv',index=False)


def generar_combinaciones(rango, limiteSup, limiteInf, num_elementos):
    # Crear lista de valores posibles para las proporciones
    valores_posibles = [round(i * rango, 2) for i in range(int(limiteSup / rango) + 1)]
    
    # Generar todas las combinaciones posibles
    combinaciones = [
        comb for comb in itertools.product(valores_posibles, repeat=num_elementos)
        if sum(comb) == 1.0 and all(limiteInf <= x <= limiteSup for x in comb)  # Filtrar combinaciones donde la suma es 1.0 y los valores están dentro de los límites
    ]
    
    # Eliminar combinaciones repetidas sin importar el orden
    combinaciones_unicas = set(tuple(sorted(comb)) for comb in combinaciones)
    
    # Convertir el conjunto de nuevo a una lista de combinaciones
    return combinaciones

def convertir_tiempo(minutos,dia):
    # Calcular el número de horas
    horas = minutos // 60
    
    # Calcular el número de minutos
    minutos = (minutos % 60) 
    
    return f"Día: {dia}  Hora:{horas:02}:{minutos:02}"


def graficar(array_parqueos, array_espera, tiempo, m, dia, tam_pila):
    
    aumento = (tam_pila + m)// 2 % 10
    aumento += 1
    
    # Crear la carpeta 'Imagenes' si no existe
    if not os.path.exists('Imagenes'):
        os.makedirs('Imagenes')    

    # Calculamos la dimensión de la cuadrícula para el parqueo
    n_parqueo = math.ceil(math.sqrt(m))

    # Calculamos la dimensión de la cuadrícula para la pila
    n_pila = math.ceil(math.sqrt(tam_pila))

    # Crear la figura y los ejes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12+ aumento, 6 + aumento))

    # Ajustar los límites de la cuadrícula del parqueo
    ax1.set_xlim(0, n_parqueo )
    ax1.set_ylim(0, n_parqueo )

    # Ajustar los límites de la cuadrícula de la pila
    ax2.set_xlim(0, n_pila )
    ax2.set_ylim(0, n_pila )

    fig.suptitle(convertir_tiempo(tiempo, dia), fontsize=16)

    # Dibujar la cuadrícula de parqueos
    cantidad = 0
    for row in range(n_parqueo):
        for col in range(n_parqueo):
            if cantidad < m:
                ax1.add_patch(Rectangle((col, n_parqueo - row - 1), 1, 1, edgecolor='black', facecolor='none'))
                cantidad += 1
        if cantidad >= m:
            break

    
    tam_fig = 14
    tam_let = 8
    
    # Dibujar los parqueos en la cuadrícula
    for i, item in enumerate(array_parqueos):
        if i < m:
            row = i // n_parqueo
            col = i % n_parqueo
            if item:
                color = item.return_color()
                edgecolor = item.return_edgecolor()
                ax1.plot(col + 0.5, n_parqueo - row - 0.5, 'o', color=color,markeredgecolor = edgecolor, markersize=tam_fig)
                ax1.text(col + 0.4, n_parqueo - row - 0.5, f'{item.id}', fontsize=tam_let, verticalalignment='center')

    # Dibujar la cuadrícula de la pila de espera
    cantidad = 0
    for row in range(n_pila):
        for col in range(n_pila):
            if cantidad < tam_pila:
                ax2.add_patch(Rectangle((col, n_pila - row - 1), 1, 1, edgecolor='red', facecolor='none'))
                
                cantidad += 1
        if cantidad >= tam_pila:
            break

    # Dibujar la pila de espera en la cuadrícula
    for i, item in enumerate(array_espera):
        if i < tam_pila:
            row = i // n_pila
            col = i % n_pila
            if item:
                color = item.return_color()
                edgecolor = item.return_edgecolor()
                ax2.plot(col + 0.5, n_pila - row - 0.5, 'o', color=color, markeredgecolor = edgecolor , markersize=tam_fig)
                ax2.text(col + 0.4, n_pila - row - 0.5, f'{item.id}', fontsize=tam_let, verticalalignment='center')

    # Centrar las cuadrículas en las subgráficas
    ax1.set_aspect('equal')
    ax2.set_aspect('equal')

    # Remover ejes
    ax1.axis('off')
    ax2.axis('off')


    # Mostrar la gráfica
    iteracion = tiempo
    plt.savefig(f'Imagenes/D{dia}P{iteracion}.png', bbox_inches='tight')
    plt.close()
