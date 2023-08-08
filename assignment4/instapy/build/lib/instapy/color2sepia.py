import cv2
from numba_implementation import numba_color2sepia
from python_implementation import python_color2sepia

from numpy_implementation import numpy_color2sepia


def sepia_image(input_filename, output_filename=None, implementation = 'numpy', scale=100):
    '''

    Args:
        input_filename: input filename/destination
        output_filename: output filename/destination

    Returns: sepia image, and prints photo to desination if wanted

    '''
    if implementation == 'numpy':
        sep = numpy_color2sepia(input_filename)
    elif implementation == 'numby':
        sep = numba_color2sepia(input_filename)
    else:
        sep = python_color2sepia(input_filename)
    sep = cv2 . resize (sep , (0, 0) , fx =scale/100 , fy =scale/100)
    if output_filename:
        filename_without_ending = output_filename.split(".")[0]
        #Endret slik t
        cv2.imwrite(filename_without_ending+"_sepia.jpeg", sep)
    return sep
