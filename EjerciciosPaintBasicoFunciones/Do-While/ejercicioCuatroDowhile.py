def datosProceso():
    # Definición de variables
    promedioResultado = 0.0
    resultadoNota = 0.0
    nota1 = 0.0
    nota2 = 0.0
    contador = 0
    CalcularProceso(promedioResultado, resultadoNota, nota1, nota2, contador)

def CalcularProceso(promedioResultado, resultadoNota,nota1, nota2, contador):
    while contador == 0:
        # Solicitar al usuario que ingrese las notas de los dos semestres
        nota1 = float(input("Escriba la nota del primer semestre: "))
        nota2 = float(input("Escriba la nota del segundo semestre: "))

        # Calcular el promedio de las notas
        resultadoNota = nota1 + nota2
        promedioResultado = resultadoNota / 2

        # Verificar si el estudiante ha aprobado la materia
        if promedioResultado < 3:
            verNoAprovado(promedioResultado)
        else:
            verAprovado(promedioResultado)        
    
        # Actualizar el contador para salir del bucle
        contador = 1


def verNoAprovado(promedioResultado):
    print("No ha aprobado la materia. Promedio:", promedioResultado)

def verAprovado(promedioResultado):
    print("Ha aprobado la materia. Promedio:", promedioResultado)



def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, ingresar Conocer el promedio de las 2 notas del semestre: ")
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