class Botella:
    def __init__(self, material, capacidad, forma, diseno, tapa):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa

    def __str__(self):
        return f"Material: {self.material}, Capacidad: {self.capacidad}, Forma: {self.forma}, Diseño: {self.diseno}, Tapa: {self.tapa}"

    

class BotellaVidrio(Botella):
    def __init__(self, material, capacidad, forma, diseno, tapa, color):
        super().__init__(material, capacidad, forma, diseno, tapa)
        self.color = color

    def __str__(self):
        return super().__str__() + f", Color: {self.color}"

class BotellaPlastico(Botella):
    def __init__(self, material, capacidad, forma, diseno, tapa, reciclable):
        super().__init__(material, capacidad, forma, diseno, tapa)
        self.reciclable = reciclable

    def __str__(self):
        return super().__str__() + f", Reciclable: {self.reciclable}"

class Botellas:
    def __init__(self):
        self.botellas = []

    def registrarBotella(self, material, capacidad, forma, diseno, tapa, tipo="vidrio", color=None, reciclable=None):
        if tipo == "vidrio":
            botella = BotellaVidrio(material, capacidad, forma, diseno, tapa, color)
        elif tipo == "plastico":
            botella = BotellaPlastico(material, capacidad, forma, diseno, tapa, reciclable)
        else:
            raise ValueError("Tipo de botella no válido")

        self.botellas.append(botella)

    def buscarBotella(self, material):
        for botella in self.botellas:
            if botella.material == material:
                return botella  # Return the botella object directly
        return None

    def eliminarDatoBotella(self, material):
        for botella in self.botellas:
            if botella.material == material:
                self.botellas.remove(botella)
                return True
        return False

    def actualizarBotella(self, material, new_material, capacidad, forma, diseno, tapa):
        for botella in self.botellas:
            if botella.material == material:
                botella.material = new_material
                botella.capacidad = capacidad
                botella.forma = forma
                botella.diseno = diseno
                botella.tapa = tapa
                return True  # Indica que la actualización fue exitosa
        return False  # Indica que no se encontró la botella a actualizar

    def __str__(self):
        if self.botellas:
            return "\n".join(str(botella) for botella in self.botellas)
        else:
            return "No hay botellas registradas"
