from modelo import Numeros

class ControladorNumeros:
    def __init__(self):
        self.numeros = None

    def establecer_numeros(self, numero1, numero2):
        self.numeros = Numeros(numero1, numero2)

    def calcular_mayor(self):
        if self.numeros is None:
            raise ValueError("Los números no han sido establecidos.")
        numero1 = self.numeros.get_numero1()
        numero2 = self.numeros.get_numero2()
        if numero1 > numero2:
            mayor = numero1
        else:
            mayor = numero2
        return mayor
