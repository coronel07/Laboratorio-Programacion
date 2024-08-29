class Vehiculo():
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def detener(self):
        print(f"El vehículo {self.get_marca()} {self.get_modelo()} se está deteniendo.")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.__puertas = puertas

    def detener(self):
        print(f"El auto {self.get_marca()} {self.get_modelo()} se está deteniendo.")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.__cilindrada = cilindrada

    def detener(self):
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} se está deteniendo.")

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.__capacidad_carga = capacidad_carga

    def detener(self):
        print(f"La camioneta {self.get_marca()} {self.get_modelo()} se está deteniendo.")

if __name__ == "__main__":
    vehiculos = {
        "Corolla": Auto("Toyota", "Corolla", 2020, 4),
        "MT-07": Motocicleta("Yamaha", "MT-07", 2019, 689),
        "F-150 Raptor": Camioneta("Ford", "F-150 Raptor", 2023, 3244)
    }

    for modelo, vehiculo in vehiculos.items():
        vehiculo.detener()
