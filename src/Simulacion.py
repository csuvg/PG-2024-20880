import random
from Vehiculo import Vehiculo
from Parqueo import Parqueo
from utils import *
from PIL import Image
from Statistics import Statistics
import os 


def Simular(inicio_simulacion, Tiempo_habil, unidadtiempo, Cantidad_vehiculos, Cantidad_estacionamientos,Vehiculos,Dias,bandera_graficar=True,duracion_periodo = 40,nomgif = 'output'):
    random.seed(42)
    Parqueos = Parqueo(Cantidad_estacionamientos)
    Statistica = Statistics()
    Statistica.get_color(Vehiculos)

    for dia in range(Dias):
        for tiempo in range(inicio_simulacion,Tiempo_habil,unidadtiempo):
            if bandera_graficar:
                graficar(Parqueos.return_estacionados(),Parqueos.return_pila_espera(),tiempo,Cantidad_estacionamientos, dia,Cantidad_estacionamientos)
            Parqueos.dia_actual = dia
            for vehiculo in Vehiculos:
                vehiculo.tiempo_transcurrido(tiempo)
                vehiculo.realizar_acciones(tiempo,duracion_periodo,dia)
                if vehiculo in Parqueos.return_pila_espera():
                    if vehiculo.tiempo_dentro >= vehiculo.tiempo_salida:
                        Parqueos.sacar_tarde(vehiculo)
                    else:
                        Parqueos.ingresar_vehiculo(vehiculo)
                    vehiculo.tiempo_esperado(dia,unidadtiempo)
                if vehiculo.Listo_salir():
                    Parqueos.sacar_vehiculo(vehiculo)
                if tiempo >= vehiculo.tiempo_entrada:
                    Parqueos.ingresar_vehiculo(vehiculo)
        
        #print(f"Fin del día {dia}.")    
        Statistica.insertar_fila(dia,Vehiculos,Parqueos)
        
        for vehiculo in Vehiculos:
            vehiculo.nuevo_dia(dia+1)  
        Parqueos.restart()       
        
                
    #print("Simulación terminada.")
    Statistica.transform_to_csv()
    Statistica.replicar_carros(Vehiculos)


    if bandera_graficar:
        log = ''
        for c in Vehiculos:
            for dia in range(Dias):
                log+= f"El vehículo {c.id} esperó {c.get_tiempo_esperado_por_dia(dia)} minutos el día {dia}.\n"
                log+= c.get_acciones(dia)
        # Guardar el log en un archivo de texto
        with open('src/log.txt', 'w',encoding='utf-8') as file:
            file.write(log)
        print("Log guardado en 'log.txt'.")



    # Directorio que contiene las imágenes
    image_folder = './Imagenes/'

    # Lista para almacenar las imágenes
    images = []

    if bandera_graficar:
        for day in range(Dias):
            for number in range(inicio_simulacion,Tiempo_habil,unidadtiempo):
                filename = f'D{day}P{number}.png'
                if filename.endswith(('.png', '.jpg', '.jpeg')):
                    img_path = os.path.join(image_folder, filename)
                    img = Image.open(img_path)
                    images.append(img)


    if images:
        # Guardar las imágenes en un archivo GIF
        gif_path = nomgif+'.gif'
        images[0].save(gif_path, save_all=True, append_images=images[1:], duration=Dias * 180, loop=0)

        print(f"GIF creado con éxito: {gif_path}")
    else:
        if bandera_graficar:
            print("No se encontraron imágenes en el directorio especificado.")