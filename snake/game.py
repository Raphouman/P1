import random

class SnakeGame:
    def __init__(self, width=50, height=50):
        self.board_width = width
        self.board_height = height
        self.snake = [(width // 2, height // 2)]  # Position initiale du serpent
        self.snake_direction = (0, 1)  # Direction initiale : droite
        self.food = None
        self.score = 0
        self.game_over = False
        self.spawn_food()

    def spawn_food(self):
        """Place la nourriture à une position aléatoire."""
        self.food = (random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1))
        while self.food in self.snake:  # Évite que la nourriture apparaisse sur le serpent
            self.food = (random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1))

    def move_snake(self):
        """Déplace le serpent dans la direction actuelle."""
        if self.game_over:
            return

        head_x, head_y = self.snake[0]
        direction_x, direction_y = self.snake_direction
        new_head = (head_x + direction_x, head_y + direction_y)

        # Vérification des collisions
        if (new_head[0] < 0 or new_head[0] >= self.board_width or
            new_head[1] < 0 or new_head[1] >= self.board_height or
            new_head in self.snake):
            self.game_over = True
            return

        # Déplacement du serpent
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.spawn_food()  # Nouvelle nourriture
        else:
            self.snake.pop()  # Retire la queue du serpent

    def change_direction(self, new_direction):
        """Change la direction du serpent."""
        if (self.snake_direction[0] == -new_direction[0] and self.snake_direction[1] == -new_direction[1]): # Empêche le serpent de faire demi-tour
            return  # Ne fait rien si la nouvelle direction est opposée à la direction actuelle
        self.snake_direction = new_direction # Met à jour la direction du serpent donc si c'est sur les cotés

    def reset_game(self):
        """Réinitialise le jeu."""
        self.snake = [(self.board_width // 2, self.board_height // 2)]
        self.snake_direction = (0, 1)
        self.score = 0
        self.game_over = False
        self.spawn_food()