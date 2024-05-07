from ProductoNormal import ProductoNormal
from ProductoDescuento import ProductoDescuento

class FabricaProducto:
    def crear_producto(self, nombre, precio, descuento=None):
        if descuento:
            return ProductoDescuento(nombre, precio, descuento)
        else:
            return ProductoNormal(nombre, precio)