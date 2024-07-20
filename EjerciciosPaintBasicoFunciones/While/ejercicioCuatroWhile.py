def datosProceso():
    respuesta = 'S'
    while respuesta != 'n' or respuesta !='N':
        distancia = int(input("Ingrese la distancia total del viaje en kilometros: "))
        velocidad = int(input("Ingrese la velocidad promedio del coche: "))
    
        tiempo = distancia / velocidad
        VerRespuesta(tiempo)    
    
        respuesta = str(input("Ingrese S o s para salir o N  y n como opcion para continuar con otra operacion: "))
        if respuesta == 'S' or respuesta == 's':
            print("Finalizo con exito: ")
            break
        else:
            print("Sigues dentro del proceso Do while ")
        
        
def VerRespuesta(tiempo):    
    print("El tiempo estimado de viaje es de: ", tiempo, "Horas: ")
        
        
        
def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("1. Opcion, ingresar Distancia y Velocidad para viaje menu: ")
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