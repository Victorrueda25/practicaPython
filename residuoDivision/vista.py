import tkinter as tk
from tkinter import messagebox

class ResiduoApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Residuo")
        self.root.geometry("300x200")
        
        self.label_dividendo = tk.Label(root, text="Ingrese el dividendo:")
        self.label_dividendo.pack(pady=10)
        
        self.dividendo_var = tk.DoubleVar()
        self.entry_dividendo = tk.Entry(root, textvariable=self.dividendo_var)
        self.entry_dividendo.pack(pady=10)
        
        self.label_divisor = tk.Label(root, text="Ingrese el divisor:")
        self.label_divisor.pack(pady=10)
        
        self.divisor_var = tk.DoubleVar()
        self.entry_divisor = tk.Entry(root, textvariable=self.divisor_var)
        self.entry_divisor.pack(pady=10)
        
        self.button_calcular = tk.Button(root, text="Calcular Residuo", command=self.calcular_residuo)
        self.button_calcular.pack(pady=10)
        
    def calcular_residuo(self):
        try:
            dividendo = self.dividendo_var.get()
            divisor = self.divisor_var.get()
            if divisor == 0:
                raise ValueError("El divisor no puede ser cero.")
            resultado = self.controlador.calcular_residuo(dividendo, divisor)
            messagebox.showinfo("Resultado", f"El residuo de {dividendo} dividido por {divisor} es: {resultado:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = ResiduoApp(root, controlador)
    root.mainloop()
