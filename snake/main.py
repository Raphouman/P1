#source /Users/RaphaelPICARD/env_msi/bin/activate


from graphics import SnakeGraphics
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeGraphics(root)
    root.mainloop()
