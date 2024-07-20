def datosProceso():
    paginas = int(input("Ingrese la cantidad de paginas a Imprimir: "))

    Cantidad_Papel = 40
    procesarDatos(Cantidad_Papel, paginas)


def procesarDatos(Cantidad_Papel, paginas):
    while Cantidad_Papel != 0:
        paginas = int(input("Ingrese la cantidad de paginas a Imprimir: "))
        if Cantidad_Papel <= paginas:
            cantidadRestante = Cantidad_Papel - paginas
            verRespuesta(cantidadRestante)
        else:
            print("La cantidad de papel ya se ha agotado: ")
            
            
def verRespuesta(cantidadRestante):        
    print("La cantidad restante de las hojas es de: ", cantidadRestante)
        
        
            
def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, entrar a ingresar precio producto menu: ")
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