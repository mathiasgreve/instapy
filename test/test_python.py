from in3110_instapy.python_filters import python_color2gray, python_color2sepia
from PIL import Image
import in3110_instapy.io as my_io
import time

def test_color2gray(image):
    # run color2gray
    # ...
    # check that the result has the right shape, type
    # ...
    # assert uniform r,g,b values
    # ...
    return None


def test_color2sepia(image):
    # run color2sepia
    # ...
    # check that the result has the right shape, type
    # ...
    # verify some individual pixel samples
    # according to the sepia matrix

    result = python_color2sepia(my_io.read_image("test/rain.jpg"))

    my_io.write_image(result, "rain_sepia_python.jpg")

def test_python_color2gray(benchmark):

    # i = python_color2gray(my_io.read_image("test/rain.jpg"))
    result = benchmark(python_color2gray, my_io.read_image("test/rain.jpg"))

    my_io.write_image(result, "rain_grey_python.jpg")