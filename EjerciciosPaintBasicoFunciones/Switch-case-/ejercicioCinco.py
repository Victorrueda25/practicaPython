def datosProceso():
    print( "---------------------")
    print("Bienvenido al Resturante El Buen Sabor: " )
    print( "El Dia de hoy tenemos de almuerzo: ")
    print("---------------------") 
    print("A Bandeja Paisa: con un Costo de 12.000: ") 
    print("B Higado encebollado: con un costo de 10.000: ") 
    print("C Sancocho de Gallina: con un costo de 11.000: ") 
    
    guardados = 0
    totalCompra = 0
    
    decision = 'A'
    while decision != 'D':
        decision = str(input("Ingrese la decision de plato con la D puede salir de la seleccion: "))
        if decision == 'D':
            break
        else:
            cantidad = int(input("Ingrese la cantidad de platos: "))
            metodoPago = input("Ingrese el metodo de pago efectivo o tarjeta: ")
            match decision:
                case 'A':
                    decision = 'Bandeja paisa con costo de 12.000'
                    precio = 12000
                    subtotal = precio * cantidad
                case 'B':
                    decision = 'higado encebollado con un costo de 10.000'
                    precio = 10000
                    subtotal = precio * cantidad
                case 'C':
                    decision = 'Sanchocho de gallina'
                    precio = 11000
                    subtotal = precio * cantidad
                case _:
                    print("Entendemos no tenga opcion: ")
        Calcularpago(subtotal, metodoPago, guardados, totalCompra)
           
               
def Calcularpago(subtotal, metodoPago, guardados, totalCompra):
    totalCompr = 0

    if metodoPago == 'efectivo':
        totalPagar = subtotal + (subtotal * 5/100) 
    elif metodoPago == 'tarjeta':
        totalPagar = subtotal + (subtotal * 10/100) 
    else:
        print("Ha ocurrido algún error")
        return

    guardados = guardados + totalPagar # Sumar el total acumulado
    VerTotal(guardados, totalCompra, totalCompr)

    verResultados(totalPagar)    
    
    
    
def verResultados(totalPagar):
    print("El total a pagar es de: ", totalPagar)    
    
def VerTotal(guardados, totalCompra, totalComp):
    totalComp = guardados + totalCompra
    print("Total compra: ", totalComp)
        
  
def MenuPrincipal():      
    bandera = True
    while bandera:
        print("Bienvenido, ingresa una opción")
        print("Bienvenido al Restaurante el Buen sabor: ")
        print("1. Opcion, entrar a elegir menu: ")
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
        
        
        
MenuPrincipal()