import numpy as np
import scipy.signal as signal
import scipy.interpolate as ip
from typing import List, Tuple

def sgolay(order : int, flamelen : int) -> Tuple:
    """
    Parameters
    ----------
    order : int
        The order of the polynomial used to fit the samples. polyorder must be 
        less than flamelen.
        
    flamelen : int
        The length of the filter window (i.e. the number of coefficients). 
        framelen must be an odd positive integer.

    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)

    """
    num = signal.savgol_coeffs(flamelen, order)
    den = 1
    
    return num, den