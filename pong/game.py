import random

class PongGame:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.ball = {"x": self.width // 2, "y": self.height // 2, "dx": 4, "dy": 4, "radius": 10}
        self.paddle1 = {"x": 20, "y": self.height // 2 - 50, "width": 10, "height": 100, "dy": 0}
        self.paddle2 = {"x": self.width - 30, "y": self.height // 2 - 50, "width": 10, "height": 100, "dy": 0}
        self.score1 = 0
        self.score2 = 0

    def update_ball(self):
        """Met à jour la position de la balle et gère les collisions."""
        ball = self.ball
        ball["x"] += ball["dx"]
        ball["y"] += ball["dy"]

        # Collision avec le haut et le bas
        if ball["y"] - ball["radius"] <= 0 or ball["y"] + ball["radius"] >= self.height:
            ball["dy"] *= -1

        # Collision avec les raquettes
        if (self.paddle1["x"] <= ball["x"] - ball["radius"] <= self.paddle1["x"] + self.paddle1["width"] and
                self.paddle1["y"] <= ball["y"] <= self.paddle1["y"] + self.paddle1["height"]):
            ball["dx"] *= -1

        if (self.paddle2["x"] <= ball["x"] + ball["radius"] <= self.paddle2["x"] + self.paddle2["width"] and
                self.paddle2["y"] <= ball["y"] <= self.paddle2["y"] + self.paddle2["height"]):
            ball["dx"] *= -1

        # Gérer les points
        if ball["x"] - ball["radius"] <= 0:  # Joueur 2 marque
            self.score2 += 1
            self.reset_ball()

        if ball["x"] + ball["radius"] >= self.width:  # Joueur 1 marque
            self.score1 += 1
            self.reset_ball()

    def reset_ball(self):
        """Réinitialise la balle au centre avec une direction aléatoire."""
        self.ball = {"x": self.width // 2, "y": self.height // 2, "radius": 10}

        # Direction aléatoire : -1 ou 1 pour dx et dy
        dx = random.choice([-4, 4])  # La balle ira à gauche ou à droite
        dy = random.choice([-3, 3])  # L'angle peut varier légèrement
        self.ball["dx"] = dx
        self.ball["dy"] = dy

    def move_paddles(self):
        """Déplace les raquettes selon leur direction actuelle."""
        self.paddle1["y"] += self.paddle1["dy"]
        self.paddle2["y"] += self.paddle2["dy"]

        # Empêche les raquettes de sortir du terrain
        self.paddle1["y"] = max(0, min(self.height - self.paddle1["height"], self.paddle1["y"]))
        self.paddle2["y"] = max(0, min(self.height - self.paddle2["height"], self.paddle2["y"]))
