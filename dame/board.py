from piece import Piece

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_pieces()

    def initialize_pieces(self):
        """Initialise les pièces sur le plateau."""
        for row in range(8):
            if row % 2 == 0:
                cols = range(1, 8, 2)
            else:
                cols = range(0, 8, 2)

            if row < 3:
                for col in cols:
                    self.grid[row][col] = Piece("black")
            elif row > 4:
                for col in cols:
                    self.grid[row][col] = Piece("red")

    def get_piece(self, row, col):
        """Retourne la pièce à une position donnée."""
        if 0 <= row < 8 and 0 <= col < 8:
            return self.grid[row][col]
        return None

    def move_piece(self, start, end):
        """
        Déplace une pièce sur le plateau.
        :param start: tuple (row, col) de la position de départ.
        :param end: tuple (row, col) de la position d'arrivée.
        :return: True si le mouvement est valide et effectué, sinon False.
        """
        start_row, start_col = start
        end_row, end_col = end
        piece = self.get_piece(start_row, start_col)

        # Vérifications de base
        if not piece:  # Pas de pièce à déplacer
            return False
        if self.get_piece(end_row, end_col):  # La case d'arrivée est occupée
            return False
        

        # Si c'est une reine
        if piece.is_queen:
            # Vérifier si le déplacement est valide pour une reine (diagonale libre)
            if self.is_valid_queen_move(start, end):
                # Si la case intermédiaire est occupée et qu'il s'agit d'une capture
                mid_row, mid_col = (start_row + end_row) // 2, (start_col + end_col) // 2
                captured_piece = self.get_piece(mid_row, mid_col)

                if captured_piece and captured_piece.color != piece.color:
                    self.grid[mid_row][mid_col] = None  # Enlever la pièce capturée

                self.grid[end_row][end_col] = piece
                self.grid[start_row][start_col] = None
                return True
            else:
                return False

        # Déplacement simple
        if abs(end_row - start_row) == 1 and abs(end_col - start_col) == 1:
            self.grid[end_row][end_col] = piece
            self.grid[start_row][start_col] = None
            self.check_promotion(end_row, piece)  # Vérifie la promotion
            return True

        # Capture
        if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            captured_piece = self.get_piece(mid_row, mid_col)
            if captured_piece and captured_piece.color != piece.color:
                # Effectuer la capture
                self.grid[end_row][end_col] = piece
                self.grid[start_row][start_col] = None
                self.grid[mid_row][mid_col] = None  # Retirer la pièce capturée
                self.check_promotion(end_row, piece)  # Vérifie la promotion
                return True

        return False  # Si aucune des conditions n'est respectée


    def check_promotion(self, row, piece):
        """Vérifie si une pièce doit être promue en reine."""
        if piece.color == "red" and row == 0:  # Les pions rouges atteignent la ligne 0
            piece.promote_to_queen()
        elif piece.color == "black" and row == len(self.grid) - 1:  # Les pions noirs atteignent la dernière ligne
            piece.promote_to_queen()



    def is_valid_queen_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end

        # Le déplacement doit être sur une diagonale
        if abs(end_row - start_row) != abs(end_col - start_col):
            return False

        # Vérifier si la trajectoire est libre
        step_row = 1 if end_row > start_row else -1
        step_col = 1 if end_col > start_col else -1
        current_row, current_col = start_row + step_row, start_col + step_col

        # Vérifier toutes les cases intermédiaires
        while (current_row != end_row) and (current_col != end_col):
            if self.get_piece(current_row, current_col):  # Si une pièce bloque la trajectoire
                return False
            current_row += step_row
            current_col += step_col

        return True




    def is_valid_move(self, start, end):
        """Vérifie si le déplacement est valide."""
        start_row, start_col = start
        end_row, end_col = end
        piece = self.get_piece(start_row, start_col)

        if not piece:
            return False

        # Vérifie que la case d'arrivée est vide
        if self.get_piece(end_row, end_col):
            return False

        # Vérifie la direction du déplacement
        direction = 1 if piece.color == "red" else -1
        if (end_row - start_row) == direction and abs(end_col - start_col) == 1:
            return True

        # Vérifie les sauts par-dessus une pièce adverse
        if (end_row - start_row) == 2 * direction and abs(end_col - start_col) == 2:
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            mid_piece = self.get_piece(mid_row, mid_col)
            if mid_piece and mid_piece.color != piece.color:
                self.grid[mid_row][mid_col] = None  # Retire la pièce sautée
                return True

        return False
