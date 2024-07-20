from modelo import Triangulo

class ControladorTriangulo:
    def __init__(self):
        self.triangulo = None
    
    def calcular_area(self, base, altura):
        self.triangulo = Triangulo(base, altura)
        return self.triangulo.calcular_area()
