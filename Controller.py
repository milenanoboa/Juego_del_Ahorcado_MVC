"""
Controller - Controlador del juego 
Conecta el Model con la View y maneja el flujo del juego 
"""
from Model import HangmanModel
from View import HangmanView


class HangmanController:
    def __init__(self):
        self.model = HangmanModel()
        self.view = HangmanView()
        self.jugando = True

    def iniciar(self):
        """
        Inicia el juego y muestra el menú principal.
        Bucle WHILE: Mentiene el juego ejecutandose hasta que el jugador decida salir. Este bucle permite jugar inclusive hasta tres partidas sin reiniciar el programa 
        """
        # Bucle principal del juego: se ejecta mientras jugando sea True
        while self.jugando:
            self.mostrar_menu_principal()

    def mostrar_menu_principal(self):
        """
        Muestra el menú y procesa la elección del jugador
        Se utiliza la estructura condicional (if-elif-else): Evalua la opción del jugador y ejecuta la acción debida. Esta estructura permite manejar múltiples opciones de manera ordena.
        """
        self.view.mostrar_menu()
        opcion = self.view.pedir_opcion_menu()
            
        #Estructura de opción multiple para procesar la opción del menú
        #Opción 1= Iniciar Partida o jugar partida
        #Opción 2= Salir del juego
        #Opción invalida= mustrar el mensaje error y vualve a mostrar menú
        
        if opcion == '1':
                self.jugar_partida()
        elif opcion == '2':
                self.salir()
        else:
                self.view.mostrar_error_opcion()

    def jugar_partida(self):
         """
         Ejecuta la partida completa al iniciar el juego.
         Se menciona que esta es la funcionalidad mas compleja implentada en el Controller.
         Su función es coodinar el flujo completo de una partida: mostrar estado, recibir entrada, validar, actualizar y verificar el estado de victoria o derrota.

         Se utiliza el bucle (While True): Estructura infinita que se ejecuta hasta que se cumpla la condición de salida (victori o derrota).
         Se termina el bucle(break) al finalizar la partida o el juego.          
         """
         # Definir una nueva partida en el modelo
         self.model.nueva_partida()

         # Bucle principal de la partida: continia hasta ganar o perder el juego
         while True:
             # Paso 1: Obtener estado actual del juego.
              estado = self.model.obtener_estado()
              self.view.mostrar_juego(estado)

            # Paso 2: Verificar condición de VICTORIA - si el jugador adivino todas las letras, terminar con victoria.
            if self.model.esta_ganada():
               puntuacion = self.model.calcular_puntuacion()
               self.view.mostrar_victoria(estado['palabra_secreta'],puntuacion)
               self.view.esperar_continuar()
               break # Salir del bucle= partida terminada
         

