class Conversor:
    def __init__(self, tasa_cambio):
        self.tasa_cambio = tasa_cambio
        
    def convertir(self, dolares):
        return dolares * self.tasa_cambio
