import tkinter as tk
from tkinter import messagebox
from controlador import ControladorNumeros

class NumerosApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Mayor")
        self.root.geometry("300x200")

        self.label_numero1 = tk.Label(root, text="Ingrese el primer número:")
        self.label_numero1.pack(pady=10)

        self.numero1_var = tk.DoubleVar()
        self.entry_numero1 = tk.Entry(root, textvariable=self.numero1_var)
        self.entry_numero1.pack(pady=10)

        self.label_numero2 = tk.Label(root, text="Ingrese el segundo número:")
        self.label_numero2.pack(pady=10)

        self.numero2_var = tk.DoubleVar()
        self.entry_numero2 = tk.Entry(root, textvariable=self.numero2_var)
        self.entry_numero2.pack(pady=10)

        self.button_calcular = tk.Button(root, text="Calcular Mayor", command=self.calcular_mayor)
        self.button_calcular.pack(pady=10)

    def calcular_mayor(self):
        try:
            numero1 = self.numero1_var.get()
            numero2 = self.numero2_var.get()
            self.controlador.establecer_numeros(numero1, numero2)
            mayor = self.controlador.calcular_mayor()
            messagebox.showinfo("Resultado", f"El mayor de los dos números es: {mayor}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = NumerosApp(root, controlador)
    root.mainloop()
