from PIL import Image
import numpy as np


def ft_load(path: str, x: int, y: int, channel: int) -> np.array:
    try:
        img = Image.open(path)
    except FileNotFoundError:
        return "Error: The file '{path}' was not found."
    height, width = img.size
    if x > width or y > height:
        return "Error: x, y"
    print(f"New shape after slicing: ({x}, {y}, {channel}) or ({x}, {y})")
    img_array = np.array(img)
    img_array = img_array[:x, :y, :channel]
    img.close()
    return img_array
