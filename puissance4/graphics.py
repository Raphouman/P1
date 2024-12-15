import tkinter as tk
from game import Game

class Graphics:
    def __init__(self):
        self.game = Game()
        self.root = tk.Tk()
        self.root.title("Puissance 4")

        # Grille de jeu (6x7)
        self.canvas = tk.Canvas(self.root, width=700, height=600)
        self.canvas.pack()

        # Zone de statut
        self.status_label = tk.Label(self.root, text="C'est au tour du Joueur 1")
        self.status_label.pack()

        # Bouton de réinitialisation
        self.reset_button = tk.Button(self.root, text="Réinitialiser", command=self.reset_game)
        self.reset_button.pack()

        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)   # Lorsque le joueur clique sur la grille, la méthode handle_click est appelée

    def draw_board(self):
        """Dessine la grille du jeu."""
        for row in range(6):
            for col in range(7):
                x0, y0 = col * 100, row * 100 # Coin supérieur gauche, le fois 100 est pour la taille des cases (100x100 pixels)
                x1, y1 = x0 + 100, y0 + 100 # Coin inférieur droit
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", width=2)  #outline donne l'impression de séparation entre les cases
                # Dessine les jetons
                if self.game.board[row][col] == "Joueur 1":
                    self.canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill="red")
                elif self.game.board[row][col] == "Joueur 2":
                    self.canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill="yellow")

    def handle_click(self, event):  # event est un objet qui contient des informations sur l'événement
        """Gère le clic sur la grille pour jouer un coup."""
        column = event.x // 100  # Détecte la colonne sur laquelle le joueur a cliqué
        if self.game.make_move(column):
            self.draw_board()
            self.check_victory()

    def check_victory(self): # fonction de win mais graphique
        """Vérifie si un joueur a gagné et met à jour le statut."""
        if self.game.winner: #si différent de None initialisé dans la classe Game
            self.status_label.config(text=f"{self.game.winner} a gagné !")

        elif all(self.game.board[row][col] != " " for row in range(6) for col in range(7)):
            self.status_label.config(text="Match nul !")

        else:
            current_player = self.game.current_player
            self.status_label.config(text=f"C'est au tour de {current_player}")
        

    def reset_game(self):
        """Réinitialise le jeu."""
        self.canvas.delete("all")
        self.game.reset_game()
        self.draw_board()
        self.status_label.config(text="C'est au tour du Joueur 1")

    def run(self):
        """Lance l'application Tkinter."""
        self.root.mainloop()
