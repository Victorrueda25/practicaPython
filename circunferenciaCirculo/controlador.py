from modelo import Circulo

class ControladorCirculo:
    def __init__(self):
        self.circulo = None
    
    def calcular_circunferencia(self, radio):
        self.circulo = Circulo(radio)
        return self.circulo.calcular_circunferencia()
