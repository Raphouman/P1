from grid import SudokuGrid

class SudokuBoard:
    def __init__(self):
        self.grid = SudokuGrid.generate_grid()

    def is_valid_number(self, row, col, value):
        """Vérifie si une valeur peut être placée à (row, col)."""
        # Vérifie la ligne
        if value in self.grid[row]:
            return False

        # Vérifie la colonne
        if value in [self.grid[i][col] for i in range(9)]:
            return False

        # Vérifie le carré 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == value:
                    return False

        return True
