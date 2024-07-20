class Residuo:
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor
        
    def calcular_residuo(self):
        return self.dividendo % self.divisor
