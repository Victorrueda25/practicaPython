import tkinter as tk
from tkinter import messagebox

class RectanguloApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Área de Rectángulo")
        self.root.geometry("300x200")
        
        self.label_base = tk.Label(root, text="Ingrese la base del rectángulo:")
        self.label_base.pack(pady=10)
        
        self.base_var = tk.DoubleVar()
        self.entry_base = tk.Entry(root, textvariable=self.base_var)
        self.entry_base.pack(pady=10)
        
        self.label_altura = tk.Label(root, text="Ingrese la altura del rectángulo:")
        self.label_altura.pack(pady=10)
        
        self.altura_var = tk.DoubleVar()
        self.entry_altura = tk.Entry(root, textvariable=self.altura_var)
        self.entry_altura.pack(pady=10)
        
        self.button_calcular = tk.Button(root, text="Calcular Área", command=self.calcular_area)
        self.button_calcular.pack(pady=10)
        
    def calcular_area(self):
        try:
            base = self.base_var.get()
            altura = self.altura_var.get()
            if base <= 0 or altura <= 0:
                raise ValueError("La base y la altura deben ser números positivos.")
            self.controlador.establecer_lado(base, altura)
            area = self.controlador.calcular_area()
            messagebox.showinfo("Resultado", f"El área del rectángulo es: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = RectanguloApp(root, controlador)
    root.mainloop()
