import tkinter as tk
from tkinter import messagebox

class ConversorApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Conversor de Litros a Galones")
        self.root.geometry("300x200")
        
        self.label_litros = tk.Label(root, text="Ingrese el valor en litros:")
        self.label_litros.pack(pady=10)
        
        self.litros_var = tk.DoubleVar()
        self.entry_litros = tk.Entry(root, textvariable=self.litros_var)
        self.entry_litros.pack(pady=10)
        
        self.button_convertir = tk.Button(root, text="Convertir a Galones", command=self.convertir_a_galones)
        self.button_convertir.pack(pady=10)
        
    def convertir_a_galones(self):
        try:
            litros = self.litros_var.get()
            if litros <= 0:
                raise ValueError("El valor debe ser un número positivo.")
            galones = self.controlador.convertir_a_galones(litros)
            messagebox.showinfo("Resultado", f"{litros} litros son {galones:.2f} galones")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = ConversorApp(root, controlador)
    root.mainloop()
