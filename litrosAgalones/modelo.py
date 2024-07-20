class Conversor:
    def __init__(self, litros):
        self.litros = litros

    def convertir_a_galones(self):
        return self.litros * 0.264172
