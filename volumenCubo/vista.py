import tkinter as tk
from tkinter import messagebox

class CuboApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Volumen de Cubo")
        self.root.geometry("300x200")
        
        self.label_lado = tk.Label(root, text="Ingrese la longitud del lado del cubo:")
        self.label_lado.pack(pady=10)
        
        self.lado_var = tk.DoubleVar()
        self.entry_lado = tk.Entry(root, textvariable=self.lado_var)
        self.entry_lado.pack(pady=10)
        
        self.button_calcular = tk.Button(root, text="Calcular Volumen", command=self.calcular_volumen)
        self.button_calcular.pack(pady=10)
        
    def calcular_volumen(self):
        try:
            lado = self.lado_var.get()
            if lado <= 0:
                raise ValueError("El lado debe ser un número positivo.")
            volumen = self.controlador.calcular_volumen(lado)
            messagebox.showinfo("Resultado", f"El volumen del cubo es: {volumen:.2f} unidades cúbicas")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = CuboApp(root, controlador)
    root.mainloop()
