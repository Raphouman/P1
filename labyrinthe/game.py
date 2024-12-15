import random

class MazeGame:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.maze = []
        self.player_position = (0, 0)
        self.exit_position = (width - 1, height - 1)
        self.generate_maze()
        self.reset_game()

    def generate_maze(self):
        """Génère un labyrinthe avec un chemin garanti entre le départ et la sortie."""
        # Initialise le labyrinthe avec uniquement des murs
        self.maze = [[1 for _ in range(self.width)] for _ in range(self.height)]

        # Création d'un chemin avec un DFS pour garantir un chemin existant
        stack = [(0, 0)]
        visited = set()
        visited.add((0, 0))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Droite, Bas, Gauche, Haut

        while stack:
            current = stack[-1]
            x, y = current
            self.maze[x][y] = 0  # Marquer le chemin comme libre
            neighbors = []

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.height and 0 <= ny < self.width and (nx, ny) not in visited:
                    # Vérifie si on ne casse pas trop de murs autour
                    walls = 0
                    for ddx, ddy in directions:
                        wx, wy = nx + ddx, ny + ddy
                        if 0 <= wx < self.height and 0 <= wy < self.width and self.maze[wx][wy] == 0:
                            walls += 1
                    if walls < 2:  # Évite les intersections inutiles
                        neighbors.append((nx, ny))

            if neighbors:
                next_cell = random.choice(neighbors)
                stack.append(next_cell)
                visited.add(next_cell)
            else:
                stack.pop()

        # Assurez-vous que la sortie est dégagée
        self.maze[self.exit_position[0]][self.exit_position[1]] = 0

    def reset_game(self):
        """Réinitialise la position du joueur."""
        self.generate_maze()
        self.player_position = (0, 0)

    def move_player(self, direction):
        """Déplace le joueur si possible."""
        x, y = self.player_position
        if direction == "up" and x > 0 and self.maze[x - 1][y] == 0:
            self.player_position = (x - 1, y)
        elif direction == "down" and x < self.height - 1 and self.maze[x + 1][y] == 0:
            self.player_position = (x + 1, y)
        elif direction == "left" and y > 0 and self.maze[x][y - 1] == 0:
            self.player_position = (x, y - 1)
        elif direction == "right" and y < self.width - 1 and self.maze[x][y + 1] == 0:
            self.player_position = (x, y + 1)

    def is_game_over(self):
        """Vérifie si le joueur a atteint la sortie."""
        return self.player_position == self.exit_position
