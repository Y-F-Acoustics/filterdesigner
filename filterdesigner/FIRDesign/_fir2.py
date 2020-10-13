import numpy as np
import scipy.signal as signal
import scipy.interpolate as ip
from typing import List, Tuple

def fir2(n : int, f, m, npt : int =512, window=None) -> Tuple:
    """
    FIR filter design using the window method.

    From the given frequencies `f` and corresponding gains `m`,
    this function constructs an FIR filter with linear phase and
    (approximately) the given frequency response.

    Parameters
    ----------
    n : int
        The number of taps in the FIR filter.  `n` must be less than
        `npt`.
        
    f : array_like, 1D
        The frequency sampling points. Typically 0.0 to 1.0 with 1.0 being
        Nyquist.
        The values in `f` must be nondecreasing.  A value can be repeated
        once to implement a discontinuity.  The first value in `f` must
        be 0, and the last value must be 1.
        
    m : array_like
        The filter gains at the frequency sampling points. Certain
        constraints to gain values, depending on the filter type, are applied,
        see Notes for details.
        
    npt : int, optional
        The size of the interpolation mesh used to construct the filter.
        The default is 512.  `npt` must be greater than `n/2`.
        
    window : string or (string, float) or float, or None, optional
        Window function to use. Default is "hamming".  See
        `scipy.signal.get_window` for the complete list of possible values.
        If None, no window function is applied.

    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)

    """
    
    if npt <= n/2:
        raise ValueError('`npt` must be larger than `n/2`.')
    
    nfreqs = npt * 2
        
    num = signal.firwin2(n, f, m, nfreqs=nfreqs, window=window)
    den = 1
    
    return num, den