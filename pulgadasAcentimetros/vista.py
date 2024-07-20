import tkinter as tk
from tkinter import messagebox

class ConversorApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Conversor de Pulgadas a Centímetros")
        self.root.geometry("300x200")
        
        self.label_pulgadas = tk.Label(root, text="Ingrese el valor en pulgadas:")
        self.label_pulgadas.pack(pady=10)
        
        self.pulgadas_var = tk.DoubleVar()
        self.entry_pulgadas = tk.Entry(root, textvariable=self.pulgadas_var)
        self.entry_pulgadas.pack(pady=10)
        
        self.button_convertir = tk.Button(root, text="Convertir a Centímetros", command=self.convertir_a_centimetros)
        self.button_convertir.pack(pady=10)
        
    def convertir_a_centimetros(self):
        try:
            pulgadas = self.pulgadas_var.get()
            if pulgadas <= 0:
                raise ValueError("El valor debe ser un número positivo.")
            centimetros = self.controlador.convertir_a_centimetros(pulgadas)
            messagebox.showinfo("Resultado", f"{pulgadas} pulgadas son {centimetros:.2f} centímetros")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = ConversorApp(root, controlador)
    root.mainloop()
