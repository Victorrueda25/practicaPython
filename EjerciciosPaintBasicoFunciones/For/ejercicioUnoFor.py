def datoProceso():
    # Variables definidas
    cantidad = int(input("¿Cuantos carros desea ingresar: "))
    acum = ""
    calcularDatos(cantidad, acum)

def calcularDatos(cantidad, acum):
    # Bucle For
    for i in range(cantidad):
        Usuario = input("Por favor ingrese el Nombre del Usuario: ")
        NumPlca = input("Por favor ingrese el número de placa: ")
        Hora = input("Ingrese la hora actual: ")
        print("Número de placa:", NumPlca)
        print("Hora actual es", Hora)
        acum += NumPlca + " " + Usuario + " " + Hora + "-----\n"
        verResultados(acum)

def verResultados(acum):
        print("Los carros guardados son:\n", acum)



def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, Ingresar la cantidad de carros que guardara: ")
        print("2. Salir")
        opc = input("")
        match opc: 
            case "1":
                datoProceso()
            case "2": 
                print("Saliendo del programa")
                bandera = False #lo utilizo para detener el while
            case _:
                print("Opción no valida")  
              
              
menuPrincipal()