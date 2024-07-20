class botellas:
    def __init__(self):
        self.forma = ""
        self.color = ""
        self.material = ""
        self.diseno = ""
        self.BD = []

    def agregar_botella(self, forma, color, material, diseno, tapas="", grabados=""):
        botella = [forma, color, material, diseno, tapas, grabados]  
        self.BD.append(botella)  

    def agregar_otro_tipo(self):
        otro_tipo = input("Ingrese los detalles de la botella (forma, color, material, diseño): ").split()
        self.BD.append(otro_tipo)

    def mostrar_BD(self):
        print("Base de Datos:") 
        for botella in self.BD:
            print(botella)

    def __str__(self):
        print(f"botellas: {len(self.BD)}")
        return self.BD
    
    def GetForma(self):
        for botella in self.BD:
            forma_primera_botella = botella[0]  # Obtener la forma de la primera botella
            print(forma_primera_botella)
        return forma_primera_botella  # Devolver la forma de la primera botella


class botellas_vino_decora(botellas):
    def __init__(self):
        super().__init__()
        self.tapas = ""
        self.grabados = ""
        self.tapas = ""
        self.grabados = ""

    def agregar_botella_decorada(self):
        forma = input("Ingrese la forma de la botella: ")
        color = input("Ingrese el color de la botella: ")
        material = input("Ingrese el material de la botella: ")
        diseno = input("Ingrese el diseño de la botella: ")
        tapas = input("Ingrese el diseño de la tapa: ")
        grabados = input("Ingrese el grabado de la botella: ")
        super().agregar_botella(forma, color, material, diseno, tapas, grabados)

    
BD = botellas()  # Aquí creamos una instancia de la clase botellas
while True:
    print("---------\n---------------- ")
    print("1. Agregar botella a la base de datos")
    print("2. Agregar otro tipo de botella")
    print("3. Agregar botella con decoración")
    print("4. Agregar botella predefinida por el sistema")
    print("5. Ver base de datos")
    print("6. Salir")
    print("7. Agregar solo forma a la base datos")
    print("8. Ver forma")
    opcion = input("Ingrese la decisión del menú: ")
    if opcion == "1":
        f = input("Ingrese la forma de la botella: ")
        c = input("Ingrese el color de la botella: ")
        m = input("Ingrese el material de la botella: ")
        d = input("Ingrese el diseño de la botella: ")
        BD.agregar_botella(f, c, m, d)
        print("Botella guardada con éxito....")
    elif opcion == "2":
        BD.agregar_otro_tipo()
        BD.mostrar_BD()
    elif opcion == "3":
        # Uso de la clase
        BD= botellas_vino_decora()
        BD.agregar_botella_decorada()
        BD.mostrar_BD()
    elif opcion == "4":
        # Agregar botellas predefinidas por el sistema
        botellas_vinodulce = ["Benjamin", "Verde Oscuro", "vidrio", "logotipo empresa"]
        botellas_vinoOrange = ["Frasca", "Negro mate", "vidrio", "logotipo empresa con naranja"]
        botellas_vinoManzana = ["Clavelin", "Negro", "vidrio", "logotipo empresa con manzana"]
        BD.agregar_botella(*botellas_vinodulce)
        BD.agregar_botella(*botellas_vinoOrange)
        BD.agregar_botella(*botellas_vinoManzana)
        BD.mostrar_BD()
    elif opcion == "5":
        BD.mostrar_BD()
    elif opcion == "6":
        print("Saliendo...")
        break
    elif opcion == "7":
        print("Agregar forma a botella")
        FormaN=str(input("Agregar solo forma: "))
        print(FormaN)
    elif opcion == "8":
        # Obtener la forma de la primera botella en la base de datos
        forma_primera_botella = BD.GetForma()
        print("La forma de la primera botella es:", forma_primera_botella)

    else:
        print("Opción inválida.")
