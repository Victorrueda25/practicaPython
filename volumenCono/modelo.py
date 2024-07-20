import math

class Cono:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
        
    def calcular_volumen(self):
        return (1/3) * math.pi * (self.radio ** 2) * self.altura
