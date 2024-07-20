from modelo import Conversor


class ControladorConversor:
    def __init__(self):
        self.conversor = None
    
    def convertir_a_galones(self, litros):
        self.conversor = Conversor(litros)
        return self.conversor.convertir_a_galones()
