import tkinter as tk
from game import Game

class Graphics:
    def __init__(self):
        self.game = Game()
        self.root = tk.Tk()
        self.root.title("Morpion")

        # Grille de jeu comme une liste de boutons
        self.buttons = [tk.Button(self.root, text=" ", width=10, height=3, command=lambda i=i: self.handle_click(i)) for i in range(9)]  # lambda i=i est une astuce pour capturer la valeur actuelle de i, sinon i vaudrait 9 pour tous les boutons
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)   # i//3 et i%3 calculent la ligne et la colonne de chaque bouton

        # Statut du jeu
        self.status_label = tk.Label(self.root, text="C'est au tour de X")
        self.status_label.grid(row=3, column=0, columnspan=3)

        # Bouton de réinitialisation
        self.reset_button = tk.Button(self.root, text="Réinitialiser", command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3)   # columnspan étend le bouton sur 3 colonnes

    def handle_click(self, position):
        """Gère le clic sur un bouton de la grille."""
        if self.game.make_move(position):   # make_move renvoie True si le coup est valide
            self.update_buttons()
            self.check_victory()
        else:
            self.status_label.config(text="Case déjà occupée ou jeu terminé")

    def update_buttons(self):
        """Met à jour les boutons en fonction de l'état actuel du plateau."""
        board = self.game.get_board()
        for i, button in enumerate(self.buttons):
            button.config(text=board[i])    # Met à jour le texte de chaque bouton

    def check_victory(self):
        """Vérifie la victoire ou l'égalité."""
        if self.game.winner:
            self.status_label.config(text=f"{self.game.winner} a gagné !")
        elif " " not in self.game.get_board():
            self.status_label.config(text="Égalité !")
        else:
            current_player = self.game.current_player
            self.status_label.config(text=f"C'est au tour de {current_player}")

    def reset_game(self):
        """Réinitialise le jeu."""
        self.game.reset_game()
        self.update_buttons()
        self.status_label.config(text="C'est au tour de X")

    def run(self):
        self.root.mainloop()