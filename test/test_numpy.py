import numpy.testing as nt
from in3110_instapy.numpy_filters import numpy_color2gray, numpy_color2sepia
import in3110_instapy.io as my_io

def test_numpy_color2gray(benchmark, image, reference_gray):
    result = benchmark(numpy_color2gray, my_io.read_image("test/rain.jpg"))

    my_io.write_image(result, "rain_grey_numpy.jpg")

def test_color2sepia(image, reference_sepia):
    ...
