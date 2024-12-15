import tkinter as tk

class Graphics:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Sudoku")
        
        # Calculer la taille de l'écran et ajuster les dimensions des cases
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.cell_size = min(self.screen_width, self.screen_height) // 12  # Taille adaptative des cellules
        
        self.cells = {}  # Dictionnaire pour stocker les cases de la grille
        self.create_grid()
        self.root.mainloop()

    def create_grid(self):
        """Crée l'interface graphique pour le plateau de Sudoku."""
        for row in range(9):
            for col in range(9):

                # Définir l'épaisseur des bordures
                border_top = 2 if row % 3 == 0 else 1
                border_left = 2 if col % 3 == 0 else 1
                border_bottom = 2 if row == 8 else 1
                border_right = 2 if col == 8 else 1

                frame = tk.Frame(
                    self.root,
                    width=self.cell_size,
                    height=self.cell_size,
                    bg="white" if (border_top or border_left) else "black",  # Bordure blanche
                )
                frame.grid(row=row, column=col, padx=(border_left, border_right), pady=(border_top, border_bottom))

                value = self.game.current_grid[row][col]
                if value != 0:
                    label = tk.Label(frame, text=value, font=("Arial", 16))
                    label.pack(expand=True, fill="both")
                else:
                    entry = tk.Entry(frame, font=("Arial", 16), justify="center")
                    entry.pack(expand=True, fill="both")
                    entry.bind("<Return>", lambda e, r=row, c=col: self.on_input(r, c, entry))
                    self.cells[(row, col)] = entry

    def on_input(self, row, col, entry):
        """Gère l'entrée utilisateur pour une case."""
        try:
            value = int(entry.get())
            if self.game.make_move(row, col, value):
                entry.config(fg="black")  # Entrée valide
                if self.game.is_completed():
                    self.show_message("Félicitations, vous avez gagné !")
            else:
                entry.delete(0, tk.END)
                entry.config(fg="red")  # Entrée invalide
        except ValueError:
            entry.delete(0, tk.END)
            entry.config(fg="red")  # Entrée invalide

    def show_message(self, message):
        """Affiche un message de fin."""
        popup = tk.Toplevel()
        popup.title("Sudoku")
        tk.Label(popup, text=message, font=("Arial", 18)).pack(padx=20, pady=20)
        tk.Button(popup, text="OK", command=popup.destroy).pack(pady=10)
