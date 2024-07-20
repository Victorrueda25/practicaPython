#Primera opcion y su funcion 
def accion1(): 
    print("En esta seccion sabras si la temperatura esta en el rango adecuado: ")
    grados = int(input("Porfavor ingrese la temperatura actual en grados: "))
    accion2(grados)

def accion2(grados):
    if grados >= 18 and grados <= 25:
        print("la temperatura es adecuada: ")
    else: 
        print("La temperatura esta fuera del rango :")
        
        verResultado(grados)


def verResultado(grados):
    print(grados)


    
def menuPrincipal():
    bandera = True
    while bandera : 
        print("Bienvenido al menu: ")
        print("1. Opcion. ingresar Temperatura: ")
        print("2. Salir")
        opc = input("")
        match opc:     
            case "1":
                accion1()
            case "2":
                print("Saliendo del menu de opciones: ")
                bandera = False
            case _:
                print("Sigues en el menu: ")
             

menuPrincipal()