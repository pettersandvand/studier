import timeit
import cv2
import numpy as np

import python_color2gray


def numpy_color2gray(filename):
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
    height, width = image.shape[:2]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = np.zeros((height, width), np.uint8)
    #HT Add the weights
    gray = image[:, :, 0:1]*0.21 + image[:, :, 1:2]*0.72 + image[:, :, 2:3]*0.07
    gray = gray.astype("uint8")
    return gray

def report_numpy_gray():
    filename = "./rain.jpg"

    #HT open the file
    f = open("reports/numpy_report_color2gray.txt", "w")
    time3_numpy = (timeit.timeit(lambda: numpy_color2gray(filename), number=3))/3
    time3_python = (timeit.timeit(lambda: python_color2gray.python_color2gray(filename), number=3))/3
    timeDiff = time3_python / time3_numpy
    #HT removed comment-out line
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
