from Vehiculo import Vehiculo
class Automovil(Vehiculo):
    def conducir(self):
        print(f"Conduciendo el automóvil {self.marca} {self.modelo}")