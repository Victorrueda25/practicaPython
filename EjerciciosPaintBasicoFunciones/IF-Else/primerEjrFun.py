def datosProceso():
    print("Has ingresado a la opcion de ingresar datos de calificacion: ")
    print("En esta seccion ingresa la calificacion para saber que tipo de calificacion tiene: ")
    puntaje = int(input("Porfavor ingrese le puntaje: "))
    datosProcesar(puntaje)
    
    
def datosProcesar(puntaje): 
    if puntaje >= 90:
        print("Calificacion es de : A")
    else:
        if puntaje>= 80:
                print("Calificacion es de: B")
        else:
            if puntaje >= 70:
                print("Calificacion es de: C")
            else:
                if puntaje >= 60:
                    print("Calificacion es de D:")
                else:
                    print("Calificacion es de: F reprovado")
                    return puntaje
                verResultado(puntaje)
              
            
def verResultado(puntaje):
    print("El resultado es: ", puntaje)
              
                
def menuPrincipal():
    bandera = True
    while bandera : 
        print("Bienvenido al menu: ")
        print("1. Opcion. ingresar puntaje")
        print("2. Salir")
        opc = input("")
        match opc:     
            case "1":
                datosProceso()
            case "2":
                print("Saliendo del menu de opciones: ")
                bandera = False
            case _:
                print("Sigues en el menu: ")
             

menuPrincipal()