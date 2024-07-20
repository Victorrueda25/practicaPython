import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio
