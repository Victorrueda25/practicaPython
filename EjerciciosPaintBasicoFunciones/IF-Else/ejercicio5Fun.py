def datosProceso():
    print("Ingrese el peso, (limite del peso 150kg): ")
    peso = int(input("Ingrese peso: "))
    piso = int(input("ingrese el piso: "))
    accion1(peso, piso)
    
      
def accion1(peso, piso): 
    if peso >= 150:
        print("El asensor esta sobrecargado no se puede ingresar: ")
    else:
        if peso <= 0:
            print("El peso no es valido, es menor a 0: ")
        else:
            print("Porfavor ingrese al piso al que desear trasladarse: ")
        if piso >= 1:
            print("Se traslado al piso", piso)
        else:
            if piso <= 10:
                print("se traslado al piso: ", piso)
            else:
                print("El piso no esta disponible: ")  
        
                
def VerUmbr():
    print("En esta opcion podras ver si la temperatura esta en el Umbral :")
    temperatura = int(input("Ingrese la temperatura actual, sin exceder el umbral: "))
    Umbral = 26
    if temperatura>Umbral:
        print("La temperatura esta por ecima del Umbral: ")
    else:
        print("La temperatura esta dentro del Umbral permitido: ")
   
   
        
def menuPrincipal():
    bandera = True
    while bandera : 
        print("Bienvenido al menu: ")
        print("1. Opcion. ingresar puntaje")
        print("2. Opcion. Ingresar para concer el umbral actual: ")
        print("3. Salir")
        opc = input("")
        match opc:     
            case "1":
                datosProceso()
            case "2":
                VerUmbr()
            case "3":
                print("Saliendo del menu de opciones: ")
                bandera = False
            case _:
                print("Sigues en el menu: ")
             

menuPrincipal()