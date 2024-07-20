from modelo import Cuadrado

class ControladorCuadrado:
    def __init__(self):
        self.cuadrado = None
    
    def establecer_lado(self, lado):
        self.cuadrado = Cuadrado(lado)
    
    def calcular_area(self):
        if self.cuadrado is None:
            raise ValueError("El lado del cuadrado no ha sido establecido.")
        return self.cuadrado.lado ** 2
