#Definimos la clase padre
class vehiculo:
    #Metodo constructor
    def __init__(self):
        self.motor = ""
        self.color = ""

    #Caracteristicas
    def asignacion_caracteristicas(self, dato_motor, dato_color):
        self.motor = dato_motor
        self.color = dato_color
     
    #Asignacion del hijo uno    
    def asignacion_seguridad(self, dato_seguridad):
        self.seguridad = dato_seguridad
        
    #Ver informacion hijo uno
    def mostrar_informacion(self):
        print(f"El tipo de motor: {self.motor}- color -- {self.color} - el tipo de seguridad es: {self.seguridad}")
        
    #Mostrar informacion 2
    def mostrar_informacion2(self):
        print(f"El tipo de motor : {self.motor}- color : {self.color}")
        
    #Get motor
    def getmotor(self):
        return self.motor
    
    #Get color
    def getcolor(self):
        return self.color
    
    #Get seguridad
    def getseguridad(self):
        return self.seguridad
    
    #Set para modificar motor
    def setmotor(self,motor):
        self.motor=motor
        
    #set para modificar color
    def setcolor(self,color):
        self.color=color
        
    #set para modificar seguridad
    def setseguridad(self,seguridad):
        self.seguridad=seguridad
        
#Hijo uno subclase
class deportivo(vehiculo):
    def __init__(self):
        super().__init__()
        self.modelo = ""

    #modelo y climatizacion
    def asignacion_funcionalidad(self, dato_modelo):
        super().asignacion_caracteristicas(input("ingrese el motor: "),input("ingrese el color: "))
        self.modelo=dato_modelo
        self.climatizacion=input("ingrese el tipo de climatizacion :(1. combertible/2.no combertible): ")
        match self.climatizacion:
            case "1":
                self.climatizacion="combertible"
            case _:
                self.climatizacion="no combertible"
                
    #Nueva asignacion de acelleracion y frenado
    def asignazion_aceleracion_y_frenado(self):
        self.aceleracion=input("ingrese la aceleracion maxima del vehucilo: ")
        self.frenado=input("ingrese el sistema de frenado: (1. con ABS / 2. sin ABS)")
        match self.frenado:
            case "1":
                self.frenado="con ABS"
            case _:
                self.frenado="sin ABS"
                
    #seguridad desde padre
    def asignacion_seguridad(self):
        super().asignacion_seguridad(input("ingrese el tipo de seguridad: "))
        
    
    #mostrar la informacion hijo
    def mostrar_informacion_hijo(self):
        super().mostrar_informacion()
        print(f"modelo: {self.modelo} -- sistema de aceleracion: {self.aceleracion}km/h -- sistema de frenado: {self.frenado} -- climatizacion: {self.climatizacion}")
        
    #get modelo
    def getmodelo(self):
        return self.modelo
    
    #get climatizacion
    def getclimatizacion(self):
        return self.climatizacion
    
    #get aceleracion
    def getaceleracion(self):
        return self.aceleracion
    
    # get frenado
    def getfrenado(self):
        return self.frenado
    
    #set mofidicar modelo 
    def setmodelo(self,modelo):
        self.modelo=modelo

    #set modificar climatizacion
    def setclimatizacion(self,climatizacion):
        self.climatizacion=climatizacion
        match self.climatizacion:
            case "1":
                self.climatizacion="combertible"
            case _:
                self.climatizacion="no combertible"
                
    #set modificar acelelacion
    def setaceleracion(self,aceleracion):
        self.aceleracion=aceleracion

    #set modificar frenado
    def setfrenado(self,frenado):
        self.frenado=frenado
        match self.frenado:
            case "1":
                self.frenado="con ABS"
            case "2":
                self.frenado="sin ABS"
            case _:
                print("ingrese una opcion valida")
      
#hijo dos de la clase vehiculo                
class mini_bam(vehiculo):
    def _init_(self):
        super()._init_()
        self.numero_puertas=""
        self.capacidad_pasajeros=""
        
    #pasajeros y puertas
    def asignacion_pasajeros(self,dato_puerta,dato_pasajeros):
        super().asignacion_caracterizticas(input("ingrese el motor: "),input("ingrese el color: "))
        self.numero_puertas=dato_puerta
        self.capacidad_pasajeros=dato_pasajeros
        
    #Asignacion ventanas 
    def asignacion_ventanas(self):
        self.ventanas=input("ingrese el tipo de ventanas: ")
        
    #apagado y deireccion
    def asignacion_apagado_y_direccion(self):
        self.apagado=input("ingrese el tipo de apagado: ")
        self.direccion=input("ingrese el tipo de direccion: ")
        
    #muestra la informacion
    def mostrar_informacion_miniban(self):
        super().mostrar_informacion2()
        print(f"capacidad de pasajeros: {self.capacidad_pasajeros} -- tipo de ventanas: {self.ventanas} -- tipo de apagado: {self.apagado} -- tipo de direccion: {self.direccion}")
        
    #get ver numero de puertas
    def getpuerta(self):
        return self.numero_puertas
    
    #get ver numero de pasajeros
    def getpasajero(self):
        return self.capacidad_pasajeros
    
    #get ver ventanas
    def getventanas(self):
        return self.ventanas

    #get ver modo de apagado
    def getapagado(self):
        return self.apagado
    
    #get ver direccion
    def getdireccion(self):
        return self.direccion

    #set modificar puertas
    def setpuerta(self,puerta):
        self.numero_puertas=puerta
        
    #set modificar pasajeros    
    def setpasajero(self,pasajero):
        self.capacidad_pasajeros=pasajero
        
    #set modificar ventanas    
    def setventanas(self,ventanas):
        self.ventanas=ventanas
        
    #set modificar apagado    
    def setapagado(self,apagado):
        self.apagado=apagado
        
    #set modificar direccion    
    def setdireccion(self,direccion):
        self.direccion=direccion

#hijo tres
class camion(vehiculo):
    def __init__(self):
        super().__init__()
        self.tipo_combustible=""

    #combustible
    def asignacion_combustible(self,dato_combustible):
        super().asignacion_caracterizticas(input("ingrese el motor: "),input("ingrese el color: "))
        self.tipo_combustible=dato_combustible

    #luces,espejos y arranque
    def asignacion_espejos_luces_arranque(self):
        self.espejos=input("ingrese tipo de espejos: ")
        self.luces=input("ingrese las luces: ")
        self.arranque=input("ingrese la fuerza de arranque: ")
        
    #muestra informacion    
    def ver_info_hijo(self):
        super().mostrar_informacion2()
        print(f"tipo combustible: {self.tipo_combustible} -- tipo de espejos: {self.espejos} -- tipo de luces: {self.luces} -- tipo de arranque: {self.arranque}")
        
    #get ver combustible
    def getcombustible(self):
        return self.tipo_combustible
    
    #get ver espejos
    def getespejos(self):
        return self.espejos
    
    #get ver luces
    def getluces(self):
        return self.luces
    
    #get ver arranque
    def getarranque(self):
        return self.arranque
    
    #set modificar combustible
    def setcombustible(self,combustible):
        self.tipo_combustible=combustible
        
    #set modificar espejos
    def setespejos(self,espejos):
        self.espejos=espejos
        
    #set modificar luces
    def setluces(self,luces):
        self.luces=luces
        
    #set modificar arranque    
    def setarranque(self,arranque):
        self.arranque=arranque

def menu():
    while True:
        print("bienvenido")
        print("1. para elegir un vehiculo deprotivo")
        print("2. para elegir una mini-ban")
        print("3. para elegir un camion")
        print("4. para salir")
        opcion=input("ingrese la opcion: ")
        match opcion:
            case "1":
                vehiculo_deportivo=deportivo()
                vehiculo_deportivo.asignacion_funcionalidad(input("ingrese el modelo: "))
                vehiculo_deportivo.asignazion_aceleracion_y_frenado()
                vehiculo_deportivo.asignacion_seguridad()
                vehiculo_deportivo.mostrar_informacion_hijo()


            case "2":
                    while True:
                        print("mini-ban")
                        print("1. para crear")
                        print("2. para ver")
                        print("3. para modificar")
                        print("4. para salir")
                        opc=input("elija una opcion: ")
                        match opc:
                            case "1":
                                vehiculo_miniban=mini_bam()
                                vehiculo_miniban.asignacion_pasajeros(input("ingrese la cantidad de pasajeros: "),input("ingrese el numero de puertas: "))
                                vehiculo_miniban.asignacion_ventanas()
                                vehiculo_miniban.asignacion_apagado_y_direccion()
                                vehiculo_miniban.mostrar_informacion_miniban()
                            case "2":
                                print("motor: ",vehiculo_miniban.getmotor())
                                print("color: ",vehiculo_miniban.getcolor())
                                print("puertas: ",vehiculo_miniban.getpuerta())
                                print("pasajeros: ",vehiculo_miniban.getpasajero())
                                print("vetanas: ",vehiculo_miniban.getventanas())
                                print("apagado: ",vehiculo_miniban.getapagado())
                                print("direccion: ",vehiculo_miniban.getdireccion())
                            case "3":
                                vehiculo_miniban.setmotor(input("ingrese el nuevo motor: "))
                                vehiculo_miniban.setcolor(input("ingrese el nuevo color: "))
                                vehiculo_miniban.setpuerta(input("ingrese la nueva cantidd de puertas: "))
                                vehiculo_miniban.setpasajero(input("ingrese la nueva cantidad de pasajeros: "))
                                vehiculo_miniban.setventanas(input("ingrese el nuevo tipo de ventanas: "))
                                vehiculo_miniban.setapagado(input("ingrese el nuevo tipo de apagado: "))
                                vehiculo_miniban.setdireccion(input("ingrese el nuevo tipo de direccion: "))
                            case "4":
                                print("hasta luego")
                                break
                            case _:
                                print("ingrese una opcion valida")
            case "3":
                while True:
                    print("Camion")
                    print("1. para crear")
                    print("2. para ver")
                    print("3. para modificar")
                    print("4. para salir")
                    opc=input("elija una opcion: ")
                    match opc:
                        case "1":
                            vehiculo_camion=camion()
                            vehiculo_camion.asignacion_combustible(input("ingrese el tipo de combustible: "))
                            vehiculo_camion.asignacion_espejos_luces_arranque()
                            vehiculo_camion.ver_info_hijo()
                        case "2":
                            print("motor: ",vehiculo_camion.getmotor())
                            print("color: ",vehiculo_camion.getcolor())
                            print("combustible: ",vehiculo_camion.getcombustible())
                            print("espejos: ",vehiculo_camion.getespejos())
                            print("luces: ",vehiculo_camion.getluces())
                            print("arranque: ",vehiculo_camion.getarranque())
                        case "3":
                            vehiculo_camion.setmotor(input("ingrese el nuevo motor: "))
                            vehiculo_camion.setcolor(input("ingrese el nuevo color: "))
                            vehiculo_camion.setcombustible(input("ingrese el nuevo combustible: "))
                            vehiculo_camion.setespejos(input("ingrese los nuevos espejos: "))
                            vehiculo_camion.setluces(input("ingrese las nuevas luces: "))
                            vehiculo_camion.setarranque(input("ingrese el nuevo arraque: "))
                        case "4":
                            print("hasta luego")
                            break
                        case _:
                            print("ingrese una opcion valida")
            case "4":
                print("hasta luego...")
                break
            case _:
                print("ingrese una opcion valida")
                
                
                
menu()