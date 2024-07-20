def datosProceso():
    # Definir variables
    acumulador = ""
    numeros = ""
    # Cuerpo del algoritmo
    print("Ingrese la cantidad de contactos a guardar: ")
    cantidad = int(input())
    calcularDatos(acumulador, numeros, cantidad)
    
    
def calcularDatos(acumulador, numeros,cantidad):
    # Bucle for
    for contador in range(cantidad):  # Se ejecutará dos veces
        print("Ingrese nombre del contacto")
        nombre = input()
        print("Ingrese numero del contacto")
        nume = input()

        acumulador += nombre + "--------" 
        numeros += numeros + nume + "----------"
        verResultado(acumulador, numeros)

def verResultado(acumulador, numeros):
    print("Nombres de los contactos:", acumulador)
    print("Los numeros guardados son: ", numeros)
    
    
def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, Ingresar la cantidad de contactos y numero para guardar: ")
        print("2. Salir")
        opc = input("")
        match opc: 
            case "1":
                datosProceso()
            case "2": 
                print("Saliendo del programa")
                bandera = False #lo utilizo para detener el while
            case _:
                print("Opción no valida")  
              
              
menuPrincipal()