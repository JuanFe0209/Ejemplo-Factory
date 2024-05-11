from Vehiculo import Vehiculo
from Automovil import Automovil
from Motocicleta import Motocicleta
class FabricaVehiculos:
    def fabricar_vehiculo(self, tipo, marca, modelo):
        if tipo == "automovil":
            return Automovil(marca, modelo)
        elif tipo == "motocicleta":
            return Motocicleta(marca, modelo)
        else:
            raise ValueError("Tipo de vehículo no válido")