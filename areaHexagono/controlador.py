from modelo import Hexagono

class ControladorHexagono:
    def __init__(self):
        self.hexagono = None
    
    def calcular_area(self, lado):
        self.hexagono = Hexagono(lado)
        return self.hexagono.calcular_area()
