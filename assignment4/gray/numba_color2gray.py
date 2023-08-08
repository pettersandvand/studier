import timeit
import cv2
from python_color2gray import python_color2gray
from numpy_color2gray import numpy_color2gray
from numba import jit


def numba_color2gray(filename):
    '''
    Convert image to grayscale using python.
    Args:
        filename: filename/path to the wanted image.

    Returns: image

    '''
    try:
        image = cv2.imread(filename)
    except Exception:
        print("cant find file specified")
        return
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = numpyCal(image)
    image = image.astype("uint8")
    return image

@jit(nopython=True)
def numpyCal(image):
    #HT Goes through the with of the picture
    for i in range(len(image)):
        #HT Goes through the height of the picture
        for j in range(len(image[i])):
            tmp = image[i][j][0] * .21 + image[i][j][1] * .72 + image[i][j][2] * .07
            image[i][j] = (tmp, tmp, tmp)
    #HT Return the new picture
    return image


def report_numba_gray():
    filename = "./rain.jpg"

    #HT Open the file
    f = open("reports/numba_report_color2gray.txt", "w")
    time3_numba = (timeit.timeit(lambda: numba_color2gray(filename), number=3)) / 3
    time3_numpy = (timeit.timeit(lambda: numpy_color2gray(filename), number=3))/3
    time3_python = (timeit.timeit(lambda: python_color2gray(filename), number=3))/3
    time_diff_numba_python = time3_python / time3_numba
    time_diff_numba_numpy = time3_numba / time3_numpy

    #HT make the report
    f.write(f"Dimensions of the image being grayscaled: {filename}")
    image = cv2.imread(filename)
    f.write("\n")
    f.write(f"H: {len(image)} \nW: {len(image[0])} \nC: {len(image[0][0])}")
    f.write("\n\n")

    f.write("Timing : numba_color2gray")
    f.write("\n")
    f.write("Average runtime running python_color2gray after 3 runs : {:.6f} s".format(time3_numba))
    f.write("\n")
    f.write("Average runtime of numba_color2gray is {:.0f} times faster than python_color2gray".format(time_diff_numba_python))
    f.write("\n")
    f.write("Average runtime of numba_color2gray is {:.0f} times slower than numpy_color2gray".format(time_diff_numba_numpy))
    f.write("\n")
    f.write("Timing performed using : timeit")
    f.write("\n\n")
    f.write("There is one main advantage to use Numba, that is for many runs of the algorithm, because it utilize the "
            "cash. The main disadvantage is that Numba is a not that much used pack, and it will require an extra "
            "install, which takes time.")
    f.close()
