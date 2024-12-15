import tkinter as tk

class MazeGraphics:
    def __init__(self, game):
        self.game = game
        self.cell_size = 40
        self.root = tk.Tk()
        self.root.title("Maze Runner")
        self.canvas = tk.Canvas(
            self.root, 
            width=self.game.width * self.cell_size, 
            height=self.game.height * self.cell_size, 
            bg="white"
        )
        self.canvas.pack()

        self.status_label = tk.Label(self.root, text="Trouvez la sortie !", font=("Arial", 14))
        self.status_label.pack()

        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack()

        self.root.bind("<KeyPress>", self.handle_keypress)

    def draw_maze(self):
        """Dessine le labyrinthe et les positions."""
        self.canvas.delete("all")
        for i in range(self.game.height):
            for j in range(self.game.width):
                x0, y0 = j * self.cell_size, i * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                color = "black" if self.game.maze[i][j] == 1 else "white"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="gray")

        # Dessiner le joueur
        px, py = self.game.player_position
        self.canvas.create_oval(
            py * self.cell_size + 5, px * self.cell_size + 5,
            py * self.cell_size + self.cell_size - 5, px * self.cell_size + self.cell_size - 5,
            fill="blue"
        )

        # Dessiner la sortie
        ex, ey = self.game.exit_position
        self.canvas.create_rectangle(
            ey * self.cell_size + 5, ex * self.cell_size + 5,
            ey * self.cell_size + self.cell_size - 5, ex * self.cell_size + self.cell_size - 5,
            fill="green"
        )

    def handle_keypress(self, event):
        """Gère les déplacements du joueur."""
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            directions = {
                "Up": "up", "Down": "down",
                "Left": "left", "Right": "right"
            }
            self.game.move_player(directions[event.keysym])
            self.update_game()

    def update_game(self):
        """Met à jour l'état du jeu."""
        self.draw_maze()
        if self.game.is_game_over():
            self.status_label.config(text="Bravo, vous avez gagné !")
            self.root.unbind("<KeyPress>")

    def start_game(self):
        """Démarre une nouvelle partie."""
        self.game.reset_game()
        self.game.generate_maze()
        self.draw_maze()
        self.status_label.config(text="Trouvez la sortie !")
        self.root.bind("<KeyPress>", self.handle_keypress)

    def run(self):
        self.root.mainloop()
