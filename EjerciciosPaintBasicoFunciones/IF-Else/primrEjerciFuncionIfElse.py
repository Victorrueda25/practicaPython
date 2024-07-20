def datosProceso():
    piso = int(input("Porfavor ingrese el piso: "))
    accion1(piso)
        
def accion1(piso):    
    if piso <= 0:
        print("Piso no valido: ")
    else:
        if piso >= 7:
            print("Excedio el numero de pisos existentes: ")
        else:
            verRespuesta(piso)        
    
            
def verRespuesta(piso):
    print("Se trasladara al piso: ", piso)
 
 
 
def menuprincipal():
    bandera = True
    while bandera : 
        print("Bienvenido al menu: ")
        print("1 Opcion, ingresar")
        print("2 Salir, para salir del menu")
        opc = input("")
        match opc:     
            case '1':
                datosProceso()
            case '2':
                bandera = False
                print("Saliendo del menu de opciones: ")    
            case _:
                print("Sigues en el menu: ")
             


menuprincipal()