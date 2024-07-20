def datosprocedimiento():
    edad = int(input("Porfavor ingrese su edad: "))
    procesardatos(edad)
    
def procesardatos(edad):
    if edad < 6:
        respuesta = "6"
    else:
        if edad <= 7 or edad < 17:
            respuesta = "7"
        else:
            if edad > 18 or edad < 30:
                respuesta = "18"
            else:
                print("La edad no esta bien escrita: ")
    verrespuesta(respuesta)
                
def verrespuesta(respuesta):       
    match respuesta: 
        case "6":
            print("El cliente tiene menos de 7 años. Recomendamos películas animadas")
        case "7":
            print("El cliente tiene entre 7 y 17 años. Recomendamos películas para niños y adolescentes, como animaciones, aventuras y comedias familiares.")
        case "18":
            print("El cliente tiene entre 18 y 30 años. Tenemos una variedad de géneros disponibles, como acción, drama, comedia y ciencia ficción")
        case "30":
            print("El cliente tiene más de 30 años. Recomendamos películas clásicas y dramas que pueden ser de su interés")
        case _:
            print("Opcion no valida: ")
        
        
bandera = True
while bandera:
    print("Bienvenido, ingresa una opción")
    print("1. Ingrese su edad: ")
    print("2. Salir")
    opc = input("")
    match opc: 
        case "1":
            datosprocedimiento()
        case "2": 
            print("Saliendo del programa")
            bandera = False #lo utilizo para detener el while
        case _:
            print("Opción no valida")