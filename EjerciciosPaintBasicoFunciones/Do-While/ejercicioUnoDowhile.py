def datosProceso():
# Declaración de variables
    autor = ""
    numPaginas = 0
    acumulador = ""
    control = 0
# Repetir el proceso hasta que sea verdadero
    print("Bienvenido a la biblioteca:")
    calcularLibros(autor, numPaginas, acumulador, control)
    
    
def calcularLibros(autor, numPaginas, acumulador, control):
    while control < 2:
        # Solicitar al usuario que ingrese los detalles del libro
        libro = input("Ingrese el nombre del libro: ")
        autor = input("Ingrese el Autor del libro: ")
        numPaginas = int(input("Ingrese el número de páginas: "))
    
    # Concatenar los detalles del libro al acumulador
        acumulador += f"{libro} - {autor} - {numPaginas} -----\n"
        control += 1
    verresultad(autor, numPaginas, acumulador)
        
def verresultad(autor, numPaginas, acumulador):
# Mostrar los textos que se han guardado
    print("Los textos que ha guardado son:")
    print(autor)
    print(numPaginas)
    print(acumulador)

def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, ingresar Numero Pata cuenta regresiva: ")
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