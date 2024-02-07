import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family,  list):
        raise ValueError("'family' argument must be a list.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("'start' and 'end' arguments must be integers.")
    if start < 0 or end > len(family):
        raise ValueError("Start and end indices must be within the bounds of" +
                         "the list.")
    np_array = np.array(family)
    print("My shape is :", np_array.shape)
    truncated_array = np_array[start:end]
    print("My new shape is :", truncated_array.shape)
    return truncated_array
