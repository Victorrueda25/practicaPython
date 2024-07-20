def datosProceso():
    # Definición de variables
    producto = ""
    continuar = ""
    precio = 0.0
    totalVentas = 0.0
    resumenVentas = ""
    calcularProceso(producto, continuar, precio, totalVentas, resumenVentas)


def calcularProceso(producto, continuar, precio, totalVentas, resumenVentas):
    # Bucle para registrar ventas
    while continuar != "No":
        # Solicitar al usuario que ingrese el nombre del producto y su precio
        producto = input("Ingrese el nombre del producto vendido: ")
        precio = float(input("Ingrese el precio del producto: "))
    
        # Sumar el precio al total de ventas
        totalVentas += precio
    
        # Agregar el producto y su precio al resumen de ventas
        resumenVentas += f"{producto}: ${precio:.2f}\n"
    
        # Preguntar al usuario si desea registrar otra venta
        continuar = input("¿Desea registrar otra venta? (Sí/No): ")
        continuar = continuar.capitalize()  # Convertir la respuesta a mayúsculas para permitir "sí" o "Sí"
    
    verResultados(totalVentas, resumenVentas)


def verResultados(totalVentas, resumenVentas):
    # Mostrar el monto total de las ventas y el resumen de los productos vendidos
    print("Monto total de las ventas: $", totalVentas)
    print("Resumen de ventas:")
    print(resumenVentas)
    
    
def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, ingresar para La venta: ")
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