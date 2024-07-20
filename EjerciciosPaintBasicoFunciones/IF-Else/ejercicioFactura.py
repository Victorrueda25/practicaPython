def datosProceso():
    iva = 0
    importe = 0
    TipoClien = input("Ingresar tipo de cliente: estudiante / No estudiante ")
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    producto = str(input("Ingrese el nombre del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto que comprara: "))
    valor_uni = float(input("Ingresar el valor unitario del producto:" ))
    calcularProceso(iva, importe, TipoClien, nombre, apellido, producto, cantidad, valor_uni)


def calcularProceso(iva, importe, TipoClien, nombre, apellido, producto, cantidad, valor_uni):
    iva = importe * 0.05
    iva = importe * 0.13
    importe = cantidad * valor_uni
    
    if TipoClien == 'estudiante':
        importe = importe * 0.95
        print("Es estudiante: ")
    else:
        if TipoClien == 'No estudiante':
            importe = importe * 0.87
            print("No es estudiante: ")
        else:
            print("Ha ocurrido algun error: ")
    verTotales(iva, importe, TipoClien, nombre, apellido,producto,cantidad, valor_uni)
    
def verTotales(iva, importe, TipoClien, nombre, apellido,producto,cantidad, valor_uni):
    TipoClien = ""
    total = importe + iva
    verResultado(nombre, apellido, producto, importe, iva, total)    
            
        
def verResultado(nombre, apellido, producto, importe, iva, total):
    print("Nombre: ", nombre, "apellido", apellido)
    print("Producto:", producto)
    print("Importe: ", importe)
    print("iva: ", iva)
    print("Total a pagar: ", total)


def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion. Ingresar tipo de cliente y productos: ")
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