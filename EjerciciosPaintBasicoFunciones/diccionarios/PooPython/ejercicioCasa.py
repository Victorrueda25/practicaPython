class Casa:
    def _init_(self):

        self._direccion = ""
        self.numPisos = ""
        self.cuartos = ""
        self.baños = ""
        self.cocina = ""
        self.patio = ""
        self.sala = ""

    def get_direccion(self):
        return self._direccion
    
    def set_direccion(self):
        direccion = input ("Indica la direccion de la casa a construir: ")
        self._direccion = direccion

    def asigancion (self):
        print("Indica el numero de pisos que tendra la vivienda: ")
        self.numPisos = input()

        print ("indica el numero de cuartos que tendra la vivienda: ")
        self.cuartos = input()

        print (" Cuantos baños tendra la vivienda? ")
        self.baños = input()

    def construir(self):
        print(f"Construyendo casa en {self._direccion} con {self.numPisos}.")
    def pintar (self):
        print("Pintando la casa.")

class Cuarto (Casa):
    def _init_ (self):
        self.nombre = ""
        self.area = ""

    def usar (self):
        print(f"Usando el cuarto {self.nombre}.")

class Baño(Casa):
    def _init_(self):
        self.area = ""
    
    def usar(self):
        print ("Usando el baño. ")

class Cocina (Casa):
    def _init_ (self):
        self.cocinar = ""
        self.limpiar = ""

    def cocinar (self):
        print("Cocinando en la cocina. ")

    def limpiar (self):
        print("Limpiando la cocina. ")

class Patio(Casa):
    def _init_(self):
        self.relajar = ""
        self.jardineria = ""

    
    def relajar(self):
        print ("relajandose en el patio. ")

    def jardineria (self):
        print ("Realizando trabajo de jardineria en el patio. ")

class Sala(Casa):

    def _init_ (self):
        super()._init_()
        self.area = ""

    def reunir(self):
        print("Reuniendose en la sala.")

    def entretener (self):
        print ("Entreteniendose en la sala. ")

class Pared:
    def _init_(self):
        self._largo = ""
        self.alto = ""
        self.materiales = []

    def get_largo(self):
        return self._largo
    
    def get_largo(self):
        largo = input (" De que largo desea la pared? ")
    
    def get_alto(self):
        return self._largo
    
    def get_alto(self):
        altura = input (" De que altrura desea la pared ? ")
        self._alto=altura
    
    def asigancion(self, largo, altura):
        self._largo = largo
        self._alto = altura
        self.materiales = ["ladrillos", "cemento", "arena", "triturado"]


class Material:
    def _init_(self):
        self.cantidad=""

class Ladrillo(Material):
    def _int_ (self):
        self.tipo = ""

class Cemento(Material):
    def _int_ (self):
        self.tipo = ""

class Pasta(Material):
    def _int_ (self):
        self.tipo = ""

class Pintura(Material):
    def _int_ (self):
        self.tipo = ""

def menu ():

    print("BIENVENIDO A LA CONSTRUCTORA PY")
    print ("A c")

mi_casa = Casa()
mi_casa.set_direccion()

mi_casa.asigancion()

mi_casa.construir()
mi_casa.pintar()

mi_cuarto = Cuarto()
mi_cuarto.nombre = "Cuarto principal"
mi_cuarto.usar()


mi_baño = Baño()
mi_baño.usar()

mi_cocina = Cocina()
mi_cocina.cocinar()
mi_cocina.limpiar()

mi_Patio = Patio()
mi_Patio.relajar()
mi_Patio.jardineria()

mi_sala = Sala()
mi_casa.nombre = "Sala de la casa"
mi_sala.reunir()
mi_sala.entretener()

menu()