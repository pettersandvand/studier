import cv2
import numpy as np

def python_color2gray(filename):
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
    for i in range(len(image)):
        for j in range(len(image[i])):
            tmp = image[i][j][0] * .21 + image[i][j][1] * .72 + image[i][j][2] * .07
            image[i][j] = (tmp, tmp, tmp)
    image = image.astype("uint8")
    return image


def python_color2sepia(filename):
    '''
    Convert image to grayscale using python.
    Args:
        filename: filename/path to the wanted image.

    Returns: tree dimensional array with sepia values.
    '''
    try:
        image = cv2.imread(filename)
    except Exception:
        print("cant find file specified")
        return
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
                sep[i][j][(2-k)] = min(255, (temp1 + temp2 + temp3))
    return sep