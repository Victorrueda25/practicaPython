from tkinter import *
import tkinter as interfaceUsuario
from tkinter import messagebox
from botellas import Botellas

class Interfaz:
    def __init__(self, color):
        self.color = color
        self.EntryMaterial = None
        self.EntryCapacidad = None
        self.OptionForma = None
        self.EntryDiseno = None
        self.EntryTapa = None
        self.botellas_registradas = Botellas()

    def crearFormulario(self):
        objformulario = interfaceUsuario.Tk()
        objformulario.title("Registrar Botella")
        objformulario.geometry("800x600")
        objformulario.config(bg=self.color)
        return objformulario

    def crearContenedorRegistro(self, objformulario):
        contenedor_externo = Frame(objformulario, bg=self.color)
        contenedor_externo.grid(row=0, column=0, sticky='nsew')

        contenedor = Frame(contenedor_externo, bg="white", height=400, width=500, pady=15, padx=20)
        contenedor.grid(row=0, column=0, padx=200, pady=100)

        contenedor_externo.grid_rowconfigure(0, weight=1)
        contenedor_externo.grid_columnconfigure(0, weight=1)

        return contenedor

    def crearPreguntas(self, contenedor, objformulario):
        labelRegistrar = Label(contenedor, text="Registro de Botellas")
        labelRegistrar.grid(row=0, column=0, padx=10, pady=15)

        auxDatoMaterial = interfaceUsuario.StringVar()
        labelR = Label(contenedor, text="Ingrese Material de la botella: ")
        labelR.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.EntryMaterial = Entry(contenedor, textvariable=auxDatoMaterial)
        self.EntryMaterial.grid(row=1, column=1, padx=5, pady=5)

        auxdatoCapacidad = interfaceUsuario.StringVar()
        labelR1 = Label(contenedor, text="Ingrese la capacidad de la Botella en ML: ")
        labelR1.grid(row=2, column=0, padx=5, pady=5)
        self.EntryCapacidad = Entry(contenedor, textvariable=auxdatoCapacidad)
        self.EntryCapacidad.grid(row=2, column=1, padx=5, pady=5)

        auxdatoForma = interfaceUsuario.StringVar()
        labelR2 = Label(contenedor, text="Seleccione el tipo de botella: ")
        labelR2.grid(row=3, column=0, padx=5, pady=5)
        opcionesForma = ["vidrio", "plástico"]
        self.OptionForma = interfaceUsuario.StringVar()
        self.OptionForma.set(opcionesForma[0])  # Valor por defecto
        OptionMenu(contenedor, self.OptionForma, *opcionesForma).grid(row=3, column=1, padx=5, pady=5)

        auxdatoDiseno = interfaceUsuario.StringVar()
        labelR3 = Label(contenedor, text="Ingrese el diseño de la botella: ")
        labelR3.grid(row=4, column=0, padx=5, pady=5)
        self.EntryDiseno = Entry(contenedor, textvariable=auxdatoDiseno)
        self.EntryDiseno.grid(row=4, column=1, padx=5, pady=5)

        auxdatoTapa = interfaceUsuario.StringVar()
        labelR4 = Label(contenedor, text="Ingrese el diseño de la tapa: ")
        labelR4.grid(row=5, column=0, padx=5, pady=5)
        self.EntryTapa = Entry(contenedor, textvariable=auxdatoTapa)
        self.EntryTapa.grid(row=5, column=1, padx=5, pady=5)

        botonGuardar = Button(objformulario, text="Registrar", command=self.registrarBotella)
        botonGuardar.grid(row=6, column=0, pady=5, padx=5)

    def registrarBotella(self):
        auxDatoMaterial = self.EntryMaterial.get()
        auxdatoCapacidad = self.EntryCapacidad.get()
        auxdatoForma = self.OptionForma.get()
        auxdatoDiseno = self.EntryDiseno.get()
        auxdatoTapa = self.EntryTapa.get()

        self.botellas_registradas.registrarBotella(auxDatoMaterial, auxdatoCapacidad, auxdatoForma, auxdatoDiseno, auxdatoTapa)

        messagebox.showinfo("Registro exitoso", f"Botella de material {auxDatoMaterial} registrada exitosamente")

        self.EntryMaterial.delete(0, END)
        self.EntryCapacidad.delete(0, END)
        self.EntryDiseno.delete(0, END)
        self.EntryTapa.delete(0, END)

    def crearMenu(self, objformulario):
        barra_menu = Menu(objformulario)
        objformulario.config(menu=barra_menu)

        menu_opciones = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Opciones", menu=menu_opciones)
        menu_opciones.add_command(label="Modificar Botella", command=self.crearVentanaBuscarYModificar)
        menu_opciones.add_command(label="Buscar Botella", command=self.crearVentanaBuscarBotella)
        menu_opciones.add_command(label="Eliminar dato Botella", command=self.eliminarDatos)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Salir", command=objformulario.quit)

    def crearVentanaBuscarBotella(self):
        ventana_buscar = interfaceUsuario.Toplevel()
        ventana_buscar.title("Buscar datos de Botella")
        ventana_buscar.geometry("400x100")

        label = Label(ventana_buscar, text="Buscar Botella por material: ")
        label.grid(row=0, column=0, padx=5, pady=5)
        self.EntryBuscar = interfaceUsuario.StringVar()
        entry = Entry(ventana_buscar, textvariable=self.EntryBuscar)
        entry.grid(row=0, column=1, padx=8, pady=8)
        boton_buscar = Button(ventana_buscar, text="Buscar", command=self.buscarBotella)
        boton_buscar.grid(row=0, column=2, padx=5, pady=5)

    def buscarBotella(self):
        nombre_botella = self.EntryBuscar.get()
        info_botella = self.botellas_registradas.buscarBotella(nombre_botella)
        if info_botella:
            messagebox.showinfo("Informacion de la botella", info_botella)
        else:
            messagebox.showerror("Error", "Botella no encontrada")

    def crearVentanaBuscarYModificar(self):
        ventana_buscar = interfaceUsuario.Toplevel()
        ventana_buscar.title("Ventana buscar botella")
        ventana_buscar.geometry("500x400")
        ventana_buscar.config(bg="lightgray")

        label = Label(ventana_buscar, text="Buscar botella por material")
        label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.EntryModificar = interfaceUsuario.StringVar()
        entry = Entry(ventana_buscar, textvariable=self.EntryModificar)
        entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        boton_buscar = Button(ventana_buscar, text="Buscar", command=self.BuscarYModificar)
        boton_buscar.grid(row=0, column=2, padx=5, pady=5)

    def BuscarYModificar(self):
        material = self.EntryModificar.get()
        botella_encontrada = self.botellas_registradas.buscarBotella(material)
        if botella_encontrada:
            ventana_editar = interfaceUsuario.Toplevel()
            ventana_editar.title("Ventana modificar botella")
            ventana_editar.geometry("400x400")
            ventana_editar.config(bg="lightgray")

            labelN = Label(ventana_editar, text="Material Botella: ")
            labelN.grid(row=0, column=0, padx=5, pady=5)
            EntryMaterial_Nuevo = Entry(ventana_editar)
            EntryMaterial_Nuevo.grid(row=0, column=1, padx=5, pady=5)
            EntryMaterial_Nuevo.insert(0, botella_encontrada.material)

            labelN = Label(ventana_editar, text="Capacidad Botella: ")
            labelN.grid(row=1, column=0, padx=5, pady=5)
            EntryCapacidad_Nuevo = Entry(ventana_editar)
            EntryCapacidad_Nuevo.grid(row=1, column=1, padx=5, pady=5)
            EntryCapacidad_Nuevo.insert(0, botella_encontrada.capacidad)

            labelN = Label(ventana_editar, text="Forma Botella: ")
            labelN.grid(row=2, column=0, padx=5, pady=5)
            EntryForma_Nuevo = Entry(ventana_editar)
            EntryForma_Nuevo.grid(row=2, column=1, padx=5, pady=5)
            EntryForma_Nuevo.insert(0, botella_encontrada.forma)

            labelN = Label(ventana_editar, text="Diseño Botella: ")
            labelN.grid(row=3, column=0, padx=5, pady=5)
            EntryDiseno_Nuevo = Entry(ventana_editar)
            EntryDiseno_Nuevo.grid(row=3, column=1, padx=5, pady=5)
            EntryDiseno_Nuevo.insert(0, botella_encontrada.diseno)

            labelN = Label(ventana_editar, text="Diseño Tapa: ")
            labelN.grid(row=4, column=0, padx=5, pady=5)
            EntryTapa_Nuevo = Entry(ventana_editar)
            EntryTapa_Nuevo.grid(row=4, column=1, padx=5, pady=5)
            EntryTapa_Nuevo.insert(0, botella_encontrada.tapa)

            botonAceptar = Button(ventana_editar, text="Actualizar", command=lambda: self.actualizarYCerrarVentana(
                material, EntryMaterial_Nuevo, EntryCapacidad_Nuevo, EntryForma_Nuevo,
                EntryDiseno_Nuevo, EntryTapa_Nuevo, ventana_editar))
            botonAceptar.grid(row=5, column=0, padx=5, pady=5)
        else:
            messagebox.showerror("Error", "Material no encontrado")

    def actualizarYCerrarVentana(self, material, EntryMaterial_Nuevo, EntryCapacidad_Nuevo, EntryForma_Nuevo, EntryDiseno_Nuevo, EntryTapa_Nuevo, ventana_editar):
        exito = self.botellas_registradas.actualizarBotella(
            material, EntryMaterial_Nuevo.get(), EntryCapacidad_Nuevo.get(), EntryForma_Nuevo.get(),
            EntryDiseno_Nuevo.get(), EntryTapa_Nuevo.get())
        if exito:
            messagebox.showinfo("Actualización exitosa", "Botella actualizada correctamente")
            ventana_editar.destroy()
        else:
            messagebox.showerror("Error", "No se pudo actualizar la botella")

    def eliminarDatos(self):
        ventana_eliminar = interfaceUsuario.Toplevel()
        ventana_eliminar.title("Eliminar datos de botella")
        ventana_eliminar.geometry("400x100")

        label = Label(ventana_eliminar, text="Eliminar Botella por material: ")
        label.grid(row=0, column=0, padx=5, pady=5)
        self.EntryEliminar = interfaceUsuario.StringVar()
        entry = Entry(ventana_eliminar, textvariable=self.EntryEliminar)
        entry.grid(row=0, column=1, padx=8, pady=8)
        boton_eliminar = Button(ventana_eliminar, text="Eliminar", command=self.confirmarEliminar)
        boton_eliminar.grid(row=0, column=2, padx=5, pady=5)

    def confirmarEliminar(self):
        material = self.EntryEliminar.get()
        respuesta = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro que deseas eliminar el dato de la botella?")
        if respuesta:
            eliminado = self.botellas_registradas.eliminarDatoBotella(material)
            if eliminado:
                messagebox.showinfo("Eliminación exitosa", f"Dato de la botella con material {material} eliminado correctamente")
            else:
                messagebox.showerror("Error", "Material no encontrado")
        else:
            messagebox.showinfo("Eliminación cancelada", "Operación cancelada por el usuario")

if __name__ == "__main__":
    objInterfaz = Interfaz("lightblue")
    objformulario = objInterfaz.crearFormulario()
    contenedor = objInterfaz.crearContenedorRegistro(objformulario)
    objInterfaz.crearPreguntas(contenedor, objformulario)
    objInterfaz.crearMenu(objformulario)
    objformulario.mainloop()
