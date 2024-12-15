from board import SudokuBoard

class SudokuGame:
    def __init__(self):
        # Crée un plateau de Sudoku (avec une grille prédéfinie ou aléatoire)
        self.board = SudokuBoard()
        self.original_grid = self.board.grid  # Grille initiale immuable
        self.current_grid = [row[:] for row in self.board.grid]  # Grille modifiable

    def is_valid_move(self, row, col, value):
        """Vérifie si un mouvement est valide (respecte les règles du Sudoku)."""
        if self.original_grid[row][col] != 0:
            return False  # Case d'origine immuable
        return self.board.is_valid_number(row, col, value)

    def make_move(self, row, col, value):
        """Effectue un mouvement si valide."""
        if self.is_valid_move(row, col, value):
            self.current_grid[row][col] = value
            return True
        return False

    def is_completed(self):
        """Vérifie si la grille est correctement remplie."""
        for row in range(9):
            for col in range(9):
                if self.current_grid[row][col] == 0 or not self.is_valid_move(row, col, self.current_grid[row][col]):
                    return False
        return True
