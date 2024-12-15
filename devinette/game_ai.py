
class GuessingAI:
    """Une IA simple pour jouer au jeu de devinette."""
    def __init__(self, lower_bound=1, upper_bound=100):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.target = None
        self.current_guess = None

    def reset_game(self):
        """Réinitialise les bornes et sélectionne une nouvelle cible."""
        self.target = None
        self.lower_bound = 1
        self.upper_bound = 100

    def set_target(self, number):
        """Définit le nombre que l'IA doit deviner."""
        self.target = number

    def make_guess(self):
        """Effectue une supposition basée sur les bornes actuelles."""
        if self.target is None:
            raise ValueError("Le nombre cible n'est pas défini.")
        self.current_guess = (self.lower_bound + self.upper_bound) // 2
        return self.current_guess

    def update_bounds(self, hint):
        """Met à jour les bornes en fonction du retour de l'utilisateur."""
        if hint == "higher":
            self.lower_bound = self.current_guess + 1
        elif hint == "lower":
            self.upper_bound = self.current_guess - 1
        else:
            raise ValueError("Indice invalide : choisissez 'higher' ou 'lower'.")
