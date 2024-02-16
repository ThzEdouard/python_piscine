from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_zoom(img_data: np.array, x: int, y: int, channel: int) -> np.array:
    """Zooms into image data based on given dimensions and returns
    the resulting numpy array."""
    height, width, _ = img_data.shape
    if x > width or y > height:
        return "Error: x, y"
    img_cropped = img_data[:x, :y, :channel]
    print(f"New shape after slicing: {img_cropped.shape} or ({x}, {y})")
    plt.imshow(img_cropped, cmap='gray')
    plt.show()
    return img_cropped[:]


def main():
    """Main function."""
    try:
        img_data = ft_load("animal.jpeg")
        if not isinstance(img_data, np.ndarray):
            raise FileNotFoundError(img_data)
        print(ft_zoom(img_data, 400, 400, 1))
    except FileNotFoundError as msg:
        print(msg)
    return


if __name__ == "__main__":
    main()
