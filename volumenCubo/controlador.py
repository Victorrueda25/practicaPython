from modelo import Cubo

class ControladorCubo:
    def __init__(self):
        self.cubo = None
    
    def calcular_volumen(self, lado):
        self.cubo = Cubo(lado)
        return self.cubo.calcular_volumen()
