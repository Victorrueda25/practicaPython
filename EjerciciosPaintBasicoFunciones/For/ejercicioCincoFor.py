def datosProceso():
    # Definimos las variables
    total_venta = 0
    registro_ventas = ""
    print("Por favor ingrese 5 productos de su preferencia:")
    calcularProceso(total_venta, registro_ventas)

def calcularProceso(total_venta, registro_ventas):
    # Bucle para registrar las ventas de varios productos
    for contador in range(1, 6):
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad vendida: "))

        # Calculamos el monto total de la venta de este producto
        monto_venta_producto = precio * cantidad

        # Sumamos el monto de esta venta al total de ventas
        total_venta += monto_venta_producto

        # Agregamos este producto al registro de ventas
        registro_ventas += f"{nombre_producto} - Precio: ${precio:.2f} - Cantidad vendida: {cantidad}\n"
        verDatos(total_venta, registro_ventas)
        # Preguntamos si desea registrar otra venta
        continuar = input("¿Desea registrar otra venta? (Sí: 1/No: 0)")
        if continuar != '1':
            break


def verDatos(total_venta, registro_ventas):
    # Mostramos el total de ventas y el registro de productos vendidos
    print("Total de ventas: $", total_venta)
    print("Registro de productos vendidos:")
    print(registro_ventas)
    
def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, Ingresar Elementos de venta 5 maximo: ")
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
# Llamamos a la función principal