from Simulacion import *
from ScheduleGenerator import *
from utils import limpiar_log


# Parámetros de la simulación
Cantidad_estacionamientos = 100
Cantidad_vehiculos = 170
inicio_simulacion = 390 
Tiempo_habil = 1330
unidadtiempo = 10
epsilon = 2
Dias = 2
graficarbandera = True

Horarios = []


combinacion = [0.35,0.10,0.35,0.1,0.1]

Horarios = [
    (390, 780, combinacion[0]),
    (600, 990, combinacion[1]),
    (410, 850, combinacion[4]),
    (930, 1320, combinacion[2]),
    (390, 1320, combinacion[3]),
]

horario_color = {'yellow': [390,780],'pink':[410,850], 'orange': [600,990], 'red': [930,1320], 'skyblue': [390,1320]}

limpiar_log()
Vehiculos = generateVehicleSchedule(Horarios,epsilon,Cantidad_vehiculos,unidadtiempo,horario_color=horario_color)
print("Cantidad de vehiculos",len(Vehiculos))
Simular(inicio_simulacion, Tiempo_habil, unidadtiempo, Cantidad_vehiculos, Cantidad_estacionamientos,Vehiculos,Dias,graficarbandera,nomgif="DEMO4c")
    
    # {yellow: [390,780], orange: [600,990], red: [930,1320], skyblue: [390,1320]}
    # {'yellow': 15, 'orange': 15, 'red': 25, 'skyblue': 45}
    # 6:30 - 13:00 : 15, 10:00 - 16:30: 15, 15:30 - 22:00: 25, 6:30 - 22:00: 45


# images = []
# image_folder = './Imagenes/'

# for day in range(Dias):
#     for number in range(inicio_simulacion,Tiempo_habil,unidadtiempo):
#         filename = f'D{day}P{number}.png'
#         if filename.endswith(('.png', '.jpg', '.jpeg')):
#             img_path = os.path.join(image_folder, filename)
#             img = Image.open(img_path)
#             images.append(img)


# if images:
#     # Guardar las imágenes en un archivo GIF
#     gif_path = 'output.gif'
#     images[0].save(gif_path, save_all=True, append_images=images[1:], duration=600, loop=0)
#     print(f"GIF creado con éxito: {gif_path}")
