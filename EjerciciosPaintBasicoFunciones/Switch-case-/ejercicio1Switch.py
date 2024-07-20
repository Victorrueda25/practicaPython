
def datosproducto():
    acumulador = 0
    totalRespuesta = 0
    print("Bienvenidos al comercio Variedades: los tipos de productos ")
    print("Que tenemos son A: alimentos, V: vestimenta, E: electronicos :")
    print("---------------")
    print("A: manzana, Naranja, Fresa: ")
    print("Con un costo de: manzana=200 naranja=100 fresa=150")
    print("V: Pantalon, Camisa, Zapato: ")
    print("Con un costo de: pantalon=80 camisa=70 zapatos=50 :")
    print("E: computador, telefono, televisor :")
    print("con un costo: computador=60 telefono=300 televisor=250 :")
    print("---------------")
    tipoProducto = (str(input("Porfavor ingrese el tipo de producto, A, V, E: ")))
    seleccion = input("Porfavor ingrese la seleccion del producto: ")
    cantidad = (int(input("Porfavor ingrese la cantidad del producto: ")))
    procesoCalcular(tipoProducto, seleccion, cantidad, acumulador, totalRespuesta)
  
    
def procesoCalcular(tipoProducto, seleccion, cantidad, acumulador, totalRespuesta):
    if tipoProducto == 'A':
        if seleccion == 'manzana':
            precio = 200
            subtotal = (precio * cantidad)
        else:  
            if seleccion == 'naranja':
                precio = 100
                subtotal = (precio * cantidad)
            else:
                if seleccion == 'fresa':
                    precio = 150
                    subtotal = (precio * cantidad)  
    else:
            if tipoProducto == 'V':
                if seleccion == 'pantalon':
                    precio= 80
                    subtotal = (precio * cantidad)
                else:
                    if seleccion == 'camisa':
                        precio = 70
                        subtotal = (precio * cantidad)
            else:
                if seleccion == 'zapatos':
                    precio = 50
                    subtotal = (precio * cantidad)
                else:
                    if tipoProducto == 'E':
                        if seleccion == 'computador':         
                            precio = 60
                            subtotal = (precio * cantidad)
                        else:    
                            if seleccion == 'telefono':
                                precio = 300
                                subtotal = (precio * cantidad)
                            else:    
                                if seleccion == 'televisor':
                                    precio = 250
                                    subtotal = (precio * cantidad)
                                else:
                                    print("Error")        
    vertotal(tipoProducto, seleccion, cantidad, subtotal, acumulador, totalRespuesta)



def vertotal(tipoProducto,  seleccion, cantidad, subtotal, acumulador, totalRespuesta):
    if tipoProducto == 'A':
        total = subtotal - ( cantidad  * 0.10)
        print("Se le aplicara el descuento del 10%: ")
        print("Se le ha aplicado el descuento del 10%: ", total)
    else:
        if tipoProducto == 'V':
            total = subtotal - (cantidad * 0.05)
            print("Se le aplicara el descuento del 5%: ")
            print("Se le ha aplicado el descuento del 5%", total)
        else:
            if tipoProducto == 'E':
                total = subtotal
                print("El tipo de producto E no se le aplican descuentos: ")
            else:
                total = subtotal
                print("No hubo elecciones: ")
                
        verAcumu(tipoProducto,seleccion, cantidad, subtotal, total,acumulador, totalRespuesta)
        
                
def verAcumu(tipoProducto, cantidad,seleccion, subtotal, total,acumulador, totalRespuesta):
    acumulador += total
    verRepuesta(tipoProducto, cantidad,seleccion, subtotal, total, totalRespuesta, acumulador)
    

def verRepuesta(tipoProducto, cantidad, totalRespuesta,seleccion, subtotal, total, acumulador):
    print("El acumulado es de: ", acumulador)
    print("El tipo de producto es: ", tipoProducto)
    print("La cantidad del producto es de:", cantidad)
    print("Su seleccion fue:", seleccion)
    print("Este es el subtotal: ", subtotal)  
    print("El total del producto es: ", totalRespuesta)


def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Elegir la compra: ")
        print("2. Salir")
        opc = input("")
        match opc: 
            case "1":
                datosproducto()
            case "2": 
                print("Saliendo del programa")
                bandera = False #lo utilizo para detener el while
            case _:
                print("Opción no valida")
            
menuPrincipal()