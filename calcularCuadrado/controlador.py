from modelo import Cuadrado



class ControladorCuadrado:
    def __init__(self):
        self.cuadrado = None
    
    def calcular_cuadrado(self, numero):
        self.cuadrado = Cuadrado(numero)
        return self.cuadrado.calcular_cuadrado()
