import tkinter as tk

class GuessingGraphics:
    """Interface graphique pour le jeu de devinette."""
    def __init__(self, root, game, ai):
        self.root = root
        self.game = game
        self.ai = ai

        self.root.title("Jeu de Devinette")
        self.root.geometry("400x300")

        self.message_label = tk.Label(root, text="Devinez un nombre entre 1 et 100", font=("Arial", 14))
        self.message_label.pack(pady=20)

        self.input_entry = tk.Entry(root, font=("Arial", 14))
        self.input_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Valider", font=("Arial", 14), command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Réinitialiser", font=("Arial", 14), command=self.reset_game)
        self.reset_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        self.ai_button = tk.Button(root, text="Lancer IA", font=("Arial", 14), command=self.ai_guess)
        self.ai_button.pack(pady=10)

    def check_guess(self):
        """Vérifie la supposition de l'utilisateur."""
        try:
            guess = int(self.input_entry.get())
            result = self.game.check_guess(guess)
            if result == "higher":
                self.result_label.config(text="Trop petit ! Essayez encore.")
            elif result == "lower":
                self.result_label.config(text="Trop grand ! Essayez encore.")
            elif result == "correct":
                self.result_label.config(text=f"Bravo ! Vous avez deviné en {self.game.get_attempts()} essais.")
        except ValueError:
            self.result_label.config(text="Veuillez entrer un nombre valide.")

    def ai_guess(self):
        """Lance l'IA pour deviner le nombre cible."""
        if self.ai.target is None:
            self.ai.set_target(self.game.target)

        guess = self.ai.make_guess()
        result = self.game.check_guess(guess)
        if result == "higher":
            self.ai.update_bounds("higher")
            self.result_label.config(text=f"L'IA dit : {guess}. Trop petit !")
        elif result == "lower":
            self.ai.update_bounds("lower")
            self.result_label.config(text=f"L'IA dit : {guess}. Trop grand !")
        elif result == "correct":
            self.result_label.config(text=f"L'IA a deviné : {guess} en {self.game.get_attempts()} essais.")

    def reset_game(self):
        """Réinitialise le jeu."""
        self.game.reset_game()
        self.ai.reset_game()
        self.result_label.config(text="")
        self.message_label.config(text="Devinez un nombre entre 1 et 100")
        self.input_entry.delete(0, tk.END)
