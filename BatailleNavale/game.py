from board import Board

class Game:
    def __init__(self):
        self.player_board = Board()
        self.opponent_board = Board()
        self.current_turn = "player"

    def place_ships_auto(self, player="opponent"):
        """Place les bateaux automatiquement pour un joueur."""
        board = self.player_board if player == "player" else self.opponent_board
        board.place_ships_automatically()

    def place_ships_manually(self, positions, player="player"):
        """Place un bateau manuellement sur la grille d'un joueur."""
        board = self.player_board if player == "player" else self.opponent_board
        return board.place_ship_manually(positions)

    def take_turn(self, x, y):
        """Effectue un tir sur la grille de l'adversaire."""
        print(f"Tour actuel avant le tir: {self.current_turn}")
        if self.current_turn == "player":
            result = self.opponent_board.receive_shot(x, y)
            self.current_turn = "opponent"
        else:
            result = self.player_board.receive_shot(x, y)
            self.current_turn = "player"

        # Debug : Vérification du changement de tour
        print(f"Changement de tour: {self.current_turn}")
        

        return result

    def get_random_shot(self):
        """Retourne une position aléatoire non encore attaquée."""
        available_shots = []
        for i in range(10):
            for j in range(10):
                if self.player_board.grid[i][j] not in ["X", "O"]:  # Pas déjà attaqué
                    available_shots.append((i, j))
        
        if available_shots:
            return random.choice(available_shots)
        return None

    def check_victory(self):
        """Vérifie si un joueur a gagné."""
        if all(ship.is_sunk() for ship in self.opponent_board.ships):
            return "player"
        if all(ship.is_sunk() for ship in self.player_board.ships):
            return "opponent"
        return None
