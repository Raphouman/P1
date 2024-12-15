import tkinter as tk
from game import Game

class Graphics:
    def __init__(self, rows: int, cols: int, cell_size: int = 20):
        """
        Initialise l'interface graphique.
        :param rows: Nombre de lignes.
        :param cols: Nombre de colonnes.
        :param cell_size: Taille d'une cellule en pixels.
        """
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.game = Game(rows, cols)

        self.root = tk.Tk()
        self.root.title("Jeu de la Vie")
        self.canvas = tk.Canvas(self.root, width=cols * cell_size, height=rows * cell_size, bg="white")
        self.canvas.pack()

        self.running = False
        self.canvas.bind("<Button-1>", self.handle_click)   # Lier le clic gauche de la souris à la méthode handle_click
        self.create_buttons()

    def create_buttons(self):
        """Crée les boutons Start, Stop et Reset."""
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()
        tk.Button(btn_frame, text="Start", command=self.start_game).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Stop", command=self.stop_game).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Reset", command=self.reset_game).pack(side=tk.LEFT)

    def handle_click(self, event):
        """Gère le clic pour activer/désactiver une cellule."""
        x, y = event.y // self.cell_size, event.x // self.cell_size  # Inversion x et y pour correspondre à la grille car le click est en (y, x) et diviser par la taille de la cellule pour obtenir la position dans la grille (quelle ligne et quelle colonne)
        self.game.toggle_cell(x, y) # change l'état de la cellule graphiquement
        self.draw_grid()   

    def draw_grid(self):
        """Dessine la grille avec l'état actuel des cellules."""
        self.canvas.delete("all")
        for row in self.game.grid:
            for cell in row:
                x0 = cell.y * self.cell_size       # x0 et y0 sont les coordonnées du coin supérieur gauche de la cellule
                y0 = cell.x * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                color = "black" if cell.is_alive() else "white"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="gray")    # Dessiner un rectangle pour chaque cellule de contour gris

    def update(self):
        """Met à jour l'affichage et la logique du jeu."""
        if self.running:
            self.game.update()  # Appliquer une génération du Jeu de la vie
            self.draw_grid()    # Mettre à jour l'affichage représentant la grille après la génération
            self.root.after(300, self.update)   # Appeler la méthode update après 300ms pour pas que ça aille trop vite

    def start_game(self):
        """Démarre le jeu."""
        self.running = True
        self.update()

    def stop_game(self):
        """Stoppe le jeu."""
        self.running = False

    def reset_game(self):
        """Réinitialise le jeu."""
        self.game = Game(self.rows, self.cols)
        self.draw_grid()

    def run(self):
        """Lance la boucle principale."""
        self.draw_grid()
        self.root.mainloop()    # Lancer la boucle principale de l'interface graphique ce qui lance la fenêtre
