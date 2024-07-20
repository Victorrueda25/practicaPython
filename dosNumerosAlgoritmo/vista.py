import tkinter as tk
from tkinter import messagebox

class RestaApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Resta")
        self.root.geometry("300x200")
        
        self.label_minuendo = tk.Label(root, text="Ingrese el minuendo:")
        self.label_minuendo.pack(pady=10)
        
        self.minuendo_var = tk.DoubleVar()
        self.entry_minuendo = tk.Entry(root, textvariable=self.minuendo_var)
        self.entry_minuendo.pack(pady=10)
        
        self.label_sustraendo = tk.Label(root, text="Ingrese el sustraendo:")
        self.label_sustraendo.pack(pady=10)
        
        self.sustraendo_var = tk.DoubleVar()
        self.entry_sustraendo = tk.Entry(root, textvariable=self.sustraendo_var)
        self.entry_sustraendo.pack(pady=10)
        
        self.button_calcular = tk.Button(root, text="Calcular Resta", command=self.calcular_resta)
        self.button_calcular.pack(pady=10)
        
    def calcular_resta(self):
        try:
            minuendo = self.minuendo_var.get()
            sustraendo = self.sustraendo_var.get()
            resultado = self.controlador.calcular_resta(minuendo, sustraendo)
            messagebox.showinfo("Resultado", f"La resta es: {resultado:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = RestaApp(root, controlador)
    root.mainloop()
