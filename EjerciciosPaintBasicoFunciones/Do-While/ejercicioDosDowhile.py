def datosProceso():
    # Declaración de variables
    comidaRapida = ""
    acumulador = ""
    controlador = ""
    precio = 0
    costoTotal = 0
    # Mostrar el menú de comidas rápidas
    print("1: Hamburgesa: ")
    print("2: Perro Americano: ")
    print("3: Salchipapa: ")
    print("4: Pizza: ")
    calcularVenta(comidaRapida, acumulador, controlador, precio, costoTotal)

def calcularVenta(comidaRapida, acumulador, controlador, precio, costoTotal):
    # Repetir el proceso hasta que el cliente no desee más
    while controlador != "No":
        # Solicitar al cliente que elija una opción del menú
        opc = int(input("¿Qué opción desea del menú?: "))
    
        # Procesar la opción elegida por el cliente
        if opc == 1:
            print("En la Opción 1 tenemos Hamburgesa con un costo de 4000: ")
            precio = 4000
            comidaRapida = "Hamburgesa"
        elif opc == 2:
            print("En la Opción 2 tenemos Perro Americano con un costo de 3500: ")
            precio = 3500
            comidaRapida = "Perro Americano"
        elif opc == 3:
            print("Tenemos como opción 3 Salchipapa: ")
            precio = 14000
            comidaRapida = "Salchipapa"
        elif opc == 4:
            print("En la Opción 4 tenemos pizza con un costo de 10000: ")
            precio = 10000
            comidaRapida = "Pizza"
    
        # Agregar la comida elegida al acumulador y sumar el precio al costo total
        acumulador += f"-----{comidaRapida}"
        costoTotal += precio
    
        # Preguntar al cliente si desea algo más
        controlador = input("¿Deseas algo más? (Si/No): ")
    verResultado(acumulador, costoTotal)

def verResultado(acumulador, costoTotal):
    # Mostrar el pedido y el total a pagar
    print("Tu pedido es el siguiente:", acumulador)
    print("El total a pagar es:", costoTotal)
    print("Gracias por tu compra")


def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, ingresar la compra que desea realizar: ")
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