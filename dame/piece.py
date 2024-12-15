class Piece:
    def __init__(self, color):
        self.color = color
        self.is_queen = False

    def promote_to_queen(self):
            """Promouvoir un pion en reine."""
            self.is_queen = True