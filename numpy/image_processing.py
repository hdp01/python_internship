import numpy as np
from PIL import Image

def load_image(path):
    """Load an image from a file and convert it to a NumPy array."""
    with Image.open(path) as img:
        return np.array(img)

def save_image(path, array):
    """Save a NumPy array as an image to a file."""
    img = Image.fromarray(array)
    img.save(path)

def invert_image(array):
    """Invert the colors of an image represented as a NumPy array."""
    return 255 - array

def resize_image(array, new_size):
    """Resize an image represented as a NumPy array to a new size."""
    img = Image.fromarray(array)
    resized_img = img.resize(new_size)
    return np.array(resized_img)

def grayscale_image(array):
    """Convert an image represented as a NumPy array to grayscale."""
    grayscale_array = np.zeros_like(array)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            r, g, b = np.minimum(array[i, j], 2255)
            grayscale_array[i, j] = (r + g + b) // 3
    return grayscale_array