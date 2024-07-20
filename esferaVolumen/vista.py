import tkinter as tk
from tkinter import messagebox

class EsferaApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Volumen de Esfera")
        self.root.geometry("300x200")
        
        self.label_radio = tk.Label(root, text="Ingrese el radio de la esfera:")
        self.label_radio.pack(pady=10)
        
        self.radio_var = tk.DoubleVar()
        self.entry_radio = tk.Entry(root, textvariable=self.radio_var)
        self.entry_radio.pack(pady=10)
        
        self.button_calcular = tk.Button(root, text="Calcular Volumen", command=self.calcular_volumen)
        self.button_calcular.pack(pady=10)
        
    def calcular_volumen(self):
        try:
            radio = self.radio_var.get()
            if radio <= 0:
                raise ValueError("El radio debe ser un número positivo.")
            volumen = self.controlador.calcular_volumen(radio)
            messagebox.showinfo("Resultado", f"El volumen de la esfera es: {volumen:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = EsferaApp(root, controlador)
    root.mainloop()
