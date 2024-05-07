class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        def descripcion(self):
            return f"{self.nombre}: ${self.precio}"