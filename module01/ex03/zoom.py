from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_zoom(img_data: np.array, x: int, y: int, channel: int) -> np.array:
    height, width, _ = img_data.shape
    if x > width or y > height:
        return "Error: x, y"
    print(f"New shape after resizing: ({x}, {y}, 3)")
    img_cropped = img_data[:y, :x]
    plt.imshow(img_cropped[:, :, channel], cmap='gray')
    plt.show()
    return img_cropped


def main():
    img_data = ft_load("animal.jpeg")
    print(ft_zoom(img_data, 400, 400, 1))
    return


if __name__ == "__main__":
    main()
