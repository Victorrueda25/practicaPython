def datosProceso():
    print("Bienvenido al Cajero Automatico: ")
    print("Ingrese salgo actual: ")
    saldo = int(input("Saldo: "))
    while saldo != 0:
        monto_retirar = int(input("Ingrese el monto a retirar: "))
        if monto_retirar > saldo:
            print("Error: fondos insuficientes: ")
        else:
            saldo = saldo - monto_retirar
        
    verresultado(saldo)
        
def verresultado(saldo):
    print("Retiro exitoso, saldo restante: ", saldo)
    
   
def menuPrincipal():
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("Bienvenido al Restaurante el Buen sabor: ")
        print("1. Opcion, entrar a ingresar saldo menu: ")
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