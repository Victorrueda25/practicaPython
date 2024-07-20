def datosProceso():
    # Declaración de variables
    temperatura = 0.0
    print("Simulación de temperatura:")
    CalcularTemperatura(temperatura)


def CalcularTemperatura(temperatura):
# Repetir hasta que la temperatura esté dentro del rango deseado
    while True:
        # Solicitar al usuario que ingrese la temperatura actual
        temperatura = float(input("Ingrese la temperatura actual: "))
    
        # Verificar si la temperatura está fuera del rango deseado
        if temperatura < 18 or temperatura > 25:
            print("Temperatura fuera del rango deseado.")
        else:
            print("La temperatura está en el rango indicado.")
            break  # Salir del bucle si la temperatura está en el rango deseado
        verTemperatura(temperatura)

def verTemperatura(temperatura):
    # Mostrar la temperatura actual
    print("Temperatura actual:", temperatura)


def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, ingresar temperatura: ")
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