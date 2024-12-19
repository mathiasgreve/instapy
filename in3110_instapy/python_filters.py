"""pure Python implementation of image filters"""
from __future__ import annotations

import numpy as np
from PIL import Image

def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    # Get the dimensions of the input image
    height, width, _ = image.shape

    # Create an empty array for the grayscale image
    # gray_image = np.empty((height, width), dtype="uint8")
    gray_image = np.empty_like(image)

    # Iterate through each pixel and apply the grayscale formula
    for i in range(height):
        for j in range(width):
            # get the RGB values
            red = image[i, j, 0]
            green = image[i, j, 1]
            blue = image[i, j, 2]
            
            # Apply the grayscale transformation
            gray_value = 0.21 * red + 0.72 * green + 0.07 * blue
            
            # Store the computed grayscale value in the new array
            gray_image[i, j] = gray_value

    # print(gray_image.shape)
    # for val in gray_image[10,20,:]:
    #     print(val)

    return gray_image.astype("uint8")


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ]
    
    sepia_image = np.empty_like(image)
    # Iterate through the pixels
    # applying the sepia matrix

    # Get the dimensions of the input image
    height, width, _ = image.shape

    # Iterate through each pixel and apply the sepia formula
    for i in range(height):
        for j in range(width):

            # get the RGB values
            red = image[i, j, 0]
            green = image[i, j, 1]
            blue = image[i, j, 2]
            
            # Apply the sepia transformation
            sepia_red = min(255, sepia_matrix[0][0] * red + sepia_matrix[0][1] * green + sepia_matrix[0][2] * blue)
            sepia_green = min(255, sepia_matrix[1][0] * red + sepia_matrix[1][1] * green + sepia_matrix[1][2] * blue)
            sepia_blue = min(255, sepia_matrix[2][0] * red + sepia_matrix[2][1] * green + sepia_matrix[2][2] * blue)
            
            sepia_image[i, j, 0] = sepia_red
            sepia_image[i, j, 1] = sepia_green
            sepia_image[i, j, 2] = sepia_blue

    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image.astype("uint8")
