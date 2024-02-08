from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    try:
        img = Image.open(path)
    except FileNotFoundError:
        return "Error: The file '{path}' was not found."
    h, w = img.size
    print(f"The shape of image is: ({w}, {h}, 3)")
    img_array = np.array(img)
    img.close()
    print(img_array)
    return img_array
