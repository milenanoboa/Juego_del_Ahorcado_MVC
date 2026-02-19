"""
View - Interfaz visual del juego
Maneja toda la presentación y visualización
"""
import os


class HangmanView:
    def __init__(self):
        self.dibujos = {
            6: """
  --------
  |      |
  |
  |
  |
  |
  |
 ---""",
            5: """
  --------
  |      |
  |      O
  |
  |
  |
  |
 ---""",
            4: """
  --------
  |      |
  |      O
  |      |
  |
  |
  |
 ---""",
            3: """
  --------
  |      |
  |      O
  |     /|
  |
  |
  |
 ---""",
            2: """
  --------
  |      |
  |      O
  |     /|\\
  |
  |
  |
 ---""",
            1: """
  --------
  |      |
  |      O
  |     /|\\
  |     /
  |
  |
 ---""",
            0: """
  --------
  |      |
  |      O
  |     /|\\
  |     / \\
  |
  |
 ---"""
        }

    def limpiar_pantalla(self):
        """
        Limpia la pantalla de la consola.
        """
        # Secuencia ANSI: mueve el cursor al inicio y borra toda la pantalla
       
        print("\033[H\033[J", end="")
    
    def mostrar_menu(self):
        """Muestra el menú principal"""
        self.limpiar_pantalla()
        print("\n" + "="*40)
        print("       🎮 JUEGO DEL AHORCADO 🎮")
        print("="*40)
        print("\n1) 🎯 Jugar Partida")
        print("2) ❌ Salir")
        print("\n" + "="*40)
    
    def mostrar_juego(self, estado):
        """Muestra el estado actual del juego"""
        self.limpiar_pantalla()
        print("\n" + "="*40)
        print("       🎯 A H O R C A D O")
        print("="*40)
        print(self.dibujos[estado['vidas']])
        print("\n" + "-"*40)
        print(f"💔 Vidas: {estado['vidas']}")
        print(f"📝 Usadas: {', '.join(sorted(estado['letras_usadas']))}")
        print(f"\n🔤 Progreso: {' '.join(estado['progreso'])}")
        
        # Mostrar letras erróneas debajo de la palabra
        if estado['letras_fallidas']:
            print(f"❌ Erróneas: {' '.join(sorted(estado['letras_fallidas']))}")
        else:
            print("❌ Erróneas: (ninguna)")
        
        print("-"*40)
    
    def pedir_letra(self):
        """Solicita al usuario que ingrese una letra"""
        return input("\n✏️  Ingresa una letra: ").strip()
    
    def mostrar_mensaje(self, mensaje, tipo="info"):
        """Muestra un mensaje al usuario"""
        iconos = {
            "info": "ℹ️",
            "error": "⚠️",
            "exito": "✅",
            "game_over": "💀"
        }
        icono = iconos.get(tipo, "")
        print(f"\n{icono} {mensaje}")
    
    def mostrar_victoria(self, palabra, puntuacion):
        """Muestra el mensaje de victoria"""
        print("\n" + "="*40)
        print("       🎉 ¡FELICIDADES! 🎉")
        print("="*40)
        print(f"\n✨ Palabra: {palabra.upper()}")
        print(f"⭐ Puntuación: {puntuacion} puntos")
        print("\n¡Ganaste la partida!")
        print("="*40)
    
    def mostrar_derrota(self, palabra):
        """Muestra el mensaje de derrota"""
        print("\n" + "="*40)
        print("       💀 GAME OVER 💀")
        print("="*40)
        print(f"\n📖 La palabra era: {palabra.upper()}")
        print("\n¡Mejor suerte la próxima vez!")
        print("="*40)
    
    def esperar_continuar(self):
        """Espera a que el usuario presione enter"""
        input("\n📌 Presiona ENTER para continuar...")
    
    def pedir_opcion_menu(self):
        """Solicita al usuario una opción del menú"""
        return input("\n➡️  Elige una opción: ").strip()
    
    def mostrar_error_opcion(self):
        """Muestra error de opción inválida"""
        self.mostrar_mensaje("Opción inválida. Intenta de nuevo.", "error")
        self.esperar_continuar()