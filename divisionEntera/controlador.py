from modelo import Numeros

class ControladorNumeros:
    def __init__(self):
        self.numeros = None

    def establecer_numeros(self, numero1, numero2):
        self.numeros = Numeros(numero1, numero2)

    def calcular_cociente(self):
        if self.numeros is None:
            raise ValueError("Los números no han sido establecidos.")
        numero1 = self.numeros.get_numero1()
        numero2 = self.numeros.get_numero2()
        if numero2 == 0:
            raise ValueError("La división por cero no está permitida.")
        cociente = numero1 // numero2
        return cociente
