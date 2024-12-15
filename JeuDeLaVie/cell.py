class Cell:
    def __init__(self, x: int, y: int, alive: bool = False):
        """
        Initialise une cellule avec sa position et son état.
        :param x: Position x de la cellule.
        :param y: Position y de la cellule.
        :param alive: État initial de la cellule (vivante ou morte).
        """
        self.x = x
        self.y = y
        self.alive = alive

    def set_alive(self, alive: bool):
        """Modifie l'état de la cellule."""
        self.alive = alive

    def is_alive(self) -> bool:
        """Retourne True si la cellule est vivante, sinon False."""
        return self.alive
