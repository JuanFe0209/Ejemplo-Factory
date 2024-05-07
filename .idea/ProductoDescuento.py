class ProductoDescuento(Producto):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.descuento = descuento
        def descripcion(self): precio_descuento = self.precio - self.descuento
        return f"{self.nombre} (Descuento): ${precio_descuento}"
