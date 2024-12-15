import tkinter as tk
from game import PongGame


class PongGraphics:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong Game")
        self.game = PongGame()

        # Canvas pour afficher le jeu
        self.canvas = tk.Canvas(root, width=self.game.width, height=self.game.height, bg="black")
        self.canvas.pack()

        # Liens pour les touches
        self.root.bind("<KeyPress>", self.key_press)
        self.root.bind("<KeyRelease>", self.key_release)

        # Boucle du jeu
        self.run_game_loop()

    def run_game_loop(self):
        """Boucle principale du jeu."""
        self.game.update_ball()
        self.game.move_paddles()
        self.update_canvas()
        self.root.after(16, self.run_game_loop)  # Rafraîchissement à ~60 FPS

    def update_canvas(self):
        """Met à jour les éléments graphiques."""
        self.canvas.delete("all")

        # Dessiner la balle
        ball = self.game.ball
        self.canvas.create_oval(
            ball["x"] - ball["radius"], ball["y"] - ball["radius"],
            ball["x"] + ball["radius"], ball["y"] + ball["radius"],
            fill="white"
        )

        # Dessiner les raquettes
        paddle1 = self.game.paddle1
        paddle2 = self.game.paddle2
        self.canvas.create_rectangle(
            paddle1["x"], paddle1["y"],
            paddle1["x"] + paddle1["width"], paddle1["y"] + paddle1["height"],
            fill="white"
        )
        self.canvas.create_rectangle(
            paddle2["x"], paddle2["y"],
            paddle2["x"] + paddle2["width"], paddle2["y"] + paddle2["height"],
            fill="white"
        )

        # Dessiner le score
        self.canvas.create_text(
            self.game.width // 4, 20, text=str(self.game.score1), fill="white", font=("Arial", 24)
        )
        self.canvas.create_text(
            3 * self.game.width // 4, 20, text=str(self.game.score2), fill="white", font=("Arial", 24)
        )

    def key_press(self, event):
        """Gère les appuis sur les touches."""
        key = event.keysym
        if key == "z":
            self.game.paddle1["dy"] = -8
        elif key == "s":
            self.game.paddle1["dy"] = 8
        elif key == "Up":
            self.game.paddle2["dy"] = -8
        elif key == "Down":
            self.game.paddle2["dy"] = 8

    def key_release(self, event):
        """Gère les relâchements des touches."""
        key = event.keysym
        if key in ["z", "s"]:
            self.game.paddle1["dy"] = 0
        elif key in ["Up", "Down"]:
            self.game.paddle2["dy"] = 0
