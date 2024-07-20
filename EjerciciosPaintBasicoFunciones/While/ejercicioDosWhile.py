def datosProceso():
    precio = int(input("Ingrese Precio: "))
    cantidad = int(input("Ingrese la cantidad de productos: "))
    respuesta = input("Desea comprar mas productos: s/n: ")
    acomula = 0
    totalCompra = precio * cantidad 
    calculcarProceso(precio, cantidad, respuesta, acomula, totalCompra)


def calculcarProceso(precio, cantidad, respuesta, acomula, totalCompra):
    while respuesta == 'S' or respuesta == 's':
        precio = int(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad de productos: "))
    
        total = precio * cantidad 
        acomula = acomula + total
    
        respuesta = str(input("Ingrese una respuesta si continuar, S o s, y no, n: "))
    
    totalRespuesta = acomula + totalCompra
    VerRespuesta(totalRespuesta)
 
def VerRespuesta(totalRespuesta):  
    print("El total es", totalRespuesta)    



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