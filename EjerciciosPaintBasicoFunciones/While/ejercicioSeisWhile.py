def datosProceso():
    import random
    # Generar un número aleatorio entre 1 y 100
    numAleatorio = random.randint(1, 100)
    numero = 25  # Inicializar la variable de entrada del usuario
    # Mostrar mensaje de bienvenida
    print("Bienvenido al juego de adivinanza.")
    print("Intenta adivinar el número secreto entre 1 y 100.")
    CalcularDatos(numAleatorio, numero)


def CalcularDatos(numAleatorio, numero):
    # Iniciar bucle mientras el usuario no adivine el número
    while numero != numAleatorio:
        # Solicitar al usuario que ingrese un número
        numero = int(input("Ingresa tu número: "))
        # Verificar si el número ingresado es mayor, menor o igual al número aleatorio
        if numero < numAleatorio:
                print("El número secreto es mayor.")
        elif numero > numAleatorio:
                print("El número secreto es menor.")
    VerResultado()


def VerResultado():
    # El usuario adivinó el número, mostrar mensaje de felicitaciones
    print("¡Felicidades! Has adivinado el número secreto.")
   

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