import numpy as np
import scipy.signal as signal
import scipy.interpolate as ip
from typing import List, Tuple

def firls(n : int, f, a, w=None) -> Tuple:
    """
    FIR filter design using least-squares error minimization.

    Calculate the filter coefficients for the linear-phase finite
    impulse response (FIR) filter which has the best approximation
    to the desired frequency response described by `f` and
    `a` in the least squares sense (i.e., the integral of the
    weighted mean-squared error within the specified bands is
    minimized).

    Parameters
    ----------
    n : int
        The number of taps in the FIR filter.  `n` must be odd.
        
    f : array_like
        A monotonic nondecreasing sequence containing the band edges in
        Hz. All elements must be non-negative and less than or equal to
        1.
        
    a : array_like
        A sequence the same size as `f` containing the desired gain
        at the start and end point of each band.
        
    w : array_like, optional
        A relative weighting to give to each band region when solving
        the least squares problem. `w` has to be half the size of
        `f`.

    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)
    """

    if n%2 == 0:
        n += 1
        print('Warning: The filter length you inserted is even.')
        print('         The filter length changed to {}.'.format(n))
    
    num = signal.firls(n, f, a, weight=w)
    den = 1
    
    return num, den