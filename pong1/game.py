from ball import Ball
from paddle import Paddle

class PongGame:
    def __init__(self):
        self.width = 800
        self.height = 600

        # Création des objets du jeu
        self.ball = Ball(self.width // 2, self.height // 2, radius=10, dx=4, dy=4)
        self.paddle1 = Paddle(20, self.height // 2 - 50, width=10, height=100)
        self.paddle2 = Paddle(self.width - 30, self.height // 2 - 50, width=10, height=100) #le -50 sert à centrer la raquette car la hauteur est de 100

        # Scores
        self.score1 = 0
        self.score2 = 0

    def update_ball(self):
        """Met à jour la position de la balle et gère les collisions."""
        self.ball.update_position(self.width, self.height)  #pas besoin de width d'ailleurs car limites du terrain dépendent de la hauteur seulement

        # Collision avec les raquettes
        if self.paddle1.collides_with(self.ball):
            self.ball.dx *= -1
        if self.paddle2.collides_with(self.ball):
            self.ball.dx *= -1

        # Points pour les joueurs
        if self.ball.x - self.ball.radius <= 0:  # Joueur 2 marque
            self.score2 += 1
            self.ball.reset(self.width // 2, self.height // 2)

        if self.ball.x + self.ball.radius >= self.width:  # Joueur 1 marque
            self.score1 += 1
            self.ball.reset(self.width // 2, self.height // 2)

    def move_paddles(self):
        """Déplace les raquettes."""
        self.paddle1.move(self.height)
        self.paddle2.move(self.height)
