from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, edad, habitad, dieta, tamano, color):
        self.__nombre = nombre
        self.__edad = edad
        self.__habitad = habitad
        self.__dieta = dieta
        self.__tamano = tamano
        self.__color = color

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        self.__edad = value

    @property
    def habitad(self):
        return self.__habitad

    @habitad.setter
    def habitad(self, value):
        self.__habitad = value

    @property
    def dieta(self):
        return self.__dieta

    @dieta.setter
    def dieta(self, value):
        self.__dieta = value

    @property
    def tamano(self):
        return self.__tamano

    @tamano.setter
    def tamano(self, value):
        self.__tamano = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @abstractmethod
    def tipo(self):
        pass

class Caballo(Animal):
    def tipo(self):
        return "Caballo"

class Reptil(Animal):
    def tipo(self):
        return "Reptil"

class Acuatico(Animal):
    def tipo(self):
        return "Acuático"

class Escarabajo(Animal):
    def tipo(self):
        return "Escarabajo"

class Pato(Animal):
    def tipo(self):
        return "Pato"

class Animales:
    def __init__(self):
        self.animales = []

    def registrarAnimal(self, animal):
        self.animales.append(animal)
        return f"Animal tipo {animal.tipo()} registrado exitosamente"

    def buscarAnimal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                return animal
        return None

    def eliminarAnimal(self, nombre):
        for i, animal in enumerate(self.animales):
            if animal.nombre == nombre:
                del self.animales[i]
                return True
        return False

    def modificarAnimal(self, nombre_original, nuevos_datos):
        animal = self.buscarAnimal(nombre_original)
        if animal:
            animal.nombre = nuevos_datos[0]
            animal.edad = nuevos_datos[1]
            animal.habitad = nuevos_datos[2]
            animal.dieta = nuevos_datos[3]
            animal.tamano = nuevos_datos[4]
            animal.color = nuevos_datos[5]
            return True
        return False
