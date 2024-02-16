from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Loads image from path and returns its numpy array."""
    try:
        img = Image.open(path)
    except FileNotFoundError:
        return f"Error: The file '{path}' was not found."
    img_array = np.array(img)
    print(f"The shape of image is: {img_array.shape}")
    img.close()
    return img_array
