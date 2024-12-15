
from tkinter import Tk
from game import GuessingGame
from game_ai import GuessingAI
from graphics import GuessingGraphics

def main():
    root = Tk()
    game = GuessingGame()
    ai = GuessingAI()
    gui = GuessingGraphics(root, game, ai)
    root.mainloop()

if __name__ == "__main__":
    main()
