import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.array:
    """Inverts the color of the image received and returns
    the resulting numpy array."""
    array = np.invert(array)
    plt.imshow(array, cmap='gray')
    plt.show()
    return array


def ft_red(array) -> np.array:
    """Extracts red channel from the image and returns
    the resulting numpy array."""
    array_red = array.copy()
    array_red[:, :, 1] = 0
    array_red[:, :, 2] = 0
    plt.imshow(array_red, cmap='gray')
    plt.show()
    return array_red


def ft_green(array) -> np.array:
    """Extracts green channel from the image and returns
    the resulting numpy array."""
    array_green = array.copy()
    array_green[:, :, 0] = 0
    array_green[:, :, 2] = 0
    plt.imshow(array_green, cmap='gray')
    plt.show()
    return array_green


def ft_blue(array) -> np.array:
    """Extracts blue channel from the image and returns
    the resulting numpy array."""
    array_blue = array.copy()
    array_blue[:, :, 0] = 0
    array_blue[:, :, 1] = 0
    plt.imshow(array_blue, cmap='gray')
    plt.show()
    return array_blue


def ft_grey(array) -> np.array:
    """Converts the image to grayscale and returns
    the resulting numpy array."""
    array_grey = array.copy()
    array_grey = np.mean(array_grey, axis=2)
    plt.imshow(array_grey, cmap='gray')
    plt.show()
    return array_grey
