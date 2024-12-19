"""Command-line (script) interface to instapy"""
from __future__ import annotations

import argparse
import sys

import in3110_instapy
import in3110_instapy.python_filters
import numpy as np
from PIL import Image

from . import io

from .python_filters import python_color2gray, python_color2sepia
from .numpy_filters import numpy_color2gray, numpy_color2sepia
from .numba_filters import numba_color2gray, numba_color2sepia
# from .cython_filters import cython_color2gray, cython_color2sepia

def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = io.read_image(file)
    if scale != 1:
        # Resize image, if needed
        print("scale: {scale}")

    # Apply the filter
    
    # Apply the selected filter and implementation
    if filter == "color2gray":
        if implementation == "python":
            filtered = python_color2gray(image)
        elif implementation == "numpy":
            filtered = numpy_color2gray(image)
        elif implementation == "numba":
            filtered = numba_color2gray(image)
        # elif implementation == "cython":
        #     filtered = cython_color2gray(image)
        else:
            raise ValueError(f"Unknown implementation: {implementation}")
    elif filter == "color2sepia":
        if implementation == "python":
            filtered = python_color2sepia(image)
        elif implementation == "numpy":
            filtered = numpy_color2sepia(image)
        elif implementation == "numba":
            filtered = numba_color2sepia(image)
        # elif implementation == "cython":
        #     filtered = cython_color2sepia(image)
        else:
            raise ValueError(f"Unknown implementation: {implementation}")
    else:
        raise ValueError(f"Unknown filter: {filter}")
    
    
    if out_file:
        
        # save the file
        io.write_image(filtered, out_file)
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description="Apply filters to an image.")

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")

    # Optional arguments
    parser.add_argument("-o", "--out", help="The output filename")
    parser.add_argument("-g", "--gray", action="store_true", help="Select gray filter")
    parser.add_argument("-se", "--sepia", action="store_true", help="Select sepia filter")
    parser.add_argument("-sc", "--scale", type=float, default=1.0, help="Scale factor to resize image")
    parser.add_argument("-i", "--implementation", choices=["python", "numpy", "numba"], default="python", help="The implementation to use") # NB can be expanded with cython

    # Parse arguments
    args = parser.parse_args()

    # Determine filter type
    if args.gray:
        filter_type = "color2gray"
    elif args.sepia:
        filter_type = "color2sepia"
    else:
        parser.error("No filter selected, add either --gray or --sepia.")

    # Run the filter with parsed arguments
    run_filter(
        file=args.file,
        out_file=args.out,
        implementation=args.implementation,
        filter=filter_type,
        # scale=args.scale, # scale not implemented yet
    )
