import cv2
from numba_implementation import numba_color2gray
from python_implementation import python_color2gray

from numpy_implementation import numpy_color2gray


def grayscale_image(input_filename, output_filename=None, implementation = 'numpy', scale = 100):
    '''

       Args:
           input_filename: input filename/destination
           output_filename: output filename/destination

       Returns: grayscale image, and prints photo to desination if wanted

       '''
    if implementation == 'numpy':
        gray = numpy_color2gray(input_filename)
    elif implementation == 'numby':
        gray = numba_color2gray(input_filename)
    else:
        gray = python_color2gray(input_filename)
    if output_filename:
        filename_without_ending = output_filename.split(".")[0]
        cv2.imwrite(f"{filename_without_ending}_gray.jpeg", gray)
    return gray