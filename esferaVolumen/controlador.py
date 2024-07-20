from modelo import Esfera

class ControladorEsfera:
    def __init__(self):
        self.esfera = None
    
    def calcular_volumen(self, radio):
        self.esfera = Esfera(radio)
        return self.esfera.calcular_volumen()
