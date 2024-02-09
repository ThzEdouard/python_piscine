class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        dot = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print("Dot product is:", dot)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        add = [v1 + v2 for v1, v2 in zip(V1, V2)]
        print("Add Vector is :", add)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        add = [v1 - v2 for v1, v2 in zip(V1, V2)]
        print("Sous Vector is :", add)
