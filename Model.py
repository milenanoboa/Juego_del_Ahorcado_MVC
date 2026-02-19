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
        
        # LÓGICA PRINCIPAL: Verificar si la letra está en la palabra secreta
        if letra in self.palabra_secreta:
            # La letra es CORRECTA - Actualizar el progreso de la palabra
            
            # Convertir el progreso actual a una lista para modificación
            nueva_progreso = list(self.palabra_progreso)
            
            # ESTRUCTURA REPETITIVA (for): Recorrer cada posición de la palabra
            # enumerate() nos da tanto el índice (i) como el carácter (char)
            for i, char in enumerate(self.palabra_secreta):
                # Si el carácter coincide con la letra ingresada
                if char == letra:
                    # Reemplazar el guión por la letra en esa posición
                    nueva_progreso[i] = letra
            
            # Convertir la lista de vuelta a string
            self.palabra_progreso = "".join(nueva_progreso)
            return True, "¡Correcto!"
        else:
            # La letra es INCORRECTA
            # Agregar a la lista de fallos y restar una vida
            self.letras_fallidas.append(letra)
            self.vidas -= 1
            return False, "Letra incorrecta"
    
    def esta_ganada(self):
        """Verifica si el jugador ganó"""
        return "-" not in self.palabra_progreso
    
    def esta_perdida(self):
        """Verifica si el jugador perdió"""
        return self.vidas <= 0
    
    def calcular_puntuacion(self):
        """Calcula la puntuación basada en vidas restantes y longitud de palabra"""
        if self.esta_ganada():
            self.puntuacion = self.vidas * len(self.palabra_secreta) * 10
            return self.puntuacion
        return 0
    
    def obtener_estado(self):
        """Retorna el estado actual del juego"""
        return {
            'progreso': self.palabra_progreso,
            'vidas': self.vidas,
            'letras_fallidas': self.letras_fallidas,
            'letras_usadas': self.letras_usadas,
            'ganada': self.esta_ganada(),
            'perdida': self.esta_perdida(),
            'palabra_secreta': self.palabra_secreta
        }