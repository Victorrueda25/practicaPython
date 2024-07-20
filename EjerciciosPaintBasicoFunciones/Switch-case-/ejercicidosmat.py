def datospeso():
    peso = float(input("Porfavor ingrese el peso: "))
    altura = float(input("Porfavor ingrese la altura: "))
    procesardatos(peso, altura)
    
def procesardatos(peso, altura):
    total = (peso/altura*altura)

    if total < 18.5:
        respuesta = "1"
    else:
        if total > 18.5 and total < 24.9:
            respuesta = "2"
        else:
            if total >= 24.9 and total > 29.9:
                respuesta = "3"
            else:
                if total > 29.9:
                    respuesta = "4"
                else:
                    print("Ha ocurrido algun error: ")
                    
    respues(respuesta)
                    
def respues(respuesta):
    match respuesta: 
        case "1":
            print("Su peso es menor a lo indicado: ")
        case "2":
            print("Tu peso es normal segun lo indicado: ")
        case "3":
            print("Tienes sobre peso: ")
        case "4":
            print("Estas en un grado de obesidad: ")
        case _:
            print("")
            
bandera = True
while bandera:
    print("Bienvenido, ingresa una opción")
    print("1. ingrese su peso y altura: ")
    print("2. Salir")
    opc = input("")
    match opc: 
        case "1":
            datospeso()
        case "2": 
            print("Saliendo del programa")
            bandera = False #lo utilizo para detener el while
        case _:
            print("Opción no valida")
    