from modelo import PrismaRectangular

class ControladorPrismaRectangular:
    def __init__(self):
        self.prisma = None
    
    def calcular_volumen(self, longitud, ancho, altura):
        self.prisma = PrismaRectangular(longitud, ancho, altura)
        return self.prisma.calcular_volumen()
