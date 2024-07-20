from modelo import Conversor

class ControladorConversor:
    def __init__(self):
        self.conversor = None
    
    def convertir_a_centimetros(self, pulgadas):
        self.conversor = Conversor(pulgadas)
        return self.conversor.convertir_a_centimetros()
