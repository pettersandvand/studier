import cv2
import numpy as np



#Make random image
from instapy.numba_implementation import numba_color2sepia, numba_color2gray
from instapy.numpy_implementation import numpy_color2sepia, numpy_color2gray
from instapy.python_implementation import python_color2sepia, python_color2gray

testImage = np.random.randint(0,255,(400,600,3))
cv2.imwrite('./testImage.png', testImage)
image = cv2.imread('./testImage.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def test_sepia():
    '''

    Returns: test of sepia image converter, known that the implementation is not 100% because of the different math liberies.

    '''
    py_img = python_color2sepia('testImage.png')
    np_img = numpy_color2sepia('testImage.png')
    nb_img = numba_color2sepia('testImage.png')

    # implementation produce same result
    np.testing.assert_array_almost_equal(py_img, nb_img, decimal= -1)
    np.testing.assert_array_almost_equal(nb_img, np_img, decimal = -2)


def test_gray():
    '''

    Returns: test of gray image converter, known that the implementation is not 100% because of the different math liberies.

    '''
    python_gray = python_color2gray('testImage.png')
    numba_gray = numba_color2gray('testImage.png')
    numpy_gray = numpy_color2gray('testImage.png')

    np.testing.assert_array_almost_equal(python_gray, numba_gray, decimal= -1)
    np.testing.assert_array_almost_equal(numba_gray, numpy_gray, decimal = -1)

    assert numpy_gray.shape == (testImage.shape)

