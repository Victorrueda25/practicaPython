class Conversor:
    def __init__(self, pulgadas):
        self.pulgadas = pulgadas

    def convertir_a_centimetros(self):
        return self.pulgadas * 2.54
