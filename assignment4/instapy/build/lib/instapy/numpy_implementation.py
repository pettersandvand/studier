import cv2
import numpy as np



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
    gray = np.zeros(image.shape)
    bgr = np.array([0.07, 0.72, 0.21])
    gray[:, :, 0] = image.dot(bgr)
    gray[:, :, 1] = image.dot(bgr)
    gray[:, :, 2] = image.dot(bgr)
    gray = gray.astype("uint8")
    return gray

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

    sepia_matrix = np.array([[0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]])

    sep = image @ sepia_matrix.T
    sep = np.flip(sep, axis = 2)
    sepia = sep.astype("uint8")
    np.putmask(sepia, sepia > 255, 255)
    return sep
