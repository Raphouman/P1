import tkinter as tk
from game import Game

class Graphics:
    def __init__(self):
        self.game = Game()
        self.game.place_ships_auto("opponent")  # L'adversaire place ses bateaux automatiquement.

        self.root = tk.Tk()
        self.root.title("Bataille Navale")

        # État du placement des bateaux
        self.placing_phase = True
        self.current_ship_size = 3  # Taille du bateau en cours (exemple : 3 cases)
        self.current_ship_orientation = "horizontal"  # Orientation par défaut
        self.placed_ships = 0  # Nombre de bateaux placés

        # Grilles
        self.player_canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.player_canvas.grid(row=0, column=0, padx=10, pady=10)
        self.player_canvas.bind("<Button-1>", self.handle_click)

        self.opponent_canvas = tk.Canvas(self.root, width=400, height=400, bg="lightblue")
        self.opponent_canvas.grid(row=0, column=1, padx=10, pady=10)
        self.opponent_canvas.bind("<Button-1>", self.handle_click)

        # Bouton pour changer l'orientation
        self.orientation_button = tk.Button(self.root, text="Changer orientation", command=self.toggle_orientation)
        self.orientation_button.grid(row=1, column=0)

        self.status = tk.Label(self.root, text="Placez votre bateau de 3 cases")
        self.status.grid(row=2, column=0, columnspan=2)

        self.draw_grids()

    def toggle_orientation(self):
        """Change l'orientation actuelle du bateau."""
        if self.current_ship_orientation == "horizontal":
            self.current_ship_orientation = "vertical"
        else:
            self.current_ship_orientation = "horizontal"
        self.status.config(text=f"Orientation : {self.current_ship_orientation}")

    def draw_grids(self):
        """Dessine les grilles pour le joueur et l'adversaire."""
        for i in range(10):
            for j in range(10):
                # Grille joueur
                x0, y0 = j * 40, i * 40
                x1, y1 = x0 + 40, y0 + 40
                self.player_canvas.create_rectangle(x0, y0, x1, y1, outline="black")
                
                # Afficher les bateaux du joueur
                if any((i, j) in ship.positions for ship in self.game.player_board.ships):
                    self.player_canvas.create_rectangle(x0, y0, x1, y1, fill="gray")

                # Grille adversaire
                x0_op, y0_op = j * 40, i * 40
                x1_op, y1_op = x0_op + 40, y0_op + 40
                self.opponent_canvas.create_rectangle(x0_op, y0_op, x1_op, y1_op, outline="black")

    def handle_click(self, event):
        """Gère le clic sur une grille."""
        if self.placing_phase:
            self.place_ship(event)
        else:
            self.attack(event)

    def place_ship(self, event):
        """Place un bateau sur la grille du joueur."""
        x, y = event.y // 40, event.x // 40
        positions = []

        # Calcul des positions du bateau
        if self.current_ship_orientation == "horizontal":
            positions = [(x, y + i) for i in range(self.current_ship_size)]
        else:
            positions = [(x + i, y) for i in range(self.current_ship_size)]

        # Vérifier si le placement est valide
        if self.game.player_board.is_valid_placement(positions):
            self.game.player_board.place_ship_manually(positions)
            self.placed_ships += 1

            # Vérification si tous les bateaux sont placés
            if self.placed_ships == 2:  # Exemple : 2 bateaux à placer
                self.placing_phase = False
                self.status.config(text="Phase de jeu : À vous de tirer !")
                self.orientation_button.grid_remove()  # Supprime le bouton
            else:
                self.current_ship_size += 1  # Augmente la taille pour le prochain bateau
                self.status.config(text=f"Placez votre bateau de {self.current_ship_size} cases")

            self.draw_grids()
        else:
            self.status.config(text="Placement invalide ! Réessayez.")

    def attack(self, event):
        """Gère un tir sur la grille de l'adversaire."""
        if self.game.current_turn != "player":
            self.status.config(text="C'est au tour de l'adversaire !")
            return

        x, y = event.y // 40, event.x // 40
        result = self.game.take_turn(x, y)

        # Redessiner les grilles pour afficher les tirs
        self.update_grids()
        self.status.config(text=f"Résultat : {result}")

        # Vérifier si le jeu est terminé
        winner = self.game.check_victory()
        if winner:
            self.status.config(text=f"{winner} a gagné !")
            self.disable_grids()

    def update_grids(self):
        """Met à jour les grilles avec les tirs et les résultats."""
        for i in range(10):
            for j in range(10):
                # Grille du joueur
                if self.game.player_board.grid[i][j] == "X":  # Touché
                    self.player_canvas.create_rectangle(j * 40, i * 40, j * 40 + 40, i * 40 + 40, fill="red")
                elif self.game.player_board.grid[i][j] == "O":  # Manqué
                    self.player_canvas.create_oval(j * 40 + 10, i * 40 + 10, j * 40 + 30, i * 40 + 30, fill="blue")

                # Grille de l'adversaire
                if self.game.opponent_board.grid[i][j] == "X":  # Touché
                    self.opponent_canvas.create_rectangle(j * 40, i * 40, j * 40 + 40, i * 40 + 40, fill="red")
                elif self.game.opponent_board.grid[i][j] == "O":  # Manqué
                    self.opponent_canvas.create_oval(j * 40 + 10, i * 40 + 10, j * 40 + 30, i * 40 + 30, fill="blue")

    def disable_grids(self):
        """Désactive les clics sur les grilles."""
        self.player_canvas.unbind("<Button-1>")
        self.opponent_canvas.unbind("<Button-1>")

    def run(self):
        self.root.mainloop()
