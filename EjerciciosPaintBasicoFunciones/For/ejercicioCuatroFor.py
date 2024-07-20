def datosProceso():
    suma = 0  # Inicializamos la suma en cero
    procesarDatos(suma)
    
    
def procesarDatos(suma):
    # Bucle para permitir al usuario ingresar números y sumarlos
    while True:
        for _ in range(5):
            try:
                num = float(input("Ingrese un número: "))
                suma += num  # Sumamos el número a la suma total
                verResultado(suma)
            except ValueError:
                print("¡Error! Debe ingresar un número válido.")
        
        continuar = input("¿Desea ingresar otro número? (1 para sí, 0 para no): ")
        if continuar != "1":
            break
        verResultado(suma)
    
    
def verResultado(suma):
    # Mostramos el resultado de la suma
    print("La suma de los números ingresados es:", suma)
    
    
    
def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, Ingresar 5 numeros para su suma: ")
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
# Llamamos a la función principal
