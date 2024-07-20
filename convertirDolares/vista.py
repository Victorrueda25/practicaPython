import tkinter as tk
from tkinter import messagebox

class ConversorApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Conversor de Dólares a Euros")
        self.root.geometry("300x200")
        
        self.label_dolares = tk.Label(root, text="Ingrese la cantidad en dólares:")
        self.label_dolares.pack(pady=10)
        
        self.dolares_var = tk.DoubleVar()
        self.entry_dolares = tk.Entry(root, textvariable=self.dolares_var)
        self.entry_dolares.pack(pady=10)
        
        self.label_tasa = tk.Label(root, text=f"Tasa de cambio (1 dólar = {self.controlador.conversor.tasa_cambio} euros)")
        self.label_tasa.pack(pady=10)
        
        self.button_convertir = tk.Button(root, text="Convertir", command=self.convertir)
        self.button_convertir.pack(pady=10)
        
    def convertir(self):
        try:
            dolares = self.dolares_var.get()
            if dolares <= 0:
                raise ValueError("La cantidad de dólares debe ser un número positivo.")
            euros = self.controlador.convertir(dolares)
            messagebox.showinfo("Resultado", f"{dolares} dólares son {euros:.2f} euros")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = ConversorApp(root, controlador)
    root.mainloop()
