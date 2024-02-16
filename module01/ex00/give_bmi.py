import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI from heights and weights."""
    if not all(isinstance(x, (int, float)) for x in height):
        if not all(isinstance(x, (int, float)) for x in weight):
            raise ValueError("list in not int or float")
    h_np = np.array(height)
    w_np = np.array(weight)
    bmis = (w_np / (h_np ** 2))
    return bmis.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply BMI limit and return boolean list."""
    ret = []
    for i, value in enumerate(bmi):
        if value < limit:
            ret.append(False)
        else:
            ret.append(True)
    return ret
