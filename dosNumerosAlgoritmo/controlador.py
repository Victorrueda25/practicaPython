from modelo import Resta


class ControladorResta:
    def __init__(self):
        self.resta = None
    
    def calcular_resta(self, minuendo, sustraendo):
        self.resta = Resta(minuendo, sustraendo)
        return self.resta.calcular_resta()

