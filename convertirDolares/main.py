from controlador import ControladorConversor
from vista import iniciar_aplicacion

if __name__ == "__main__":
    tasa_cambio = 0.85  # Ejemplo de tasa de cambio
    controlador = ControladorConversor(tasa_cambio)
    iniciar_aplicacion(controlador)
