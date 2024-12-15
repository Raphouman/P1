class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0

    def move(self, height):
        """Déplace la raquette en fonction de dy, sans sortir du terrain."""
        self.y += self.dy
        self.y = max(0, min(height - self.height, self.y)) # max prend le plus grand des deux arguments, min prend le plus petit donc min sert à ne pas dépasser le bas du terrain et max à ne pas dépasser le haut

    def collides_with(self, ball):  
        """Vérifie si la balle touche la raquette."""
        return (self.x <= ball.x <= self.x + self.width and
                self.y <= ball.y <= self.y + self.height)
