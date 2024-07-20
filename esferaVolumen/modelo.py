import math

class Esfera:
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)

