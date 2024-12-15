from graphics import Graphics
from game import SudokuGame

def main():
    # Crée une instance du jeu
    game = SudokuGame()
    # Démarre l'interface graphique avec le jeu en paramètre
    Graphics(game)

if __name__ == "__main__":
    main()
