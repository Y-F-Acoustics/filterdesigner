import scipy.signal as signal
from typing import List, Tuple
import numpy as np 

def cheby2(n:int, Rs:float, Ws, ftype:str='default', zs:str='z')->Tuple:
    """
    Chebyshev type II digital and analog filter design.

    Design an Nth-order digital or analog Chebyshev type II filter and return 
    the filter coefficients.
    
    Parameters
    ----------
    n : int
        The order of the filter.
        
    Rs : float
        The minimum attenuation required in the stop band. 
        Specified in decibels, as a positive number.
        
    Ws : array_like
        A scalar or length-2 sequence giving the critical frequencies. 
        For Type II filters, this is the point in the transition band at which 
        the gain first reaches -Rs.
        For digital filters, the stopband edge frequencies must lie between 
        0 and 1, where 1 corresponds to the Nyquist rate—half the sample rate 
        or π rad/sample.
        For analog filters, the stopband edge frequencies must be expressed in 
        radians per second and can take on any positive value.
        
    ftype : {'default', 'law', 'high', 'bandpass', 'stop'}, optional
        The type of filter. Default is ‘lowpass’.
        
    zs : {'z', 's'}, optional
        When 's', return an analog filter, otherwise a digital filter is
        returned.
        
    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)
    """
    
    # default parameters
    analog = False
    fs = None
    
    zslist = ['z', 's']
    ftypelist = ['default', 'low', 'high', 'bandpass', 'stop']
    
    # Filter type
    if (ftype in ftypelist) == False:
        raise ValueError("`ftype` must be 'low', 'high', 'bandpass', 'stop',"
                         + " or 'default'.")
    
    # Digital or Analog
    if (zs in zslist) == False:
        raise ValueError("`zs` must be 'z' or 's'.")
        
    if (type(n) in [int, np.int, np.int0, np.int16, np.int32, np.int64, 
           np.int8]) == False:
        raise ValueError("`n` must be an integer.")
        
    # Filter types
    if ftype == 'default':
        if type(Ws) in [float, np.float, np.float16, np.float32, np.float64]:
            ftype = 'lowpass'
        else:
            ftype = 'bandpass'
    elif ftype == 'low':
        if type(Ws) in [list, np.ndarray]:
            raise ValueError("`Wn` must be float when `ftype` is 'low'.")
        else:
            ftype = 'lowpass'
    elif ftype == 'high':
        if type(Ws) in [list, np.ndarray]:
            raise ValueError("`Wn` must be float when `ftype` is 'high'.")
        else:
            ftype = 'highpass'
    elif ftype == 'stop':
        if type(Ws) in [float, np.float, np.float16, np.float32, np.float64]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'stop'.")
        else:
            ftype = 'bandstop'
    else:
        #bandpass filter
        if type(Ws) in [float, np.float, np.float16, np.float32, np.float64]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'band'.")
        else:
            ftype = 'bandpass'
            
    # When analog filter
    if zs == 's':
        analog = True
    else:
        fs = 2
        
    # Calcurate the filter coefficients
    num, den = signal.cheby2(n, Rs, Ws, btype=ftype, analog=analog, output='ba', fs=fs)
    return num, den
