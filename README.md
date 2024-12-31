# Desarrollar una herramienta para estimar la cantidad adecuada en la venta de espacios de estacionamiento y maximizar las ganancias

## Descripción
Determinar la cantidad óptima de asignaciones de parqueo a vender en una universidad es un desafío complejo. Esto se debe a que los horarios de los estudiantes cambian cada semestre, lo que dificulta utilizar los datos históricos como referencia confiable. Por ello, esta herramienta utiliza una simulación basada en agentes para estimar la cantidad adecuada de asignaciones, considerando los resultados de múltiples simulaciones. Estas simulaciones emulan varios días de operación en un parqueo, con diferentes horarios y poblaciones, lo que permite determinar de manera precisa la cantidad ideal de asignaciones a vender.

## Instrucciones de Instalación

### Requisitos Previos
- Python 3.8 o superior.


### Pasos para la Instalación
1. Clonar el repositorio:
   ```bash
   git clone <url_del_repositorio>
   cd <nombre_del_repositorio>
   ```
2. Instalar las dependencias del archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Establelcer los parámetros de la simulación (`src/Main.py`):
- horario_color: Diccionario que permitira establecer el color con el que se reconocerán a los agentes en la simulación, la llave debera ser el color que se desea que la librería de Mathplotlib utilice y el valor sería un arreglo con el inicio y fin del horario. El inicio y fin deberá de ser en minutos

- Cantidad_estacionamientos: Cuantos estacionamientos se desea simular

- inicio_simulacion: A partir de que hora del día debera de iniciar la simulación, esta debe ser en minutos.

- Tiempo_habil: Cúanto tiempo estará operando el parqueo.

- unidadtiempo: La unidad de tiempo que debera utilizar la unidad, esta debe de ser en minutos

- Dias: La cantidad de días que se desea emular

### Ejecución de la Aplicación
Para ejecutar el sistema, sigue los pasos:
1. Ejecutar la simulación:
   ```
   python src/Main.py
   ```
2. Analizar los resultados utilizando el módulo de análisis:
   ```
   jupyter notebook src/Analisis.ipynb
   ```
3. Revisa los resultados generados en la carpeta `src/`.

### Ejecución de Simulación especifica
En caso de ya tener los horariios y la población exacta se puede utilizar    ```bash
   python src/Main resultados.py``` 
   el cual tiene los mismos parámetros que se utiliza en `src/Main.py`, con un parámetro más el cual sirve para especificar la cantidad exacta de personas pertenecientes a cada horario.

## Demo
En la carpeta [demo](https://github.com/Aristondo01/PG-2024-20880/tree/main/demo) se encuentra un archivo .zip que contiene el video que muestra el sistema en acción. Accede a él para ver cómo funciona el proyecto y resolver cualquier duda en forma de tutorial.

## Informe Final
El informe final del proyecto está disponible en la carpeta [docs](https://github.com/Aristondo01/PG-2024-20880/tree/main/docsc) bajo el nombre `informe_final.pdf`. Este documento detalla el desarrollo, los resultados y las conclusiones del trabajo.

## Estructura del Repositorio
- `/src/`: Contiene los scripts principales y los archivos necesarios para ejecutar el sistema.
- `/demo/`: Incluye el video demostrativo del proyecto.
- `/docs/`: Contiene el informe final del proyecto.

## Autor
Proyecto desarrollado como parte del trabajo de graduación de Sebastián Aristondo Pérez, dentro de la Universidad Del Valle de Guatemala
