from Vehiculo import Vehiculo
class Motocicleta(Vehiculo):
    def conducir(self):
        print(f"Conduciendo la motocicleta {self.marca} {self.modelo}")