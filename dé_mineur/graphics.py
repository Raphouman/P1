import tkinter as tk

class MinesweeperGraphics:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Démineur")
        self.buttons = {}
        self.create_grid()
        self.root.mainloop()

    def create_grid(self):
        """Crée l'interface graphique pour le plateau de jeu."""
        for row in range(self.game.rows):
            for col in range(self.game.cols):
                button = tk.Button(self.root, width=4, height=2, command=lambda r=row, c=col: self.on_click(r, c))
                button.bind("<Button-3>", lambda e, r=row, c=col: self.on_right_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[(row, col)] = button

    def on_click(self, row, col):
        """Gère le clic gauche pour révéler une cellule."""
        self.game.reveal_cell(row, col)
        self.update_grid()

        if self.game.game_over:
            self.show_message("Perdu !")
        elif self.game.check_win():
            self.show_message("Gagné !")

    def on_right_click(self, row, col):
        """Gère le clic droit pour placer ou retirer un drapeau."""
        self.game.toggle_flag(row, col)
        self.update_grid()

    def update_grid(self):
        """Met à jour l'affichage du plateau."""
        for row in range(self.game.rows):
            for col in range(self.game.cols):
                cell = self.game.grid[row][col]
                button = self.buttons[(row, col)]

                if cell.is_revealed:
                    if cell.is_mine:
                        button.config(text="💣", bg="red")
                    else:
                        button.config(text=str(cell.adjacent_mines) if cell.adjacent_mines > 0 else "", bg="lightgrey")
                elif cell.is_flagged:
                    button.config(text="🚩", bg="yellow")
                else:
                    button.config(text="", bg="SystemButtonFace")

    def show_message(self, message):
        """Affiche un message de fin."""
        popup = tk.Toplevel()
        popup.title("Fin de jeu")
        tk.Label(popup, text=message, font=("Arial", 18)).pack(pady=20)
        tk.Button(popup, text="OK", command=lambda: [popup.destroy(), self.root.destroy()]).pack(pady=10)
