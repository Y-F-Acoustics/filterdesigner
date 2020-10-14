import scipy.signal as signal
from typing import List, Tuple
import numpy as np 

def polystab(a):
    """
    Stabilize polynomial
    
    polystab stabilizes a polynomial with respect to the unit circle; it 
    reflects roots with magnitudes greater than 1 inside the unit circle.

    b = polystab(a) returns a row vector b containing the stabilized polynomial. 
    a is a vector of polynomial coefficients, normally in the z-domain:
        
    A(z) = a(0) + a(1)*z^-1 + ... + a(m)*z^-m
    """
    a = np.array(a)
    v = np.roots(a)
    vs = 0.5 * (np.sign(np.abs(v) - 1) + 1)
    v = (1 - vs) * v + vs / np.conj(v)
    b = a[0] * np.poly(v)
    
    return b
    