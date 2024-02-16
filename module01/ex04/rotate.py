from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_rotate(img_data: np.array) -> np.array:
    """Rotates image data and returns the resulting numpy array."""
    x, y, _ = img_data.shape
    print(f"New shape after Transpose: ({x}, {y})")
    plt.imshow(np.swapaxes(img_data, 0, 1), cmap="gray")
    plt.show()
    return np.array(img_data)[:, :, 0]


def main():
    """Main function."""
    try:
        img_array = ft_load("animal.jpeg", 400, 400, 1)
        if not isinstance(img_array, np.ndarray):
            raise FileNotFoundError(img_array)
        print(ft_rotate(img_array))
    except FileNotFoundError as msg:
        print(msg)
    return


if __name__ == "__main__":
    main()
