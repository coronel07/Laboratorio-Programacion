# Clase base Vehiculo - Ejemplo de Abstracción
class Vehiculo():
    def __init__(self, marca, modelo, año):
        # Encapsulamiento: los atributos están ocultos (prefijo __) y se acceden a través de métodos.
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    # Encapsulamiento: Uso de getters y setters para acceder a los atributos privados.
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_año(self):
        return self.__año

    def set_año(self, año):
        self.__año = año

    def detener(self):
        # Este método se sobrescribe en las clases derivadas, lo que es un ejemplo de cómo se pueden especializar los comportamientos.
        print(f"El vehículo {self.get_marca()} {self.get_modelo()} se está deteniendo.")

# Herencia
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.__puertas = puertas

    def get_puertas(self):
        return self.__puertas

    def set_puertas(self, puertas):
        self.__puertas = puertas

    # Polimorfismo
    def acelerar(self):
        print(f"El auto {self.get_marca()} {self.get_modelo()} está acelerando.")

# Herencia
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.__cilindrada = cilindrada

    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    # Polimorfismo.
    def acelerar(self):
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} con cilindrada de {self.get_cilindrada()}cc está acelerando.")

# Herencia
class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.__capacidad_carga = capacidad_carga

    def get_capacidad_carga(self):
        return self.__capacidad_carga

    def set_capacidad_carga(self, capacidad_carga):
        self.__capacidad_carga = capacidad_carga

    # Polimorfismo
    def acelerar(self):
        print(f"La camioneta {self.get_marca()} {self.get_modelo()} con capacidad de carga {self.get_capacidad_carga()} está acelerando.")

    # Polimorfismo
    def detener(self):
        print(f"La camioneta {self.get_marca()} {self.get_modelo()} se está deteniendo.")

# Ejecución principal
if __name__ == "__main__":
    vehiculos = {
        "Corolla": Auto("Toyota", "Corolla", 2020, 4),
        "MT-07": Motocicleta("Yamaha", "MT-07", 2019, 689),
        "F-150 Raptor": Camioneta("Ford", "F-150 Raptor", 2023, 3244)
    }

    # Ejemplo de Polimorfismo
    for modelo, vehiculo in vehiculos.items():
        vehiculo.acelerar()
