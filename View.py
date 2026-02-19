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
        