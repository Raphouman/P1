from ship import Ship

class Board:
    def __init__(self):
        self.grid = [["" for _ in range(10)] for _ in range(10)]  # Grille vide
        self.ships = []

    def place_ships_automatically(self):
        """Place des bateaux automatiquement sur la grille."""
        ship_sizes = [3, 4]  # Exemple : 2 bateaux, taille 3 et 4
        for size in ship_sizes:
            while True:
                ship = Ship.random(size)
                if self.place_ship_manually(ship.positions):
                    break

    def place_ship_manually(self, positions):
        """Place un bateau manuellement si les positions sont valides."""
        if self.is_valid_placement(positions):
            ship = Ship(positions)
            self.ships.append(ship)
            for x, y in positions:
                self.grid[x][y] = "S"  # "S" pour bateau
            return True
        return False

    def is_valid_placement(self, positions):
        """Vérifie si un placement de bateau est valide."""
        for x, y in positions:
            if not (0 <= x < 10 and 0 <= y < 10):  # En dehors de la grille
                return False
            if self.grid[x][y] == "S":  # Collision avec un autre bateau
                return False
        return True

    def receive_shot(self, x, y):
        """Reçoit un tir et met à jour la grille."""
        if self.grid[x][y] == "S":
            self.grid[x][y] = "X"  # "X" pour touché
            for ship in self.ships:
                if ship.hit(x, y):
                    return "Touché !" if not ship.is_sunk() else "Coulé !"
        elif self.grid[x][y] == "":
            self.grid[x][y] = "O"  # "O" pour manqué
            return "Manqué !"
        return "Déjà visé !"
