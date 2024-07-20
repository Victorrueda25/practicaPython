from modelo import Cono

class ControladorCono:
    def __init__(self):
        self.cono = None
    
    def calcular_volumen(self, radio, altura):
        self.cono = Cono(radio, altura)
        return self.cono.calcular_volumen()
