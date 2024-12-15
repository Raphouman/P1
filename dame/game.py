from board import Board

class CheckersGame:
    def __init__(self):
        self.board = Board()
        self.selected_piece = None
        self.turn = "red"  # Le joueur rouge commence

    def select_piece(self, row, col):
        """Sélectionne une pièce ou déplace une pièce sélectionnée."""
        piece = self.board.get_piece(row, col)

        # Sélection d'une nouvelle pièce
        if piece and piece.color == self.turn:
            self.selected_piece = (row, col)
            return True  # Sélection réussie

        # Déplacement d'une pièce sélectionnée
        elif self.selected_piece:
            start_pos = self.selected_piece
            if self.board.move_piece(start_pos, (row, col)):
                self.end_turn()  # Passer au tour suivant si le déplacement est valide
                self.selected_piece = None
                return True  # Déplacement réussi
            else:
                self.selected_piece = None  # Réinitialiser si le déplacement est invalide

        return False  # Si aucune action valide n'a été effectuée



    def end_turn(self):
        """Passe au tour du joueur suivant."""
        self.turn = "black" if self.turn == "red" else "red"
