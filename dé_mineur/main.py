from game import MinesweeperGame
from graphics import MinesweeperGraphics

if __name__ == "__main__":
    game = MinesweeperGame(rows=10, cols=10, mines=15)
    graphics = MinesweeperGraphics(game)
