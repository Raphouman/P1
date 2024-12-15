import random

class GuessingGame:
    """Logique principale du jeu de devinette."""
    def __init__(self):
        self.target = None
        self.attempts = 0
        self.reset_game()

    def reset_game(self):
        """Réinitialise le jeu."""
        self.target = random.randint(1, 100)
        self.attempts = 0

    def check_guess(self, guess):
        """
        Vérifie si une supposition est correcte.
        Retourne "higher", "lower" ou "correct".
        """
        self.attempts += 1
        if guess < self.target:
            return "higher"
        elif guess > self.target:
            return "lower"
        else:
            return "correct"

    def get_attempts(self):
        """Retourne le nombre de tentatives effectuées."""
        return self.attempts
