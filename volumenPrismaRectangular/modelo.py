class PrismaRectangular:
    def __init__(self, longitud, ancho, altura):
        self.longitud = longitud
        self.ancho = ancho
        self.altura = altura
        
    def calcular_volumen(self):
        return self.longitud * self.ancho * self.altura
    
    