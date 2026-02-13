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

    def nueva_partida(self):
        """Inicializa una nueva partida"""
        self.palabra_secreta = random.choice(self.palabras)
        self.palabra_progreso = "-" * len(self.palabra_secreta)
        self.letras_fallidas = []
        self.letras_usadas = []
        self.vidas = self.vidas_maximas
        
    def intentar_letra(self, letra):
        """
        Procesa un intento de letra ingresada por el jugador.
        Esta es una funcionalidad compleja que valida la entrada,
        actualiza el estado del juego y retorna el resultado.
        
        Args:
            letra (str): La letra ingresada por el jugador
            
        Returns:
            tuple: (es_correcta, mensaje)
                - es_correcta (bool): True si la letra está en la palabra
                - mensaje (str): Mensaje descriptivo del resultado
        """
        
        # Convertir a minúscula para comparación uniforme
        letra = letra.lower()
        
        # VALIDACIÓN 1: Verificar que sea una sola letra alfabética
        # Utiliza estructura condicional para validar el formato de entrada
        if len(letra) != 1 or not letra.isalpha():
            return False, "Ingresa solo una letra válida"
        
        # VALIDACIÓN 2: Verificar que la letra no haya sido usada antes
        # Esto evita que el jugador pierda vidas por letras repetidas
        if letra in self.letras_usadas:
            return False, "Ya usaste esa letra"
        
        # Agregar la letra a la lista de letras usadas
        self.letras_usadas.append(letra)