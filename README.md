# Instapy

Instapy is an image converter that convertes your JPEG to a greyscale or sepia version.

It is a python package with a provided command line interface.

## Setting Up the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/mathiasgreve/instapy.git

2. Navigate to the project directory and create a virtual environment:
   ```bash
   cd instapy
   python3 -m venv venv

3. Activate the virtual environment:
- macOS/Linux:
  ```bash
  source venv/bin/activate

4. Install the dependencies:
    ```bash
    python3 -m pip install .
    ```

## Use functionality

After successfull installation the functionality can be utilized be importing the package and relevant modules.

Example program, converting 'img_file.jpg' to grey version using python implementation:
```python
from in3110_instapy import get_filter
from in3110_instapy.io import  read_image, write_image

filter = get_filter()                        # without input - grey filter with python implementation
img = read_image('img_file.jpg')             # read_image() takes the path to a .jpg file as input
filtered = filter(img)     

write_image(filtered, 'filtered_name.jpg')   # second input to write_image() is the path to the new filtered image
```

## Use command line interface

After successfull installation the functionality can also be accessed through the command line interface that is provided:

   ```bash
   instapy <file to convert> <arguments>
   ```

Here are the arguments: 
   ```bash
     -o, --out             The output filename
     -g, --gray            Select gray filter
     -se, --sepia          Select sepia filter
     -sc, --scale
                           Scale factor to resize image
     -i {python,numba,numpy,cython}, --implementation {python,numba,numpy,cython}
                           The implementation
   ```
(NB! cython is NOT implemented yet!!)
