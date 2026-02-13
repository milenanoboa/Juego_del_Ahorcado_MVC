"""
Juego del Ahorcado - Versión Python con arquitectura MVC
Archivo principal para ejecutar el juego
"""
from Controller import HangmanController


def main():
    """Función principal del programa"""
    juego = HangmanController()
    juego.iniciar()


if __name__ == "__main__":
    main()
