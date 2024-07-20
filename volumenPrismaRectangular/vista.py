import tkinter as tk
from tkinter import messagebox

class PrismaApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Volumen de Prisma Rectangular")
        self.root.geometry("300x300")
        
        self.label_longitud = tk.Label(root, text="Ingrese la longitud del prisma:")
        self.label_longitud.pack(pady=10)
        
        self.longitud_var = tk.DoubleVar()
        self.entry_longitud = tk.Entry(root, textvariable=self.longitud_var)
        self.entry_longitud.pack(pady=10)

        self.label_ancho = tk.Label(root, text="Ingrese el ancho del prisma:")
        self.label_ancho.pack(pady=10)
        
        self.ancho_var = tk.DoubleVar()
        self.entry_ancho = tk.Entry(root, textvariable=self.ancho_var)
        self.entry_ancho.pack(pady=10)
        
        self.label_altura = tk.Label(root, text="Ingrese la altura del prisma:")
        self.label_altura.pack(pady=10)
        
        self.altura_var = tk.DoubleVar()
        self.entry_altura = tk.Entry(root, textvariable=self.altura_var)
        self.entry_altura.pack(pady=10)
        
        self.button_calcular = tk.Button(root, text="Calcular Volumen", command=self.calcular_volumen)
        self.button_calcular.pack(pady=10)
        
    def calcular_volumen(self):
        try:
            longitud = self.longitud_var.get()
            ancho = self.ancho_var.get()
            altura = self.altura_var.get()
            if longitud <= 0 or ancho <= 0 or altura <= 0:
                raise ValueError("La longitud, el ancho y la altura deben ser números positivos.")
            volumen = self.controlador.calcular_volumen(longitud, ancho, altura)
            messagebox.showinfo("Resultado", f"El volumen del prisma es: {volumen:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = PrismaApp(root, controlador)
    root.mainloop()
