from modelo import Articulo

class ControladorArticulo:
    def __init__(self):
        self.articulo = None

    def establecer_precio(self, precio):
        self.articulo = Articulo(precio)

    def calcular_descuento(self):
        if self.articulo is None:
            raise ValueError("El artículo no ha sido establecido.")
        precio = self.articulo.get_precio()
        descuento = precio * 0.10
        precio_final = precio - descuento
        return descuento, precio_final
