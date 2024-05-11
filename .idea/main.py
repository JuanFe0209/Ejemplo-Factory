from FabricaVehiculo import FabricaVehiculos
def main():
    fabrica = FabricaVehiculos()

    vehiculo1 = fabrica.fabricar_vehiculo("automovil", "Toyota", "Corolla")
    vehiculo1.conducir()

    vehiculo2 = fabrica.fabricar_vehiculo("motocicleta", "Honda", "CBR600RR")
    vehiculo2.conducir()

if __name__ == "__main__":
    main()
