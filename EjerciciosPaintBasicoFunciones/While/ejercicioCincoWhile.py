def datosProceso():
    numeroEntero = int(input("Ingrese un numero entero positivo: "))
    datoNumero(numeroEntero)

def datoNumero(numeroEntero):
    while numeroEntero <= 0:
        print("El numero ingresado debe ser positivo. Porfavor ingrese nuevamente: ")
        numeroEntero = int(input("Numero positivo: "))
    
    print("Iniciando cuenta regresiva: ")
    CuentaRegresiva(numeroEntero)

def CuentaRegresiva(numeroEntero):    
    while numeroEntero > 0:
        print(numeroEntero)
        numeroEntero = numeroEntero - 1 
    
    print("Tiempo cumplido: ")

def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, ingresar Numero Pata cuenta regresiva: ")
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