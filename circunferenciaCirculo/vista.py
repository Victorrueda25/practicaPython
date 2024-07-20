import tkinter as tk
from tkinter import messagebox

class CirculoApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Circunferencia")
        self.root.geometry("300x200")
        
        self.label_radio = tk.Label(root, text="Ingrese el radio del círculo:")
        self.label_radio.pack(pady=10)
        
        self.radio_var = tk.DoubleVar()
        self.entry_radio = tk.Entry(root, textvariable=self.radio_var)
        self.entry_radio.pack(pady=10)
        
        self.button_calcular = tk.Button(root, text="Calcular Circunferencia", command=self.calcular_circunferencia)
        self.button_calcular.pack(pady=10)
        
    def calcular_circunferencia(self):
        try:
            radio = self.radio_var.get()
            if radio <= 0:
                raise ValueError("El radio debe ser un número positivo.")
            resultado = self.controlador.calcular_circunferencia(radio)
            messagebox.showinfo("Resultado", f"La circunferencia del círculo es: {resultado:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = CirculoApp(root, controlador)
    root.mainloop()
