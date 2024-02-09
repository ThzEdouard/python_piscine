class calculator:
    """Your docstring for Class"""
    def __init__(self, numbers: list) -> None:
        """Your docstring for Constructor"""
        self.numbers = numbers

    def __add__(self, object) -> None:
        """Your docstring for add"""
        self.numbers = [number + object for number in self.numbers]
        print(self.numbers)

    def __mul__(self, object) -> None:
        """Your docstring for mul"""
        self.numbers = [number * object for number in self.numbers]
        print(self.numbers)

    def __sub__(self, object) -> None:
        """Your docstring for sub"""
        self.numbers = [number - object for number in self.numbers]
        print(self.numbers)

    def __truediv__(self, object) -> None:
        """Your docstring for div"""
        if object == 0:
            return None
        self.numbers = [number / object for number in self.numbers]
        print(self.numbers)
