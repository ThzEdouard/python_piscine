from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name: str, is_alive: bool = True,
                 __name__: str = "Baratheon", eyes: str = "brown",
                 hairs: str = "dark") -> None:
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = __name__
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return f"Vector : ('{type(self).__name__}', '{self.eyes}', " \
            f"'{self.hairs}')"

    def __repr__(self):
        return f"Vector : ('{type(self).__name__}', '{self.eyes}', " \
            f"'{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name: str, is_alive: bool = True,
                 __name__: str = "Lannister", eyes: str = "blue",
                 hairs: str = "light") -> None:
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = __name__
        self.eyes = eyes
        self.hairs = hairs

    @classmethod
    def create_lannister(self, first_name: str, is_alive: bool = True):
        """Your docstring for method"""
        return self(first_name, is_alive)

    def __str__(self):
        return f" : ('{type(self).__name__}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector : ('{type(self).__name__}', '{self.eyes}', "\
            f"'{self.hairs}')"
