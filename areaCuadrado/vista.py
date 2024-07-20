import tkinter as tk
from tkinter import messagebox

class CuadradoApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Área de Cuadrado")
        self.root.geometry("300x200")
        
        self.label_lado = tk.Label(root, text="Ingrese el lado del cuadrado:")
        self.label_lado.pack(pady=10)
        
        self.lado_var = tk.DoubleVar()
        self.entry_lado = tk.Entry(root, textvariable=self.lado_var)
        self.entry_lado.pack(pady=10)
        
        self.button_calcular = tk.Button(root, text="Calcular Área", command=self.calcular_area)
        self.button_calcular.pack(pady=10)
        
    def calcular_area(self):
        try:
            lado = self.lado_var.get()
            if lado <= 0:
                raise ValueError("El lado debe ser un número positivo.")
            self.controlador.establecer_lado(lado)
            area = self.controlador.calcular_area()
            messagebox.showinfo("Resultado", f"El área del cuadrado es: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = CuadradoApp(root, controlador)
    root.mainloop()
