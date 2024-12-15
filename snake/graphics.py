import tkinter as tk
from game import SnakeGame

class SnakeGraphics:
    CELL_SIZE = 20

    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.attributes("-fullscreen", True)  # Mode plein écran
        
        self.speed = 200  # Vitesse initiale en millisecondes
        self.game_started = False  # Contrôle si le jeu a commencé
        self.game = SnakeGame() # Instance du jeu

        # Canvas pour le jeu
        self.canvas = tk.Canvas(
            root, 
            width=self.game.board_width * self.CELL_SIZE, 
            height=self.game.board_height * self.CELL_SIZE, 
            bg="black"
        )
        self.canvas.pack()

        # Écran de démarrage
        self.start_screen = tk.Frame(root, bg="black")  # Fond noir
        self.start_screen.place(relwidth=1, relheight=1) # Remplit l'écran
        self.start_label = tk.Label(
            self.start_screen, 
            text="Snake Game", 
            font=("Arial", 48), 
            fg="green", 
            bg="black"
        )
        self.start_label.pack(pady=50)
        self.start_button = tk.Button(
            self.start_screen, 
            text="Start", 
            font=("Arial", 24), 
            command=self.start_game
        )
        self.start_button.pack(pady=20)

        # Bouton pour quitter le plein écran
        self.quit_button = tk.Button(
            root, 
            text="Quitter le plein écran", 
            command=self.exit_fullscreen
        )
        self.quit_button.pack()

        # Ajout d'un bouton pour réinitialiser
        self.reset_button = tk.Button(root, text="Réinitialiser", command=self.reset_game)
        self.reset_button.pack(pady=10)

        # Gestion des touches clavier
        self.root.bind("<KeyPress>", self.handle_keypress)
        self.update_canvas()

    def start_game(self):
        """Lance la partie après avoir cliqué sur 'Start'."""
        self.start_screen.destroy()  # Supprime l'écran de démarrage
        self.game_started = True
        self.run_game_loop()

    def update_canvas(self):
        """Redessine le plateau de jeu donc le serpent et la food."""
        self.canvas.delete("all")
        for x, y in self.game.snake:
            self.canvas.create_rectangle(
                x * self.CELL_SIZE, y * self.CELL_SIZE, 
                (x + 1) * self.CELL_SIZE, (y + 1) * self.CELL_SIZE, 
                fill="green"
            )
        food_x, food_y = self.game.food
        self.canvas.create_oval(
            food_x * self.CELL_SIZE, food_y * self.CELL_SIZE,
            (food_x + 1) * self.CELL_SIZE, (food_y + 1) * self.CELL_SIZE,
            fill="red"
        )

    def handle_keypress(self, event):
        """Gère les touches de direction."""
        key = event.keysym
        if key == "Up":
            self.game.change_direction((0, -1))
        elif key == "Down":
            self.game.change_direction((0, 1))
        elif key == "Left":
            self.game.change_direction((-1, 0))
        elif key == "Right":
            self.game.change_direction((1, 0))
        elif key == "Escape":
            self.exit_fullscreen()

    def run_game_loop(self):
        """Boucle principale du jeu."""
        if not self.game_started or self.game.game_over: # Arrête la boucle si le jeu n'a pas commencé ou est terminé
            return

        self.game.move_snake()
        self.update_canvas()

        if self.game.game_over:
            self.canvas.create_text(
                self.game.board_width * self.CELL_SIZE // 2,
                self.game.board_height * self.CELL_SIZE // 2,
                text=f"Game Over\nScore: {self.game.score}",
                fill="white",
                font=("Arial", 24)
            )
        else:
            # Accélère le jeu si de la nourriture a été mangée
            if self.game.score > 0:
                self.speed = self.speed - (self.game.score * 5)  # Réduit la vitesse par palier

            self.root.after(self.speed, self.run_game_loop) #plus on réduit la vitesse plus le jeu est rapide

    def reset_game(self):
        """Réinitialise le jeu."""
        self.speed = 200 # Réinitialise la vitesse
        self.game.reset_game()
        self.update_canvas()
        self.run_game_loop()

    def exit_fullscreen(self):
        """Sort du mode plein écran."""
        self.root.attributes("-fullscreen", False)
