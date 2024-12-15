import tkinter as tk
from game import CheckersGame

class CheckersGraphics:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Dames")
        self.game = CheckersGame()

        # Dimensions
        self.cell_size = 80
        self.board_size = self.cell_size * 8

        # Canvas pour afficher le plateau
        self.canvas = tk.Canvas(root, width=self.board_size, height=self.board_size, bg="white")
        self.canvas.pack()

        # Zone d'information pour afficher le joueur actuel et les messages
        self.info_label = tk.Label(root, text="Tour du joueur : Rouge", font=("Arial", 16))
        self.info_label.pack()

        # Liaison des clics
        self.canvas.bind("<Button-1>", self.on_click)

        # Affichage initial
        self.draw_board()
        self.update_pieces()

    def draw_board(self):
        """Dessine le plateau de jeu."""
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "gray"
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def update_pieces(self):
        """Met à jour les pièces sur le plateau."""
        self.canvas.delete("piece")
        for row in range(8):
            for col in range(8):
                piece = self.game.board.get_piece(row, col)
                if piece:
                    x1 = col * self.cell_size + 10
                    y1 = row * self.cell_size + 10
                    x2 = (col + 1) * self.cell_size - 10
                    y2 = (row + 1) * self.cell_size - 10
                    color = "red" if piece.color == "red" else "black"
                    self.canvas.create_oval(x1, y1, x2, y2, fill=color, tags="piece")

        # Indicateur de pièce sélectionnée
        if self.game.selected_piece:
            row, col = self.game.selected_piece
            x1 = col * self.cell_size + 5
            y1 = row * self.cell_size + 5
            x2 = (col + 1) * self.cell_size - 5
            y2 = (row + 1) * self.cell_size - 5
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="yellow", width=3, tags="piece")
        self.update_turn_display()


    def update_turn_display(self):
        """Met à jour l'affichage du joueur actuel."""
        current_player = "Rouge" if self.game.turn == "red" else "Noir"
        self.info_label.config(text=f"Tour du joueur : {current_player}")


    def on_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if self.game.select_piece(row, col):
            self.info_label.config(text=f"Tour du joueur : {'Noir' if self.game.turn == 'black' else 'Rouge'}")
        else:
            self.info_label.config(text="Mouvement invalide ou case vide. Réessayez.")

        self.update_pieces()

        # Vérification des reines
        for row in range(len(self.game.board.grid)):
            for col in range(len(self.game.board.grid[row])):
                piece = self.game.board.get_piece(row, col)
                if piece and piece.is_queen:
                    self.info_label.config(text=f"Promotion ! {piece.color} devient reine.")


    def draw_pieces(self):
        """Dessine toutes les pièces sur le plateau."""
        for row in range(len(self.game.board.grid)):
            for col in range(len(self.game.board.grid[row])):
                piece = self.game.board.get_piece(row, col)
                if piece:
                    x1 = col * self.cell_size + 10
                    y1 = row * self.cell_size + 10
                    x2 = (col + 1) * self.cell_size - 10
                    y2 = (row + 1) * self.cell_size - 10

                    # Dessiner les pions
                    self.canvas.create_oval(x1, y1, x2, y2, fill=piece.color)

                    # Dessiner une reine (indiquée par un cercle supplémentaire)
                    if piece.is_queen:
                        self.canvas.create_oval(
                            x1 + 10, y1 + 10, x2 - 10, y2 - 10, outline="gold", width=2
                        )

