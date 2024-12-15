class Game:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Représentation du plateau (9 cases)
        self.current_player = "X"  # Le joueur X commence
        self.winner = None

    def make_move(self, position):
        """Effectue un mouvement pour le joueur actuel à la position donnée."""
        if self.board[position] == " " and not self.winner:
            self.board[position] = self.current_player
            if self.check_victory():
                self.winner = self.current_player
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_victory(self):
        """Vérifie si un joueur a gagné."""
        # Combinaisons gagnantes
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Lignes
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colonnes
            (0, 4, 8), (2, 4, 6)  # Diagonales
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def reset_game(self):
        """Réinitialise le jeu."""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.winner = None

    def get_board(self):
        """Retourne l'état actuel du plateau."""
        return self.board
