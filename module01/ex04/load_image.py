from PIL import Image
import numpy as np


def ft_load(path: str, x: int, y: int, channel: int) -> np.array:
    """Loads image from path, slices it based on given dimensions,
    and returns the resulting numpy array."""
    try:
        img = Image.open(path)
    except FileNotFoundError:
        return f"FileNotFoundError: The file '{path}' was not found."
    height, width = img.size
    if x > width or y > height:
        return "Error: x, y"
    img_array = np.array(img)
    img_array = img_array[:x, :y, :channel]
    print(f"New shape after slicing: {img_array.shape} or ({x}, {y})")
    print(img_array)
    img.close()
    return img_array
