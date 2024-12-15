import random
from cell import Cell

class MinesweeperGame:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.grid = self.create_grid()
        self.place_mines()
        self.calculate_adjacent_mines()
        self.game_over = False
        self.cells_revealed = 0

    def create_grid(self):
        """Crée une grille initialisée avec des cellules vides."""
        return [[Cell(row, col) for col in range(self.cols)] for row in range(self.rows)]

    def place_mines(self):
        """Place des mines aléatoirement dans la grille."""
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)
        for pos in mine_positions:
            row, col = divmod(pos, self.cols)
            self.grid[row][col].is_mine = True

    def calculate_adjacent_mines(self):
        """Calcule le nombre de mines adjacentes pour chaque cellule."""
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.grid[row][col].is_mine:
                    count = 0
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c].is_mine:
                            count += 1
                    self.grid[row][col].adjacent_mines = count

    def reveal_cell(self, row, col):
        """Révèle une cellule. Si la cellule est vide, révèle les cellules adjacentes."""
        if self.game_over or self.grid[row][col].is_revealed:
            return
        
        cell = self.grid[row][col]
        cell.is_revealed = True
        self.cells_revealed += 1

        if cell.is_mine:
            self.game_over = True
        elif cell.adjacent_mines == 0:
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    self.reveal_cell(r, c)

    def toggle_flag(self, row, col):
        """Ajoute ou enlève un drapeau sur une cellule."""
        cell = self.grid[row][col]
        if not cell.is_revealed:
            cell.is_flagged = not cell.is_flagged

    def check_win(self):
        """Vérifie si le joueur a gagné."""
        return self.cells_revealed == self.rows * self.cols - self.mines