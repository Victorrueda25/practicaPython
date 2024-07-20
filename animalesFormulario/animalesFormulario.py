from tkinter import *
from tkinter import messagebox, PhotoImage
from Animales import Animales, Caballo, Reptil, Acuatico, Escarabajo, Pato

class Interfaz:
    def __init__(self, color):
        self.color = color
        self.animales = Animales()
        self.formulario_animal = None

    def crearFormulario(self):
        formulario = Tk()
        formulario.title("Interfaz Registrar Animales")
        formulario.geometry("1000x600")
        formulario.config(bg=self.color)
        wtotal = formulario.winfo_screenwidth()
        htotal = formulario.winfo_screenheight()
        wventana = 1000
        hventana = 600
        pwidth = round(wtotal / 2 - wventana / 2)
        pheight = round(htotal / 2 - hventana / 2)
        formulario.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")
        return formulario

    def contenedorImagen(self, objformulario, img_path):
        contenedor1 = Frame(objformulario)
        contenedor1.config(bg="Blue", height=450, width=400, pady=15, padx=15)
        contenedor1.grid(row=0, column=0, rowspan=2, pady=15, padx=15)
        self.img = PhotoImage(file=img_path)
        label_img = Label(contenedor1, image=self.img)
        label_img.pack()
        return contenedor1

    def contenedorRegistro(self, objformulario):
        contenedor = Frame(objformulario)
        contenedor.config(bg="white", height=300, width=250, padx=20, pady=20)
        contenedor.grid(row=0, column=1, padx=10, pady=20, sticky="n")
        return contenedor

    def crearVentanaSeleccion(self):
        ventana_seleccion = Toplevel()
        ventana_seleccion.title("Selección de Animal")
        ventana_seleccion.geometry("300x200")
        ventana_seleccion.config(bg="lightgray")

        label = Label(ventana_seleccion, text="Seleccione el tipo de animal:")
        label.grid(row=1, column=0, padx=10, pady=10)

        opciones = ["Caballo", "Reptil", "Acuático", "Escarabajo", "Pato"]
        seleccion = StringVar()
        seleccion.set(opciones[0])

        menu = OptionMenu(ventana_seleccion, seleccion, *opciones)
        menu.grid(row=1, column=1, padx=10, pady=10)

        boton_seleccionar = Button(ventana_seleccion, text="Seleccionar",
                                command=lambda: self.mostrarFormulario(seleccion.get(), ventana_seleccion))
        boton_seleccionar.grid(row=2, column=0, columnspan=2, pady=10)

    def mostrarFormulario(self, seleccion, ventana_seleccion):
        ventana_seleccion.destroy()
        self.formulario_animal = Toplevel()
        self.formulario_animal.title(f"Registrar {seleccion}")
        self.formulario_animal.geometry("400x300")
        self.formulario_animal.config(bg="lightgray")

        label = Label(self.formulario_animal, text=f"Registrar un {seleccion}")
        label.grid(row=0, column=0, columnspan=2, pady=10)

        labels = ["Nombre del Animal:", "Edad del Animal:", "Hábitat del Animal:", "Dieta del Animal:", "Tamaño del Animal:", "Color del Animal:"]
        self.entries = {}

        for i, label_text in enumerate(labels):
            Label(self.formulario_animal, text=label_text).grid(row=i + 1, column=0, padx=5, pady=5, sticky="w")
            entry = Entry(self.formulario_animal)
            entry.grid(row=i + 1, column=1, padx=5, pady=5, sticky="w")
            self.entries[label_text] = entry

        boton_registrar = Button(self.formulario_animal, text="Registrar", command=lambda: self.registrarAnimal(seleccion))
        boton_registrar.grid(row=7, column=0, columnspan=2, pady=10)

    def registrarAnimal(self, seleccion):
        auxDatos = {label: entry.get() for label, entry in self.entries.items()}

        if seleccion == "Caballo":
            animal = Caballo(auxDatos["Nombre del Animal:"], auxDatos["Edad del Animal:"], auxDatos["Hábitat del Animal:"], auxDatos["Dieta del Animal:"], auxDatos["Tamaño del Animal:"], auxDatos["Color del Animal:"])
        elif seleccion == "Reptil":
            animal = Reptil(auxDatos["Nombre del Animal:"], auxDatos["Edad del Animal:"], auxDatos["Hábitat del Animal:"], auxDatos["Dieta del Animal:"], auxDatos["Tamaño del Animal:"], auxDatos["Color del Animal:"])
        elif seleccion == "Acuático":
            animal = Acuatico(auxDatos["Nombre del Animal:"], auxDatos["Edad del Animal:"], auxDatos["Hábitat del Animal:"], auxDatos["Dieta del Animal:"], auxDatos["Tamaño del Animal:"], auxDatos["Color del Animal:"])
        elif seleccion == "Escarabajo":
            animal = Escarabajo(auxDatos["Nombre del Animal:"], auxDatos["Edad del Animal:"], auxDatos["Hábitat del Animal:"], auxDatos["Dieta del Animal:"], auxDatos["Tamaño del Animal:"], auxDatos["Color del Animal:"])
        elif seleccion == "Pato":
            animal = Pato(auxDatos["Nombre del Animal:"], auxDatos["Edad del Animal:"], auxDatos["Hábitat del Animal:"], auxDatos["Dieta del Animal:"], auxDatos["Tamaño del Animal:"], auxDatos["Color del Animal:"])

        self.animales.registrarAnimal(animal)

        messagebox.showinfo("Registro Exitoso", f"Se ha registrado un {seleccion} correctamente")
        print(f"Nuevo animal registrado: {seleccion} - Nombre: {auxDatos['Nombre del Animal:']}, Edad: {auxDatos['Edad del Animal:']}, Hábitat: {auxDatos['Hábitat del Animal:']}, Dieta: {auxDatos['Dieta del Animal:']}, Tamaño: {auxDatos['Tamaño del Animal:']}, Color: {auxDatos['Color del Animal:']}")

        for entry in self.entries.values():
            entry.delete(0, END)

        self.formulario_animal.destroy()

    def modificarDatos(self):
        ventana_modificar = Toplevel()
        ventana_modificar.title("Modificar Datos de Animal")
        ventana_modificar.geometry("400x300")
        ventana_modificar.config(bg="lightgray")

        label = Label(ventana_modificar, text="Buscar Animal por Nombre:")
        label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.EntryModificar = Entry(ventana_modificar)
        self.EntryModificar.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        boton_buscar = Button(ventana_modificar, text="Buscar",
                            command=lambda: self.buscarDatosModificar(self.EntryModificar.get(), ventana_modificar))
        boton_buscar.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        labels = ["Nuevo Nombre del Animal:", "Nueva Edad del Animal:", "Nuevo Hábitat del Animal:", "Nueva Dieta del Animal:", "Nuevo Tamaño del Animal:", "Nuevo Color del Animal:"]
        self.modificar_entries = {}

        for i, label_text in enumerate(labels):
            Label(ventana_modificar, text=label_text).grid(row=i + 1, column=0, padx=5, pady=5, sticky="w")
            entry = Entry(ventana_modificar)
            entry.grid(row=i + 1, column=1, padx=5, pady=5, sticky="w")
            self.modificar_entries[label_text] = entry

        boton_modificar = Button(ventana_modificar, text="Modificar", command=self.modificarAnimal)
        boton_modificar.grid(row=7, column=0, columnspan=2, pady=10)

    def buscarDatosModificar(self, nombre, ventana_modificar):
        animal = self.animales.buscarAnimal(nombre)
        if animal:
            self.modificar_entries["Nuevo Nombre del Animal:"].delete(0, END)
            self.modificar_entries["Nueva Edad del Animal:"].delete(0, END)
            self.modificar_entries["Nuevo Hábitat del Animal:"].delete(0, END)
            self.modificar_entries["Nueva Dieta del Animal:"].delete(0, END)
            self.modificar_entries["Nuevo Tamaño del Animal:"].delete(0, END)
            self.modificar_entries["Nuevo Color del Animal:"].delete(0, END)

            self.modificar_entries["Nuevo Nombre del Animal:"].insert(0, animal.nombre)
            self.modificar_entries["Nueva Edad del Animal:"].insert(0, animal.edad)
            self.modificar_entries["Nuevo Hábitat del Animal:"].insert(0, animal.habitad)
            self.modificar_entries["Nueva Dieta del Animal:"].insert(0, animal.dieta)
            self.modificar_entries["Nuevo Tamaño del Animal:"].insert(0, animal.tamano)
            self.modificar_entries["Nuevo Color del Animal:"].insert(0, animal.color)
        else:
            messagebox.showerror("Error", "No se encontró el animal con el nombre proporcionado")
            ventana_modificar.destroy()

    def modificarAnimal(self):
        nombre = self.EntryModificar.get()
        animal = self.animales.buscarAnimal(nombre)
        if animal:
            nuevos_datos = {label: entry.get() for label, entry in self.modificar_entries.items()}
            animal.nombre = nuevos_datos["Nuevo Nombre del Animal:"]
            animal.edad = nuevos_datos["Nueva Edad del Animal:"]
            animal.habitad = nuevos_datos["Nuevo Hábitat del Animal:"]
            animal.dieta = nuevos_datos["Nueva Dieta del Animal:"]
            animal.tamano = nuevos_datos["Nuevo Tamaño del Animal:"]
            animal.color = nuevos_datos["Nuevo Color del Animal:"]

            messagebox.showinfo("Modificación Exitosa", f"Se han actualizado los datos del animal correctamente")
        else:
            messagebox.showerror("Error", "No se encontró el animal para modificar")
        
    def eliminarDatos(self):
        ventana_eliminar = Toplevel()
        ventana_eliminar.title("Eliminar Datos de Animal")
        ventana_eliminar.geometry("400x300")
        ventana_eliminar.config(bg="lightgray")

        label = Label(ventana_eliminar, text="Buscar Animal por Nombre:")
        label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.EntryEliminar = Entry(ventana_eliminar)
        self.EntryEliminar.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        boton_buscar = Button(ventana_eliminar, text="Buscar",
                            command=lambda: self.buscarDatosEliminar(self.EntryEliminar.get(), ventana_eliminar))
        boton_buscar.grid(row=0, column=2, padx=5, pady=5, sticky="w")

    def buscarDatosEliminar(self, nombre, ventana_eliminar):
        animal = self.animales.buscarAnimal(nombre)
        if animal:
            confirmacion = messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro que desea eliminar a {nombre}?")
            if confirmacion:
                self.animales.eliminarAnimal(nombre)
                messagebox.showinfo("Eliminación Exitosa", f"Se ha eliminado a {nombre} correctamente")
                ventana_eliminar.destroy()
        else:
            messagebox.showerror("Error", "No se encontró el animal con el nombre proporcionado")
            ventana_eliminar.destroy()

    def buscarDatos(self):
        ventana_buscar = Toplevel()
        ventana_buscar.title("Buscar Datos de Animal")
        ventana_buscar.geometry("400x300")
        ventana_buscar.config(bg="lightgray")

        label = Label(ventana_buscar, text="Buscar Animal por Nombre:")
        label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.EntryBuscar = Entry(ventana_buscar)
        self.EntryBuscar.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        boton_buscar = Button(ventana_buscar, text="Buscar",
                                command=lambda: self.buscarDatosAnimal(self.EntryBuscar.get(), ventana_buscar))
        boton_buscar.grid(row=0, column=2, padx=5, pady=5, sticky="w")

    def buscarDatosAnimal(self, nombre, ventana_buscar):
        animal = self.animales.buscarAnimal(nombre)
        if animal:
            info = f"Nombre: {animal.nombre}\nEdad: {animal.edad}\nHábitat: {animal.habitad}\nDieta: {animal.dieta}\nTamaño: {animal.tamano}\nColor: {animal.color}"
            messagebox.showinfo("Datos del Animal", info)
            ventana_buscar.destroy()
        else:
            messagebox.showerror("Error", "No se encontró el animal con el nombre proporcionado")
            ventana_buscar.destroy()
            
    def principal(self):
        self.formulario_animal = self.crearFormulario()
        img_path="C:/Users/Administrator/Documents/Python/animalesFormulario/animales.png"
        self.contenedorImagen(self.formulario_animal, img_path)
        contenedor_registro = self.contenedorRegistro(self.formulario_animal)

        boton_registrar = Button(contenedor_registro, text="Registrar Animal", command=self.crearVentanaSeleccion)
        boton_registrar.grid(row=0, column=0, padx=5, pady=5)

        boton_modificar = Button(contenedor_registro, text="Modificar Datos", command=self.modificarDatos)
        boton_modificar.grid(row=1, column=0, padx=5, pady=5)

        boton_eliminar = Button(contenedor_registro, text="Eliminar Animal", command=self.eliminarDatos)
        boton_eliminar.grid(row=2, column=0, padx=5, pady=5)

        boton_buscar = Button(contenedor_registro, text="Buscar Datos", command=self.buscarDatos)
        boton_buscar.grid(row=3, column=0, padx=5, pady=5)

        self.formulario_animal.mainloop()

# Crear una instancia de la interfaz con el color de fondo deseado
mi_interfaz = Interfaz("lightblue")
mi_interfaz.principal()
