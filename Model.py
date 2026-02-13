"""
Model - Lógica del juego del Ahorcado
Maneja el estado del juego y las reglas
"""
import random


class HangmanModel:
    def __init__(self):
        self.palabras = [
            "monalisa", "lalaland", "luciernagas", "guernica", "venus",
            "francia", "estrellas", "luna", "mar", "italia"
        ]
        self.palabra_secreta = ""
        self.palabra_progreso = ""
        self.letras_fallidas = []
        self.letras_usadas = []
        self.vidas = 6
        self.vidas_maximas = 6
        self.puntuacion = 0
        