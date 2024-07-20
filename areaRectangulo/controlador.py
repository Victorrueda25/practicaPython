from modelo import Rectangulo

class ControladorRectangulo:
    def __init__(self):
        self.rectangulo = None

    def establecer_lado(self, base, altura):
        self.rectangulo = Rectangulo(base, altura)

    def calcular_area(self):
        if self.rectangulo is None:
            raise ValueError("El rectángulo no ha sido establecido.")
        return self.rectangulo.base * self.rectangulo.altura
