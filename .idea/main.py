from FabricaProducto import FabricaProducto

def main():
    fabrica = FabricaProducto()
    producto1 = fabrica.crear_producto("Camisa", 25)
    producto2 = fabrica.crear_producto("zapato", 30, descuento= 10)

    print(producto1.descripcion())
    print(producto2.descripcion())

    if __name__ == "__main__":
        main()