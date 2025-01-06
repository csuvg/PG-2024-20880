class Parqueo:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.espacios_disponibles = capacidad
        self.vehiculos_estacionados = []
        self.dia_actual = 0
        self.pila_espera = []
        self.vehiculos_sin_atender = []
        self.maximoparqueados = 0
        
    def restart(self):
        self.pila_espera = []
        self.vehiculos_sin_atender = []
        self.vehiculos_estacionados = []
        self.espacios_disponibles = self.capacidad
    
    def get_parqueos_libres(self):
        return self.capacidad - self.maximoparqueados

    def sacar_tarde(self, vehiculo):
        if vehiculo in self.pila_espera:
            self.pila_espera.remove(vehiculo)
            if vehiculo.id not in self.vehiculos_sin_atender:
                self.vehiculos_sin_atender.append(vehiculo.id)
            #print(f"{vehiculo.id} ha salido del estacionamiento por no haber sido atendido a tiempo.")
    
    def calcularmaximo(self):
        if len(self.vehiculos_estacionados) > self.maximoparqueados:
            self.maximoparqueados = len(self.vehiculos_estacionados)
    
    def ingresar_vehiculo(self, vehiculo,texto=""):
        if not vehiculo.ya_entro and not vehiculo.ya_salio: 
            if self.espacios_disponibles > 0:
                if vehiculo.salir_tiempo_libre:
                    vehiculo.tiempo_salida = vehiculo.tiempo_salida_back_up
                vehiculo.ya_entro = True
                self.vehiculos_estacionados.append(vehiculo)
                self.espacios_disponibles -= 1
                self.calcularmaximo()
                #print(f"{vehiculo.id} ha sido estacionado"+texto+".")
            else:
                if vehiculo not in self.pila_espera:
                    self.pila_espera.append(vehiculo)
                    #print("El estacionamiento está lleno. No se puede estacionar el vehículo.")
    
    def sacar_vehiculo(self, vehiculo):
        if vehiculo in self.vehiculos_estacionados:
            if not vehiculo.salir_tiempo_libre:
                vehiculo.ya_salio = True
                vehiculo.tiempo_salida = vehiculo.tiempo_salida_back_up
            self.vehiculos_estacionados.remove(vehiculo)
            self.espacios_disponibles += 1
            #print(f"{vehiculo.id} ha salido del estacionamiento.")
            self.siguiente_pila()
        else:
            if vehiculo.id not in self.vehiculos_sin_atender and vehiculo in self.pila_espera:
                self.vehiculos_sin_atender.append(vehiculo.id)
                print("¿Cuando debe entrar aqui?")
            #print(f"{vehiculo.id} no está estacionado en este parqueo.")
        
    def siguiente_pila(self):
        if len(self.pila_espera) > 0:
            vehiculo = self.pila_espera.pop(0)
            texto_adicional = f" luego de esperar {vehiculo.get_tiempo_esperado_por_dia(self.dia_actual)} minutos "
            self.ingresar_vehiculo(vehiculo,texto_adicional)
    
    def get_carros_fuera(self):
        return len(self.vehiculos_sin_atender)
    
    def return_estacionados(self):
        return self.vehiculos_estacionados      
    
    def return_pila_espera(self):
        return self.pila_espera  
    
    def __len__(self):
        return self.capacidad
    
    def __str__(self):
        return f"Parqueo con capacidad para {self.capacidad} vehículos, {self.espacios_disponibles} espacios disponibles."

