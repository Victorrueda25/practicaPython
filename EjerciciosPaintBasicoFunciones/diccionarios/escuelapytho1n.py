# Definir la base de datos
BD = {
    '001': {
        'datosEstudiante': ('Juan', 'Perez'),
        'pq1': {
            'matematicas': {'p1': 90, 'p2': 85, 'p3': 95},
            'algebra': {'p1': 80, 'p2': 75, 'p3': 85},
            'calculo': {'p1': 85, 'p2': 90}
        }
    },
    '002': {
        'datosEstudiante': ('Maria', 'Gomez'),
        'pq1': {
            'matematicas': {'p1': 95, 'p2': 90, 'p3': 85},
            'algebra': {'p1': 85, 'p2': 80, 'p3': 75},
            'calculo': {'p1': 90, 'p2': 85}
        }
    }
}

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    cedula = input("Ingrese la cedula del Estudiante: ")
    paquete_materias = tuple(input("Ingrese las materias del paquete separadas por coma: ").split(", "))
    notas = {}
    for materia in paquete_materias:
        notas[materia] = [float(input(f"Ingrese la nota {i+1} de {materia}: ")) for i in range(3)]
    
    BD[cedula] = {
        "datosEstudiante": (nombre, apellido),
        "pq1": dict(zip(paquete_materias, [{f"p{i+1}": notas[materia][i] for i in range(3)} for materia in paquete_materias]))
    }
    print("Estudiante agregado exitosamente.")

def eliminar_materia():
    while True:
        estudiante = input("Ingrese la cedula del estudiante al que desea eliminar una materia: ")
        if estudiante in BD:
            materia_a_eliminar = input("Ingrese la materia que desea eliminar: ")
            paquete_materias = BD[estudiante]['pq1']
            if materia_a_eliminar in paquete_materias:
                del paquete_materias[materia_a_eliminar]
                print(f"Materia '{materia_a_eliminar}' eliminada exitosamente para el estudiante {estudiante}.")
            else:
                print("La materia especificada no existe para este estudiante.")
        else:
            print("El estudiante especificado no existe en la base de datos.")

        opcion = input("¿Desea intentarlo de nuevo (Si/No)? ").lower()
        if opcion != "si":
            break

    input("Presione Enter para volver al menu...")

def imprimir_promedio_por_materia():
    promedios = {}
    for cedula, datos in BD.items():
        for materia, notas in datos['pq1'].items():
            promedio = sum(notas.values()) / len(notas)
            if materia not in promedios:
                promedios[materia] = [promedio]
            else:
                promedios[materia].append(promedio)
    
    for materia, promedios_materia in promedios.items():
        promedio_total = sum(promedios_materia) / len(promedios_materia)
        print(f"El promedio de notas de {materia} es: {promedio_total:.2f}")
        
        
def imprimir_promedio_por_estudiante():
    for cedula, datos in BD.items():
        nombre, apellido = datos['datosEstudiante']
        notas = [sum(notas.values()) for notas in datos['pq1'].values()]
        promedio = sum(notas) / len(notas)
        print(f"El promedio de notas de {nombre} {apellido} es: {promedio:.2f}")

def modificar_paquete():
    estudiante = input("Ingrese el nombre del estudiante al que desea modificar el paquete de materias: ")
    for clave, valor in BD.items():
        if valor['datosEstudiante'][0] == estudiante:
            paquete_materias = tuple(input("Ingrese las nuevas materias del paquete separadas por coma: ").split(", "))
            notas = {}
            for materia in paquete_materias:
                notas[materia] = [float(input(f"Ingrese la nota {i+1} de {materia}: ")) for i in range(3)]
                promedio = sum(notas[materia]) / len(notas[materia])
                print(f"El promedio de notas de {materia} es: {promedio:.2f}")
            BD[clave]["pq1"] = dict(zip(paquete_materias, [{f"p{i+1}": notas[materia][i] for i in range(3)} for materia in paquete_materias]))
            print("Paquete de materias modificado exitosamente.")
            return
    else:
        print("El estudiante especificado no existe en la base de datos.")
        
def modificar_estudiante():
    cedula_estudiante = input("Ingrese la cedula del estudiante que desea modificar: ")
    if cedula_estudiante in BD:
        nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
        nuevo_apellido = input("Ingrese el nuevo apellido del estudiante: ")
        BD[cedula_estudiante]['datosEstudiante'] = (nuevo_nombre, nuevo_apellido)
        print("Datos del estudiante modificados exitosamente.")
    else:
        print("El estudiante especificado no existe en la base de datos.")

def imprimir_promedio_por_materia():
    for estudiante, pq in BD.items():
        for materia, notas in pq["pq1"].items():
            notas_numeros = [float(nota) for nota in notas.values()]
            promedio = sum(notas_numeros) / len(notas_numeros)
            nombre, apellido = pq["datosEstudiante"]
            print(f"El promedio de notas de {materia} para {nombre} {apellido} es: {promedio:.2f}")
            
def actualizarBaseDatos():
    for estudiante, datos in BD.items():
        print(estudiante, datos)
        
def ver_keys():
    print("Las claves de la base de datos son:")
    for clave in BD.keys():
        print(clave)
        
def ver_nombre():
    clave = input("Ingrese la clave del estudiante que desea consultar: ")
    estudiante = BD.get(clave)
    if estudiante:
        nombre, apellido = estudiante['datosEstudiante']
        print(f"El nombre del estudiante con la clave {clave} es: {nombre} {apellido}")
    else:
        print("No se encontró ningún estudiante con la clave especificada.")

# Menú principal
while True:
        print("\n--- MENU ---")
        print("1. Agregar estudiante")
        print("2. Imprimir promedio de notas por estudiante")
        print("3. Modificar paquete de materias")
        print("4. Eliminar el paquete de materias, seguido de las comas")
        print("5. Imprimir promedio de notas por materia")
        print("6. Modificar estudiante")
        print("7. Actualizar base de datos")
        print("8. Salir")
        print("9. para ver las Keys")
        print("10. para ver el nombre")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            imprimir_promedio_por_estudiante()
        elif opcion == "3":
            modificar_paquete()
        elif opcion == "4":
            eliminar_materia()
        elif opcion == "5":
            imprimir_promedio_por_materia()
        elif opcion == "6":
            modificar_estudiante()
        elif opcion == "7":
            actualizarBaseDatos()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        elif opcion == "9":
            ver_keys()
        elif opcion == "10":
            ver_nombre()
        else:
            print("Opcion invalida. Por favor, seleccione una opción válida.")