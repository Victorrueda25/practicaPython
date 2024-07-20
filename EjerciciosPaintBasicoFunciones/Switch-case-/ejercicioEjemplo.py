def datosProceso():
    numeroDia = int(input("Ingrese el numero de dia: "))
    procesarDatos(numeroDia)
    
    
def procesarDatos(numeroDia):
    match numeroDia:
        case 1: 
            textodia = "Lunes: "
        case 2: 
            textodia = "Martes: "
        case 3: 
            textodia = "Miercoles: "
        case 4: 
            textodia = "Jueves: "
        case 5: 
            textodia = "Viernes: "
        case _:
            print("No existe la opcion: ") 
            
    verRespuesta(textodia)
   
        
def verRespuesta(textodia):
    print("", textodia)
        
        
        
def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido al menu de opciones: ")
        print("1. Opcion. Ingresar ")
        print("2. salir")
        print("")
        opc = input("")
        match opc:
            case "1":
              datosProceso()
            case "2":
                print("Saliendo del menu: ")
                bandera = False 
            case _:
                print("Opcion no valida: ") 
                
        
        
menuPrincipal()
        
            