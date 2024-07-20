def datosProceso():
    print("En la opcion 1 podras saber si la temperatura excede el umbral de alerta: ")
    temperatura = int(input("Porfavor ingrese la temperatura acutal: "))
    datosProcesar(temperatura)


   
def datosProcesar(temperatura): 
    if temperatura <= 26: 
        print("La temperatura actual esta por debajo del umbral de alerta: ")
    else:
        print("La temperatura execede el Umbral de Alerta: ")
    verRespuesta(temperatura)    
        
def verRespuesta(temperatura):
    print(temperatura)
        
        
def menuPrincipal():
    bandera = True
    while bandera : 
        print("Bienvenido al menu: ")
        print("1. Opcion. ingresar temperatura")
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

