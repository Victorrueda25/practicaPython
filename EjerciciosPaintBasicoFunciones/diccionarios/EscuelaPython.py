BsDts = {
    "cedula_estudiante_1": {
        "nombre": "Maria",
        "apellido": "Paula",
        "materias": {
            "matematicas": ("parciales",("p1", "p2", "p3")),
            "algebra": ("parciales",("p1", "p2", "p3")),
            "calculoalgebra": ("parciales",("p1", "p2", "p3"))
        }
    },
    "cedula_estudiante_2": {
        "nombre": "Jose",
        "apellido": "Miguel",
        "materias": ("matematicas",("p1", "p2", "p3")),
            "algebra": ("parciales",("p1", "p2", "p3")),
            "calculoalgebra": ("parciales",("p1", "p2", "p3"))
    }
}


def agregarIdentificador():
    cedula = input("Ingrese el número de cédula del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    BsDts[cedula] = {"nombre": nombre, "apellido": apellido, "materias": ()}
    print("Estudiante agregado correctamente.")


def agregarPaqueteNotas():
    paq1 = ('matematicas', ('p1', 'p2', 'p3'), 'algebra', ('p1', 'p2', 'p3'), 'calculoalgebra', ('p1', 'p2', 'p3'))
    paq2 = ('Gramática', ('p1', 'p2', 'p3'), 'Vocabulario', ('p1', 'p2', 'p3'), 'literaturaInglesa', ('p1', 'p2', 'p3'))
    paq3 = ('Biologia', ('p1', 'p2', 'p3'), 'Quimica', ('p1', 'p2', 'p3'), 'Física', ('p1', 'p2', 'p3'))

    decision = input("Seleccione el paquete de materias:\n1. Matemáticas\n2. Inglés\n3. Ciencias\n")
    if decision == '1':
        paquete_seleccionado = paq1
    elif decision == '2':
        paquete_seleccionado = paq2
    elif decision == '3':
        paquete_seleccionado = paq3
    else:
        print("Opción no válida.")
        return

    for estudiante in BsDts.values():
        estudiante["materias"] = paquete_seleccionado

    print("Paquete de materias agregado a todos los estudiantes correctamente.")
    
    

def mostrarBaseDeDatos():
    print("Base de datos de estudiantes:")
    for cedula, estudiante in BsDts.items():
        print(f"Cédula: {cedula}")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Apellido: {estudiante['apellido']}")
        print("Materias:")
        materias = estudiante['materias']
        for i in range(0, len(materias), 2):
            materia = materias[i]
            calificaciones = materias[i + 1]
            print(f"- {materia}: Parciales {calificaciones}")
        print()

while True:
    print("\n-------")
    print("Bienvenido al Menú:")
    print("1. Agregar estudiante")
    print("2. Agregar paquete de materias")
    print("3. Mostrar base de datos de estudiantes")
    print("4. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        agregarIdentificador()
    elif opcion == '2':
        agregarPaqueteNotas()
    elif opcion == '3':
        mostrarBaseDeDatos()
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")