from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Your docstring for Class"""
    def __init__(self, first_name: str):
        super().__init__(first_name)

    def set_eyes(self, eyes: str) -> None:
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        self.hairs = hairs

    def get_eyes(self) -> str:
        return self.eyes

    def get_hairs(self) -> str:
        return self.hairs
