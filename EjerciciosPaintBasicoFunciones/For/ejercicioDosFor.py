def datosProceso():
    # Variables definidas
    totalCompra = 0  # Inicializamos el total de la compra a cero
    carritoCompra = ""  # Inicializamos el acumulador de texto para el carrito de compras

    cantidad = int(input("¿Cuántas compras deseas realizar?: "))
    calcularDatos(totalCompra, carritoCompra, cantidad)

def calcularDatos(totalCompra, carritoCompra, cantidad):
    # Bucle para agregar productos al carrito de compras
    for i in range(cantidad):
        producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))

        totalCompra += precio  # Sumamos el precio al total de la compra

        # Agregamos el producto y su precio al carrito de compras
        carritoCompra += producto + " $" + str(precio) + "\n"
    verResultados(totalCompra, carritoCompra)

def verResultados(totalCompra, carritoCompra):
    # Mostramos el total de la compra y los productos agregados al carrito
    print("Total de la compra: $", totalCompra)
    print("Productos en el carrito:")
    print(carritoCompra)
    
    

def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, Ingresar la cantidad de compras que realizara: ")
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