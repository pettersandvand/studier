
from python_color2sepia import report_py_sepia
from numpy_color2sepia import report_numpy_sepia
from numba_color2sepia import report_numba_sepia

"""
    HT:
    Run this file, to make reports from the sepia-python, sepia-numpy and sepia-numba implementation.
    The functions report_py_sepia, report_numpy_sepia, report_numba_sepia make reports you could fine in the folder "reports"

"""

def makeReports():
    report_py_sepia()
    report_numpy_sepia()
    report_numba_sepia()
makeReports()