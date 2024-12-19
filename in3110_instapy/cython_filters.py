# """Cython implementation of filter functions"""
# from __future__ import annotations

# import cython as C
# import numpy as np

# if not C.compiled:
#     raise ImportError(
#         "Cython module not compiled! Check setup.py and make sure this package has been installed, not just imported in-place, e.g. `pip install --editable .`."
#     )

# from cython.cimports.libc.stdint import uint8_t  # noqa

# # we may need a 'const uint8_t' type to make sure we accept 'read-only' arrays
# const_uint8_t = C.typedef("const uint8_t")
# float64_t = C.typedef(C.double)


# def cython_color2gray(image):
#     """Convert rgb pixel array to grayscale

#     Args:
#         image (np.array)
#     Returns:
#         np.array: gray_image
#     """
    
#     cdef int height = image.shape[0]
#     cdef int width = image.shape[1]
    
#     # Allocate memory for the grayscale image
#     cdef np.ndarray[np.uint8_t, ndim=2] gray_image = np.empty((height, width), dtype=np.uint8)
    
#     # Declare variables to store the RGB values
#     cdef int red, green, blue
#     cdef double gray_value
#     cdef int x, y
    
#     # Iterate through the image and calculate the grayscale values
#     for x in range(height):
#         for y in range(width):
#             red = image[x, y, 0]
#             green = image[x, y, 1]
#             blue = image[x, y, 2]
            
#             # Calculate grayscale using the weighted sum
#             gray_value = 0.21 * red + 0.72 * green + 0.07 * blue
            
#             # Assign the grayscale value to the output image
#             gray_image[x, y] = <uint8_t>gray_value  # Cast to uint8_t to ensure it fits in the range
    
#     return gray_image

# def cython_color2sepia(image):
#     """Convert rgb pixel array to sepia

#     Args:
#         image (np.array)
#     Returns:
#         np.array: gray_image
#     """
#     ...
