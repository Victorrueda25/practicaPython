def datosProceso():
    victoria = int(input("Ingrese las victorias obtenidas: "))
    empatados = int(input("Ingrese los empates obtenidos: "))
    perdidos = int(input("Ingrese las perdidas obtenidas: "))
    ptsg = victoria * 3
    ptse = empatados * 1
    ptsp = perdidos * 0
    procesoCalcular(ptsg, ptse, ptsp)

def procesoCalcular(ptsg, ptse, ptsp):
    PtsCls = ptsg + ptse + ptsp
    if PtsCls > 21:
        print("A ocurrido algun error los puntos son superiores a lo establecido: ")
    else:
        if PtsCls >= 16 and PtsCls < 21:
            respuesta = "1"
        else:
            if PtsCls >= 11 and PtsCls < 15:
                respuesta = "2"
            else:
                if PtsCls >= 1 and PtsCls < 11:
                    respuesta = "3"
                else:
                    if PtsCls < 0:
                        print("Puntos de clasificacion insuficientes: ")
    VerRespuesta(respuesta)
                    
def VerRespuesta(respuesta):
    match respuesta:
        case "1":
            print("Clasificacion de Tipo A: ")
        case "2":
            print("Clasificacion de Tipo B: ")
        case "3":
            print("Clasificacion de tipo C: ")
        case _:
            print("Opcion no valida: ")
      
    
def MenuPrincipal():      
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("En total se juegan 7 partidos: ")
        print("1. Ingrese el numero de partidos G, Emp, Perd: ")
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
            
            
MenuPrincipal()