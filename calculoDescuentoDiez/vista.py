import tkinter as tk
from tkinter import messagebox
from controlador import ControladorArticulo

class ArticuloApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Descuento")
        self.root.geometry("300x200")

        self.label_precio = tk.Label(root, text="Ingrese el precio del artículo:")
        self.label_precio.pack(pady=10)

        self.precio_var = tk.DoubleVar()
        self.entry_precio = tk.Entry(root, textvariable=self.precio_var)
        self.entry_precio.pack(pady=10)

        self.button_calcular = tk.Button(root, text="Calcular Descuento", command=self.calcular_descuento)
        self.button_calcular.pack(pady=10)

    def calcular_descuento(self):
        try:
            precio = self.precio_var.get()
            if precio <= 0:
                raise ValueError("El precio debe ser un número positivo.")
            self.controlador.establecer_precio(precio)
            descuento, precio_final = self.controlador.calcular_descuento()
            messagebox.showinfo("Resultado", f"Descuento: {descuento:.2f}\nPrecio final: {precio_final:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = ArticuloApp(root, controlador)
    root.mainloop()
