import numpy as np
import scipy.signal as signal
import scipy.interpolate as ip
from typing import List, Tuple


def firpm(n : int, f, a, w=None, ftype : str ='hilbert', lgrid : int =16) -> Tuple:
    """
    Parameters
    ----------
    n : int
        The desired filter order. The number of taps is the filter order plus 
        one.
        
    f : array_like
        A monotonic sequence containing the band edges. All elements must be 
        non-negative and less than 1. The length of `f` must be even.
    
    a : array_like
        A sequence half the size of bands containing the desired gain in each
        of the specified bands.
        
    w : array_like, optional
        A relative weighting to give to each band region. The length of weight
        has to be half the length of bands.
        
    ftype :  {‘bandpass’, ‘differentiator’, ‘hilbert’}, optional
        The type of filter:
            ‘bandpass’ : flat response in bands. This is the default.
            ‘differentiator’ : frequency proportional response in bands.
            ‘hilbert’ : filter with odd symmetry, that is, type III
                        (for even order) or type IV (for odd order) linear 
                        phase filters.
        
    lgrid : int, optional
        Grid density. The dense grid used in remez is of size 
        (numtaps + 1) * grid_density. Default is 16.

    Raises
    ------
    ValueError
        If the length of `f` is odd.

    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)

    """
    
    #interpolate the frequency band from matlab-like to scipy.
    x = [i for i in range(len(f))]
    ipf = ip.interp1d(x, f)
    f_new = ipf(np.linspace(x[0], x[-1], 2*len(x)))
        
    num = signal.remez(n+1, f_new, a, weight=w, type=ftype, grid_density=lgrid, 
                       fs=2)
    den = 1
    
    return num, den
    