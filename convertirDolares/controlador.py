from modelo import Conversor

class ControladorConversor:
    def __init__(self, tasa_cambio):
        self.conversor = Conversor(tasa_cambio)
    
    def convertir(self, dolares):
        return self.conversor.convertir(dolares)
