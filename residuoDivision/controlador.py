from modelo import Residuo



class ControladorResiduo:
    def __init__(self):
        self.residuo = None
    
    def calcular_residuo(self, dividendo, divisor):
        self.residuo = Residuo(dividendo, divisor)
        return self.residuo.calcular_residuo()
