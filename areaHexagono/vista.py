import tkinter as tk
from tkinter import messagebox

class HexagonoApp:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Calculadora de Área de Hexágono Regular")
        self.root.geometry("300x200")
        
        self.label_lado = tk.Label(root, text="Ingrese la longitud del lado del hexágono:")
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
            area = self.controlador.calcular_area(lado)
            messagebox.showinfo("Resultado", f"El área del hexágono es: {area:.2f} unidades cuadradas")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def iniciar_aplicacion(controlador):
    root = tk.Tk()
    app = HexagonoApp(root, controlador)
    root.mainloop()
