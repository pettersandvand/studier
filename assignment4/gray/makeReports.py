from python_color2gray import report_py_gray
from numpy_color2gray import report_numpy_gray
from numba_color2gray import report_numba_gray

"""
    HT:
    Run this file, to make reports from the gray-python, gray-numpy and gray-numba implementation.
    The functions report_py_gray, report_numpy_gray, report_numba_gray make reports you could fine in the folder "reports"

"""

def makeReports():
    report_py_gray()
    report_numpy_gray()
    report_numba_gray()
makeReports()