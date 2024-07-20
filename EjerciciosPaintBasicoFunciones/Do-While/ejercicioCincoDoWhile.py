def datosProceso():
    # Definición de vaiables
    tareas = ""
    descripcion = ""
    fecha = ""
    continuar = 1
    calcularDatos(tareas, descripcion, fecha, continuar)

def calcularDatos(tareas, descripcion, fecha, continuar):
# Bucle para permitir al usuario agregar tareas
    while continuar == 1:
        # Solicitar al usuario que ingrese la descripción de la tarea y la fecha de vencimiento
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha = input("Ingrese la fecha de vencimiento (formato DD/MM/AAAA): ")
    
        # Concatenar la nueva tarea al acumulador de texto
        tareas += f"Tarea: {descripcion}, Fecha de vencimiento: {fecha}\n"
    
        # Preguntar al usuario si desea agregar otra tarea
        continuar = int(input("¿Desea agregar otra tarea? (1 para sí, 0 para no): "))
    verResultados(tareas)

def verResultados(tareas):
    # Mostrar la lista de tareas
    print("Lista de tareas:\n", tareas)
    
def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, ingresar Tareas y fecha de vencionmiento: ")
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