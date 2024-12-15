import random

class Ship:
    def __init__(self, positions):
        self.positions = positions  # Liste de tuples (x, y)
        self.hits = set()

    def hit(self, x, y):
        """Enregistre un tir sur le bateau."""
        if (x, y) in self.positions:
            self.hits.add((x, y))
            return True
        return False

    def is_sunk(self):
        """Vérifie si le bateau est coulé."""
        return set(self.positions) == self.hits

    @staticmethod
    def random(size):
        """Génère un bateau aléatoire."""
        orientation = random.choice(["horizontal", "vertical"])
        if orientation == "horizontal":
            x = random.randint(0, 9)
            y = random.randint(0, 10 - size)
            positions = [(x, y + i) for i in range(size)]
        else:
            x = random.randint(0, 10 - size)
            y = random.randint(0, 9)
            positions = [(x + i, y) for i in range(size)]
        return Ship(positions)
