def datosProceso():
    print("Ha elegido la opcion de 1. aqui tienes")
    print("Tienes una capacidad maxima para el asensor de 150Kg: ")
    peso = int(input("Ingrese el peso porfavor: "))
    if peso >= 150:
            print("El peso excede la capacidad de carga del asensor: ") 
    else:
        if peso <= 0:
            print("El peso es menor a 0, no valido: ")  
    ProcesarDatos(peso)
    
    
def ProcesarDatos(peso):
    piso = int(input("Porfavor ingrese el piso al que desea ir: "))
    if piso >= 10:
                print("El piso no esta disponible: ")
    else:
        if piso >= 1:
            print("Se tralado al piso: ")
        else:
            if piso <= 10:
                print("se traslado al piso: ")
            else:
                print()
            verResultado(peso, piso)
            
def verResultado(peso, piso):
    print(peso)
    print(piso)
    

       
def menuPrincipal():
    bandera = True
    while bandera : 
        print("Bienvenido al menu: ")
        print("1. Opcion. ingresar peso y el piso")
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