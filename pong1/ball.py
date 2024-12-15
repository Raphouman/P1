import random

class Ball:
    def __init__(self, x, y, radius, dx, dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = dx
        self.dy = dy

    def update_position(self, width, height):
        """Met à jour la position de la balle et gère les collisions avec les murs."""
        self.x += self.dx
        self.y += self.dy

        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.dy *= -1

    def reset(self, x, y):
        """Réinitialise la balle avec une direction aléatoire."""
        self.x = x
        self.y = y
        self.dx = random.choice([-4, 4])
        self.dy = random.choice([-3, 3])
