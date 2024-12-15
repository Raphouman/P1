from game import MazeGame
from graphics import MazeGraphics

def main():
    game = MazeGame(width=15, height=15)  # Crée une instance du jeu
    graphics = MazeGraphics(game)  # Associe l'interface graphique au jeu
    graphics.run()  # Lance l'interface graphique

if __name__ == "__main__":
    main()
