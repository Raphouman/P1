from cell import Cell

class Game:
    def __init__(self, rows: int, cols: int):
        """
        Initialise le jeu avec une grille de dimensions spécifiées.
        :param rows: Nombre de lignes.
        :param cols: Nombre de colonnes.
        """
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(x, y) for y in range(cols)] for x in range(rows)]    # Créer une grille de cellules de x lignes et y colonnes

    def get_neighbors(self, cell: Cell) -> list[Cell]:  # Renvoie une liste de cellules voisines
        """Retourne la liste des cellules voisines d'une cellule donnée."""
        neighbors = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # Les 8 directions possibles (Nord, Sud, Est, Ouest et les diagonales) chaque tuple représente un déplacement de  dx et dy
        for dx, dy in directions:   # Parcourir les 8 directions
            nx, ny = cell.x + dx, cell.y + dy  # Calculer la position du voisin
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                neighbors.append(self.grid[nx][ny])
        return neighbors

    def update(self):
        """Applique une génération du Jeu de la vie."""
        new_grid = [[cell.is_alive() for cell in row] for row in self.grid] # Créer une nouvelle grille avec les mêmes valeurs que la grille actuelle donc de x lignes et y colonnes 

        for row in self.grid:
            for cell in row:
                alive_neighbors = sum(1 for neighbor in self.get_neighbors(cell) if neighbor.is_alive()) # Compter le nombre de voisins vivants
                if cell.is_alive():
                    # Meurt si elle a moins de 2 ou plus de 3 voisins vivants ou plutot reste en vie si elle a 2 ou 3 voisins vivants
                    new_grid[cell.x][cell.y] = alive_neighbors in (2, 3)
                else:
                    # Naît si elle a exactement 3 voisins vivants
                    new_grid[cell.x][cell.y] = alive_neighbors == 3

        # Appliquer les nouvelles valeurs
        for x in range(self.rows):
            for y in range(self.cols):
                self.grid[x][y].set_alive(new_grid[x][y]) # Mettre à jour l'état de chaque cellule, donc la grille actuelle
    def toggle_cell(self, x: int, y: int):
        """Change l'état d'une cellule (vivante/morte)."""
        if 0 <= x < self.rows and 0 <= y < self.cols:
            cell = self.grid[x][y]                      # Récupérer la cellule à la position à la ligne x et colonne y
            cell.set_alive(not cell.is_alive())     # Inverser l'état de la cellule en cliquant dessus (handle_click)
