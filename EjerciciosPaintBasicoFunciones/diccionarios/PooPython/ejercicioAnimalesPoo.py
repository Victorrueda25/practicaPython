#Clase padre
class animales:
    #metodo constructor
    def __init__(self):
        self.nombre = ""
        self.edad = ""
        self.habitad = ""
        

    #Caracteristicas darlos valores de variables
    def asignacion_caracteristicas(self, dato_nombre, dato_edad, dato_habitad):
        self.nombre = dato_nombre
        self.edad = dato_edad
        self.habitad = dato_habitad

    #asignacion de clase hija, agregar metodo a la clase hija
    def agregar_reproduccion(self, dato_reproduc):
        self.reproduccion = dato_reproduc
        
    #mostrar informacion uno
    def mostrar_informacion(self):
        print(f"el nombre del caballo: {self.nombre} - la edad del caballo: {self.edad} - el habitad del animal: {self.habitad}")

    #mostrar informacion dos
    def mostrar_informacion2(self):
        print(f"el tipo de genero del animal es: {self.reproduccion}")

#Clase hija una
class animales_caballos(animales):
    #asignacion de las variables de la clase padre
    def __init__(self):
        super().__init__()
        self.caballo = ""
    
    #Asignacion de funcionalidades
    def asignacion_funcionalidad(self):        #dato nombre caballo                   #dato edad caballo                  #dato habitad
        super().asignacion_caracteristicas((input("Ingrese el nombre caballo: ")),(input("Ingrese el edad caballo: ")), (input("Ingrese el habitad caballo: ")) )
        self.alimentacion = input("Ingrese en tipo de alimentacion 1. energeticos 2.  Voluminosos")
        match self.alimentacion:
            case "1":
                self.alimentacion="energeticos"
            case "2":
                self.alimentacion="voluminosos"
    
    #Asignacion de metodo, instinto, moverse            
    def asignacion_instinto(self):
        self.instinto = input("Ingrese el instinto del caballo: ")
        self.moverse = input("Ingrese el movimiento del caballo: ")
        
    #Asignacion del se la funcion agregar_reproducccion()
    def agregar_reproducccion(self):
        super().agregar_reproducccion(input("Ingrese el tipo de reproduccion:"))
        
    #mostrar informacion de la clase padre e hija
    def mostrar_informacion_hija1(self):
        super().mostrar_informacion()
        super().mostrar_informacion2()
        print(f"El caballo : {self.nombre} - la alimentacion : {self.alimentacion} - el instinto : {self.instinto} - el movimiento: {self.moverse}")

#clase hija dos    
class animales_caiman(animales):

    #crear metodo constructor
    def __init__(self):
        super().__init__()
        self.caiman = ""
        
     #Asignacion de funcionalidades
    def asignacion_funcionalidad(self):        #dato nombre caiman                   #dato edad caiman                  #dato habitad caiman
        super().asignacion_caracteristicas((input("Ingrese el nombre caiman: ")),(input("Ingrese el edad caiman: ")), (input("Ingrese el habitad caiman: ")) )
        self.alimentacion = input("Ingrese en tipo de alimentacion 1. Vertebrados 2.  peces: ")
        match self.alimentacion:
            case "1":
                self.alimentacion="vertebrados"
            case "2":
                self.alimentacion="peces"
                
    #Asignacion de metodo, instinto, moverse            
    def asignacion_instinto(self):
        self.instinto = input("Ingrese el instinto del caiman: ")
        self.moverse = input("Ingrese el movimiento del caiman: ")
        
    #Asignacion del se la funcion agregar_reproducccion()
    def agregar_reproduccion(self):
        super().agregar_reproducccion(input("Ingrese el tipo de reproduccion:"))


    #mostrar informacion de la clase padre e hija
    def mostrar_informacion_hija2(self):
        super().mostrar_informacion()
        super().mostrar_informacion2()
        print(f"El caiman : {self.nombre} - la alimentacion : {self.alimentacion} - el instinto : {self.instinto} - el movimiento: {self.moverse}")

    #get nombre caiman
    def getVerNombre(self):
        return self.nombre

    #get edad caiman
    def getVerEdad(self):
        return self.edad
    
    #get habitad caiman
    def getHabitad(self):
        return self.habitad
    
    #get ver alimentacion
    def getAlimentacion(self):
        return self.alimentacion

    #get instinto
    def getInstinto(self):
        return self.instinto
    
    #get moverse
    def getMoverse(self):
        return self.moverse
    
    #estos son los sets
    #set nombre caiman
    def setVerNombre(self, nombre_nuevo):
        self.nombre=nombre_nuevo

    #set edad caiman
    def setVerEdad(self, edad_nuevo):
        self.edad =edad_nuevo
    
    #set habitad caiman
    def setHabitad(self, habitad_nuevo):
        self.habitad=habitad_nuevo
    
    #set ver alimentacion
    def setAlimentacion(self, alimentacion_nuevo):
        self.alimentacion=alimentacion_nuevo

    #set instinto
    def setInstinto(self, instinto_nuevo):
        self.instinto=instinto_nuevo
    
    #set moverse
    def setMoverse(self, moverse_nuevo):
        self.moverse=moverse_nuevo
    
#clase hija dos
class animales_pescado(animales):
    
    #crear metodo constructor
    def __init__(self):
        super().__init__()
        self.pescado = ""
        
    #Asignacion de funcionalidades
    def asignacion_funcionalidad(self):        #dato nombre pescado                   #dato edad pez                        #dato habitad pez
        super().asignacion_caracteristicas((input("Ingrese el nombre pescado: ")),(input("Ingrese el edad pez: ")), (input("Ingrese el habitad pez: ")) )
        self.alimentacion = input("Ingrese en tipo de alimentacion 1. Vegetariano 2.  carnivoro: ")
        match self.alimentacion:
            case "1":
                self.alimentacion="vegetariano"
            case "2":
                self.alimentacion="carnivoro"    
    
    #Asignacion de metodo, instinto, moverse            
    def asignacion_instinto(self):
        self.instinto = input("Ingrese el instinto del pez: ")
        self.moverse = input("Ingrese el movimiento del pez: ")
        
    #Asignacion de la funcion agregar_reproduccion()
    def agregar_reproduccion(self):
        super().agregar_reproduccion(input("Ingrese el tipo de reproduccion:"))

    #mostrar informacion de la clase padre e hija
    def mostrar_informacion_hija3(self):
        super().mostrar_informacion()
        super().mostrar_informacion2()
        print(f"El pez : {self.nombre} - la alimentacion : {self.alimentacion} - el instinto : {self.instinto} - el movimiento: {self.moverse}")

    #get nombre pez
    def getVerNombre(self):
        return self.nombre

    #get edad pez
    def getVerEdad(self):
        return self.edad
    
    #get habitad pez
    def getHabitad(self):
        return self.habitad
    
    #get ver alimentacion pez
    def getAlimentacion(self):
        return self.alimentacion

    #get instinto pez
    def getInstinto(self):
        return self.instinto
    
    #get moverse pez
    def getMoverse(self):
        return self.moverse
    
    #estos son los sets
    #set nombre pez
    def setVerNombre(self, nombre_nuevo):
        self.nombre=nombre_nuevo

    #set edad pez
    def setVerEdad(self, edad_nuevo):
        self.edad =edad_nuevo
    
    #set habitad pez
    def setHabitad(self, habitad_nuevo):
        self.habitad=habitad_nuevo
    
    #set ver alimentacion pez
    def setAlimentacion(self, alimentacion_nuevo):
        self.alimentacion=alimentacion_nuevo

    #set instinto pez
    def setInstinto(self, instinto_nuevo):
        self.instinto=instinto_nuevo
    
    #set moverse pez
    def setMoverse(self, moverse_nuevo):
        self.moverse=moverse_nuevo

#clase hija cuatro    
class animales_escarabajo(animales):

    #crear metodo constructor
    def __init__(self):
        super().__init__()
        self.escarabajo = ""
        
    #Asignacion de funcionalidades
    def asignacion_funcionalidad(self):        #dato nombre escarabajo                 #dato edad escarabajo                           #dato habitad escarabajo
        super().asignacion_caracteristicas((input("Ingrese el nombre escarabajo: ")),(input("Ingrese el edad escarabajo: ")), (input("Ingrese el habitad escarabajo: ")) )
        self.alimentacion = input("Ingrese en tipo de alimentacion 1. Plantas muertas 2.  Animales muertos: ")
        match self.alimentacion:
            case "1":
                self.alimentacion="Plantas muertas"
            case "2":
                self.alimentacion="Animales muertos" 
                
    #Asignacion de metodo, instinto, moverse            
    def asignacion_instinto(self):
        self.instinto = input("Ingrese el instinto del escarabajo: ")
        self.moverse = input("Ingrese el movimiento del escarabajo: ")
        
    #Asignacion de la funcion agregar_reproduccion()
    def agregar_reproduccion(self):
        super().agregar_reproduccion(input("Ingrese el tipo de reproduccion:"))
        
    #mostrar informacion de la clase padre e hija
    def mostrar_informacion_hija4(self):
        super().mostrar_informacion()
        super().mostrar_informacion2()
        print(f"El escarabajo : {self.nombre} - la alimentacion : {self.alimentacion} - el instinto : {self.instinto} - el movimiento: {self.moverse}")  
        
    #get nombre escarabajo
    def getVerNombre(self):
        return self.nombre

    #get edad escarabajo
    def getVerEdad(self):
        return self.edad
    
    #get habitad escarabajo
    def getHabitad(self):
        return self.habitad
    
    #get ver alimentacion escarabajo
    def getAlimentacion(self):
        return self.alimentacion

    #get instinto escarabajo
    def getInstinto(self):
        return self.instinto
    
    #get moverse escarabajo
    def getMoverse(self):
        return self.moverse
    
    #estos son los sets
    #set nombre escarabajo
    def setVerNombre(self, nombre_nuevo):
        self.nombre=nombre_nuevo

    #set edad escarabajo
    def setVerEdad(self, edad_nuevo):
        self.edad =edad_nuevo
    
    #set habitad escarabajo
    def setHabitad(self, habitad_nuevo):
        self.habitad=habitad_nuevo
    
    #set ver alimentacion escarabajo
    def setAlimentacion(self, alimentacion_nuevo):
        self.alimentacion=alimentacion_nuevo

    #set instinto escarabajo
    def setInstinto(self, instinto_nuevo):
        self.instinto=instinto_nuevo
    
    #set moverse escarabajo
    def setMoverse(self, moverse_nuevo):
        self.moverse=moverse_nuevo

#clase hija cinco    
class animales_pato(animales):

#crear metodo constructor
    def __init__(self):
        super().__init__()
        self.patos = ""
        
    #Asignacion de funcionalidades
    def asignacion_funcionalidad(self):        #dato nombre pato                 #dato edad pato                           #dato habitad pato
        super().asignacion_caracteristicas((input("Ingrese el nombre pato: ")),(input("Ingrese el edad pato: ")), (input("Ingrese el habitad pato: ")) )
        self.alimentacion = input("Ingrese en tipo de alimentacion 1. Plantas semillas 2.  Animales semillas: ")
        match self.alimentacion:
            case "1":
                self.alimentacion="semillas"
            case "2":
                self.alimentacion="Caracoles" 

    #Asignacion de metodo, instinto, moverse            
    def asignacion_instinto(self):
        self.instinto = input("Ingrese el instinto del pato: ")
        self.moverse = input("Ingrese el movimiento del pato: ")
        
    #Asignacion de la funcion agregar_reproduccion()
    def agregar_reproduccion(self):
        super().agregar_reproduccion(input("Ingrese el tipo de reproduccion:"))

    #mostrar informacion de la clase padre e hija
    def mostrar_informacion_hija5(self):
        super().mostrar_informacion()
        super().mostrar_informacion2()
        print(f"El pato : {self.nombre} - la alimentacion : {self.alimentacion} - el instinto : {self.instinto} - el movimiento: {self.moverse}")  

    #get nombre pato
    def getVerNombre(self):
        return self.nombre

    #get edad pato
    def getVerEdad(self):
        return self.edad
    
    #get habitad pato
    def getHabitad(self):
        return self.habitad
    
    #get ver alimentacion pato
    def getAlimentacion(self):
        return self.alimentacion

    #get instinto pato
    def getInstinto(self):
        return self.instinto
    
    #get moverse pato
    def getMoverse(self):
        return self.moverse
    
    #estos son los sets
    #set nombre pato
    def setVerNombre(self, nombre_nuevo):
        self.nombre=nombre_nuevo

    #set edad pato
    def setVerEdad(self, edad_nuevo):
        self.edad =edad_nuevo
    
    #set habitad pato
    def setHabitad(self, habitad_nuevo):
        self.habitad=habitad_nuevo
    
    #set ver alimentacion pato
    def setAlimentacion(self, alimentacion_nuevo):
        self.alimentacion=alimentacion_nuevo

    #set instinto pato
    def setInstinto(self, instinto_nuevo):
        self.instinto=instinto_nuevo
    
    #set moverse pato
    def setMoverse(self, moverse_nuevo):
        self.moverse=moverse_nuevo

while True:
    print("\n----")
    print("Bienvenido")
    print("1. para elegir caballos: ")
    print("2. para elegir caiman: ")
    print("3. para elegir pescado: ")
    print("4. para elegir escarabajo: ")
    print("5. para elegir pato: ")
    print("6. salir :")
    print("-----------------")
    opcion = input("Ingrese la opcion de su preferencia: ")
    match opcion:
        case "1":
            dato_caballo = animales_caballos()
            dato_caballo.asignacion_funcionalidad()
            dato_caballo.asignacion_instinto()
            dato_caballo.agregar_reproduccion()
            dato_caballo.mostrar_informacion_hija1()
        case "2":
            while True:
                        print("caiman")
                        print("1. para crear datos caiman")
                        print("2. para ver datos caiman")
                        print("3. para modificar datos caiman")
                        print("4. para salir")
                        opc=input("elija una opcion: ")
                        match opc:
                            case "1":
                                datos_caiman = animales_caiman()
                                datos_caiman.asignacion_funcionalidad()
                                datos_caiman.asignacion_instinto()
                                datos_caiman.agregar_reproduccion()
                                datos_caiman.mostrar_informacion_hija2()
                            case "2":
                                print("nombre: ", datos_caiman.getVerNombre())
                                print("edad: ", datos_caiman.getVerEdad())
                                print("habitad: ", datos_caiman.getHabitad())
                                print("alimentacion: ", datos_caiman.getAlimentacion())
                                print("instinto: ", datos_caiman.getAlimentacion())
                                print("moverse: ", datos_caiman.getMoverse())
                            case "3":
                                datos_caiman.setVerNombre(input("Ingrese el nuevo nombre: "))
                                datos_caiman.setVerEdad(input("Ingrese la nueva edad: "))
                                datos_caiman.setHabitad(input("Ingrese el habitad nueva: "))
                                datos_caiman.setAlimentacion(input("Ingrese la nueva alimentacion: "))
                                datos_caiman.setInstinto(input("Ingrese el nuevo instinto: "))
                                datos_caiman.setMoverse(input("Ingrese el nuevo tipo de movimiento: "))
                            case "4":
                                print("hasta luego")
                                break
                            case _:
                                print("ingrese una opcion valida")               
        case "3": 
            while True:
                        print("Pez")
                        print("1. para crear datos pez")
                        print("2. para ver datos pez")
                        print("3. para modificar datos pez")
                        print("4. para salir")
                        opc=input("elija una opcion: ")
                        match opc:
                            case "1":
                                datos_peces = animales_pescado()
                                datos_peces.asignacion_funcionalidad()
                                datos_peces.asignacion_instinto()
                                datos_peces.agregar_reproduccion()
                                datos_peces.mostrar_informacion_hija3()
                            case "2":
                                print("nombre: ", datos_peces.getVerNombre())
                                print("edad: ", datos_peces.getVerEdad())
                                print("habitad: ", datos_peces.getHabitad())
                                print("alimentacion: ", datos_peces.getAlimentacion())
                                print("instinto: ", datos_peces.getAlimentacion())
                                print("moverse: ", datos_peces.getMoverse())
                            case "3":
                                datos_peces.setVerNombre(input("Ingrese el nuevo nombre: "))
                                datos_peces.setVerEdad(input("Ingrese la nueva edad: "))
                                datos_peces.setHabitad(input("Ingrese el habitad nueva: "))
                                datos_peces.setAlimentacion(input("Ingrese la nueva alimentacion: "))
                                datos_peces.setInstinto(input("Ingrese el nuevo instinto: "))
                                datos_peces.setMoverse(input("Ingrese el nuevo tipo de movimiento: "))
                            case "4":
                                print("hasta luego")
                                break
                            case _:
                                print("ingrese una opcion valida")
        case "4":
            while True:
                    print("Escarabajo")
                    print("1. para crear datos escarabajo")
                    print("2. para ver datos escarabajo")
                    print("3. para modificar datos escarabajo")
                    print("4. para salir")
                    opc=input("elija una opcion: ")
                    match opc:
                        case "1":
                            datos_escarabajo = animales_escarabajo()
                            datos_escarabajo.asignacion_funcionalidad()
                            datos_escarabajo.asignacion_instinto()
                            datos_escarabajo.agregar_reproduccion()
                            datos_escarabajo.mostrar_informacion_hija4()
                        case "2":
                            print("nombre: ", datos_escarabajo.getVerNombre())
                            print("edad: ", datos_escarabajo.getVerEdad())
                            print("habitad: ", datos_escarabajo.getHabitad())
                            print("alimentacion: ", datos_escarabajo.getAlimentacion())
                            print("instinto: ", datos_escarabajo.getAlimentacion())
                            print("moverse: ", datos_escarabajo.getMoverse())
                        case "3":
                            datos_escarabajo.setVerNombre(input("Ingrese el nuevo nombre: "))
                            datos_escarabajo.setVerEdad(input("Ingrese la nueva edad: "))
                            datos_escarabajo.setHabitad(input("Ingrese el habitad nueva: "))
                            datos_escarabajo.setAlimentacion(input("Ingrese la nueva alimentacion: "))
                            datos_escarabajo.setInstinto(input("Ingrese el nuevo instinto: "))
                            datos_escarabajo.setMoverse(input("Ingrese el nuevo tipo de movimiento: "))
                        case "4":
                            print("hasta luego")
                            break
                        case _:
                            print("ingrese una opcion valida")
                            
        case "5":
            while True:
                print("Pato")
                print("1. para crear datos Pato")
                print("2. para ver datos Pato")
                print("3. para modificar datos Pato")
                print("4. para salir")
                opc=input("elija una opcion: ")
                match opc:
                    case "1":
                        dato_pato = animales_pato()
                        dato_pato.asignacion_funcionalidad()
                        dato_pato.asignacion_instinto()
                        dato_pato.agregar_reproduccion()
                        dato_pato.mostrar_informacion_hija5()
                    case "2":
                        print("nombre: ", dato_pato.getVerNombre())
                        print("edad: ", dato_pato.getVerEdad())
                        print("habitad: ", dato_pato.getHabitad())
                        print("alimentacion: ", dato_pato.getAlimentacion())
                        print("instinto: ", dato_pato.getAlimentacion())
                        print("moverse: ", dato_pato.getMoverse())
                    case "3":
                        dato_pato.setVerNombre(input("Ingrese el nuevo nombre: "))
                        dato_pato.setVerEdad(input("Ingrese la nueva edad: "))
                        dato_pato.setHabitad(input("Ingrese el habitad nueva: "))
                        dato_pato.setAlimentacion(input("Ingrese la nueva alimentacion: "))
                        dato_pato.setInstinto(input("Ingrese el nuevo instinto: "))
                        dato_pato.setMoverse(input("Ingrese el nuevo tipo de movimiento: "))
                    case "4":
                            print("hasta luego")
                            break
                    case _:
                        print("ingrese una opcion valida")    
        case "6":
            print("Saliendo del programa: ")
            break
        case __:
            print("La opcion que ha elegido no es la correcta: ")
