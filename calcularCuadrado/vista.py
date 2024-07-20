import tkinter as tk
from tkinter import messagebox

class CuadradoApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Cuadrado")
        self.root.geometry("300x200")
        
        self.label_numero = tk.Label(root, text="Ingrese un número:")
        self.label_numero.pack(pady=10)
        
        self.numero_var = tk.DoubleVar()
        self.entry_numero = tk.Entry(root, textvariable=self.numero_var)
        self.entry_numero.pack(pady=10)
        
        self.button_calcular = tk.Button(root, text="Calcular Cuadrado", command=self.calcular_cuadrado)
        self.button_calcular.pack(pady=10)
        
    def calcular_cuadrado(self):
        try:
            numero = self.numero_var.get()
            resultado = self.controlador.calcular_cuadrado(numero)
            messagebox.showinfo("Resultado", f"El cuadrado de {numero} es: {resultado:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = CuadradoApp(root, controlador)
    root.mainloop()
