import numpy.testing as nt
from in3110_instapy.numba_filters import numba_color2gray, numba_color2sepia
import in3110_instapy.io as my_io
import time

def test_numba_color2gray(benchmark, image, reference_gray):
    # Benchmark the numba_color2gray function
    result = benchmark(numba_color2gray, my_io.read_image("test/rain.jpg"))

    # Optionally, save the result to a file
    my_io.write_image(result, "rain_grey_numba.jpg")

def test_color2sepia(image, reference_sepia):
    ...
