import scipy.signal as signal
from typing import List, Tuple
import numpy as np 

def polyscale(a, alpha:float):
    """
    Scale roots of polynomial

    b = polyscale(a,alpha) scales the roots of a polynomial in the z-plane, 
    where a is a vector containing the polynomial coefficients and alpha is 
    the scaling factor.

    If alpha is a real value in the range [0 1], then the roots of a are 
    radially scaled toward the origin in the z-plane. Complex values for alpha 
    allow arbitrary changes to the root locations.

    """
    r = np.roots(a)
    
    return r * alpha
    