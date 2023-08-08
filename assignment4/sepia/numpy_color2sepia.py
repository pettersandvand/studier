import timeit
import cv2
import numpy as np

from python_color2sepia import python_color2sepia



def numpy_color2sepia(filename):
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

    #HT Used to decide pixels weights.
    sepia_matrix = np.array([[0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]])

    sep = image @ sepia_matrix.T
    #HT Change to RGB
    sep = np.flip(sep, axis = 2)
    sepia = sep.astype("uint8")
    np.putmask(sepia, sepia > 255, 255)
    return sep

def report_numpy_sepia():
    filename = "./rain.jpg"

    f = open("reports/numpy_report_color2sepia.txt", "w")
    time3_numpy = (timeit.timeit(lambda: numpy_color2sepia(filename), number=3))/3
    time3_python = (timeit.timeit(lambda: python_color2sepia(filename), number=3))/3
    timeDiff = time3_python / time3_numpy

    #HT Make the report
    f.write(f"Dimensions of the image being grayscaled: {filename}")
    image = cv2.imread(filename)
    f.write("\n")
    f.write(f"H: {len(image)} \nW: {len(image[0])} \nC: {len(image[0][0])}")
    f.write("\n\n")

    f.write("Timing : numpy_color2gray")
    f.write("\n")
    f.write("Average runtime running python_color2gray after 3 runs : {:.6f} s".format(time3_numpy))
    f.write("\n")
    f.write("Average runtime of numpy_color2gray is {:.0f} times faster than python_color2gray".format(timeDiff))
    f.write("Timing performed using : timeit")
    f.close()
