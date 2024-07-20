import math

class Hexagono:
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_area(self):
        return (3 * math.sqrt(3) / 2) * (self.lado ** 2)
