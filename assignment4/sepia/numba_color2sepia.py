import timeit
import cv2
import numpy as np
from numba import jit

from python_color2sepia import python_color2sepia
from numpy_color2sepia import numpy_color2sepia

def numba_color2sepia(filename):
    '''
    Convert image to sepia using numba.
    Args:
        filename: filename/path to the wanted image.

    Returns: tree dimensional array with sepia values.
    '''
    try:
        image = cv2.imread(filename)
    except Exception:
        print("cant find file specified")
        return
    sep = numpyCal(image)
    return sep

@jit(nopython=True)
def numpyCal(image):
    sep = np.zeros((len(image), len(image[0]), 3), np.uint8)
    sepia_matrix = [[0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]]
    #HT Goes through the with of the picture
    for i in range(len(image)):
        #HT Goes through the height of the picture
        for j in range(len(image[0])):
            #HT Goes through the three pixels
            for k in range(len(image[0][0])):
                temp1 = image[i][j][0] * sepia_matrix[k][2]
                temp2 = image[i][j][1] * sepia_matrix[k][1]
                temp3 = image[i][j][2] * sepia_matrix[k][0]
                sep[i][j][(2 - k)] = min(255, (temp1 + temp2 + temp3))
    return sep


def report_numba_sepia():
    filename = "./rain.jpg"

    f = open("reports/numba_report_color2sepia.txt", "w")
    time3_numba = (timeit.timeit(lambda: numba_color2sepia(filename), number=3)) / 3
    time3_numpy = (timeit.timeit(lambda: numpy_color2sepia(filename), number=3))/3
    time3_python = (timeit.timeit(lambda: python_color2sepia(filename), number=3))/3
    time_diff_numba_python = time3_python / time3_numba
    time_diff_numba_numpy = time3_numba / time3_numpy


    f.write(f"Dimensions of the image being converted to sepia: {filename}")
    image = cv2.imread(filename)
    f.write("\n")
    f.write(f"H: {len(image)} \nW: {len(image[0])} \nC: {len(image[0][0])}")
    f.write("\n\n")

    f.write("Timing : numba_color2sepia")
    f.write("\n")
    f.write("Average runtime running python_color2sepia after 3 runs : {:.6f} s".format(time3_numba))
    f.write("\n")
    f.write("Average runtime of numba_color2sepia is {:.0f} times faster than python_color2sepia".format(time_diff_numba_python))
    f.write("\n")
    f.write("Average runtime of numba_color2sepia is {:.0f} times slower than numpy_color2sepia".format(time_diff_numba_numpy))
    f.write("\n")
    f.write("Timing performed using : timeit")
    f.write("\n\n")
    f.write("There is one main advantage to use Numba, that is for many runs of the algorithm, because it utilize the "
            "cash. The main disadvantage is that Numba is a not that much used pack, and it will require an extra "
            "install, which takes time.")
    f.close()
