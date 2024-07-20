import tkinter as tk
from tkinter import messagebox

class ConoApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Volumen de Cono")
        self.root.geometry("300x250")
        
        self.label_radio = tk.Label(root, text="Ingrese el radio de la base del cono:")
        self.label_radio.pack(pady=10)
        
        self.radio_var = tk.DoubleVar()
        self.entry_radio = tk.Entry(root, textvariable=self.radio_var)
        self.entry_radio.pack(pady=10)

        self.label_altura = tk.Label(root, text="Ingrese la altura del cono:")
        self.label_altura.pack(pady=10)
        
        self.altura_var = tk.DoubleVar()
        self.entry_altura = tk.Entry(root, textvariable=self.altura_var)
        self.entry_altura.pack(pady=10)
        
        self.button_calcular = tk.Button(root, text="Calcular Volumen", command=self.calcular_volumen)
        self.button_calcular.pack(pady=10)
        
    def calcular_volumen(self):
        try:
            radio = self.radio_var.get()
            altura = self.altura_var.get()
            if radio <= 0 or altura <= 0:
                raise ValueError("El radio y la altura deben ser números positivos.")
            volumen = self.controlador.calcular_volumen(radio, altura)
            messagebox.showinfo("Resultado", f"El volumen del cono es: {volumen:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = ConoApp(root, controlador)
    root.mainloop()
