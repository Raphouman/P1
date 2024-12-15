class Game:
    def __init__(self):
        # Plateau de jeu : 6 lignes x 7 colonnes
        self.board = [[" " for _ in range(7)] for _ in range(6)]
        self.current_player = "Joueur 1"  # Le joueur X commence
        self.winner = None

    def make_move(self, column):
        """Effectue un mouvement pour le joueur actuel dans la colonne donnée."""
        if self.winner:
            return False  # Le jeu est terminé

        for row in reversed(range(6)):  # On commence par la dernière ligne
            if self.board[row][column] == " ":
                self.board[row][column] = self.current_player
                if self.check_victory(row, column):
                    self.winner = self.current_player
                else:
                    self.current_player = "Joueur 2" if self.current_player == "Joueur 1" else "Joueur 1"
                return True
        return False  # La colonne est pleine

    def check_victory(self, row, column): # fonction de win mais logique
        """Vérifie si le joueur actuel a gagné après avoir placé un jeton à (row, column)."""
        directions = [
            [(0, 1), (0, -1)],  # Horizontal , (0,1) vers la droite et (0,-1) vers la gauche
            [(1, 0), (-1, 0)],  # Vertical , (1,0) vers le bas et (-1,0) vers le haut
            [(1, 1), (-1, -1)],  # Diagonale principale , (1,1) vers le bas droite et (-1,-1) vers le haut gauche
            [(1, -1), (-1, 1)],  # Diagonale secondaire , (1,-1) vers le bas gauche et (-1,1) vers le haut droite
        ]

        for direction in directions:
            count = 1  # Le jeton actuel
            for dr, dc in direction:
                r, c = row + dr, column + dc # On commence à partir de la case adjacente
                while 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == self.current_player: # Tant que la case est dans le plateau et contient le jeton actuel
                    count += 1 
                    r, c = r + dr, c + dc # On continue dans la même direction
            if count >= 4: # Si on a trouvé 4 jetons alignés
                return True
        return False

    def get_board(self):
        """Retourne l'état actuel du plateau."""
        return self.board

    def reset_game(self):
        """Réinitialise le jeu."""
        self.board = [[" " for _ in range(7)] for _ in range(6)] # Réinitialise le plateau (6 lignes x 7 colonnes)
        self.current_player = "Joueur 1"
        self.winner = None
