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
            
            #PROGRAMACION FUNCIONAL AGREGADA: se utiliza map() transforma cada par (caracter_secreto, progreso_actual)
            #Si el caracter coincide con la letra, lo revela; si no, conserva el estado actual.
            # Esto reemplazaria el bucle FOR anterio por una funcion pura.
            self.palabra_progreso= "".join(
                map(lambda par: par[0] if par[0] == letra else par[1],
                    zip(self.palabra_secreta, self.palabra_progreso))
            )
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
        """Calcula la puntuación basada en vidas restantes y longitud de palabra
        PROGRAMACIÓN FUNCIONAL: filter() extrae solo las letras usadas que
        están en la palabra secreta, es decir las letras correctas acertadas.
        Es una función que no modifica el estado, solo calcula y retorna un valor.
        """
        if self.esta_ganada():
            letras_correctas = list(filter(lambda l: l in self.palabr_secreta, self.letras_usadas))
            self.puntuacion = self.vidas * len(letras_correctas) * 10
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