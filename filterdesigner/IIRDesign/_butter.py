import scipy.signal as signal
from typing import List, Tuple
import numpy as np

def butter(n : int, Wn, ftype :str='default', zs :str= 'z') -> Tuple:
    """
    Butterworth digital and analog filter design.

    Design an Nth-order digital or analog Butterworth filter and return the 
    filter coefficients.

    Parameters
    ----------
    n : int
        The order of the filter.
        
    Wn : array_like
        The critical frequency or frequencies. For lowpass and highpass 
        filters, Wn is a scalar; for bandpass and bandstop filters, 
        Wn is a length-2 sequence.
        For a Butterworth filter, this is the point at which the gain drops to
        1/sqrt(2) that of the passband (the “-3 dB point”).
        For digital filters, Wn are in the same units as fs. 
        By default, fs is 2 half-cycles/sample, so these are normalized from 
        0 to 1, where 1 is the Nyquist frequency. 
        (Wn is thus in half-cycles / sample.)
        For analog filters, Wn is an angular frequency (e.g. rad/s).
        
    ftype : {'default', 'low', 'high', 'bandpass', 'stop'}, optional
        The type of filter. The default is 'default'.
        
    zs : {'z', 's'}, optional
        When 's', return an analog filter, otherwise a digital filter is returned. 
        The default is 'z'.

    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)

    """
    
    ftypelist = ['low', 'high', 'bandpass', 'stop', 'default']
    zslist = ['z', 's']
    analog = False
    fs = None
    
    if (type(n) in [int, np.int, np.int0, np.int16, np.int32, np.int64, 
           np.int8]) == False:
        raise ValueError("`n` must be an integer.")
    
    if (ftype in ftypelist) == False:
        raise ValueError("`ftype` must be 'low', 'high', 'bandpass', 'stop',"
                         + " or 'default'.")
        
    if (zs in zslist) == False:
        raise ValueError("`zs` must be 'z' or 's'.")
        
    if zs == 'z':
        if type(Wn) in [list, np.ndarray]:
            if np.max(Wn) >= 1.0 or np.min(Wn) < 0.0:
                raise ValueError("When `zs` is 'z', value of `Wn` must be from"
                                 + "0 to 1.")
        else:
            if Wn >= 1.0 or Wn < 0.0:
                raise ValueError("When `zs` is 'z', value of `Wn` must be from"
                                 + "0 to 1.")
            
        
    if ftype == 'default':
        if type(Wn) in [float, np.float, np.float16, np.float32, np.float64,  
                       int, np.int, np.int0, np.int16, np.int32, np.int64, np.int8]:
            ftype = 'lowpass'
        else:
            ftype = 'bandpass'
    elif ftype == 'low':
        if type(Wn) in [list, np.ndarray]:
            raise ValueError("`Wn` must be float when `ftype` is 'low'.")
        else:
            ftype = 'lowpass'
    elif ftype == 'high':
        if type(Wn) in [list, np.ndarray]:
            raise ValueError("`Wn` must be float when `ftype` is 'high'.")
        else:
            ftype = 'highpass'
    elif ftype == 'stop':
        if type(Wn) in [float, np.float, np.float16, np.float32, np.float64,  
                       int, np.int, np.int0, np.int16, np.int32, np.int64, np.int8]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'stop'.")
        else:
            ftype = 'bandstop'
    else:
        #bandpass filter
        if type(Wn) in [float, np.float, np.float16, np.float32, np.float64,  
                       int, np.int, np.int0, np.int16, np.int32, np.int64, np.int8]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'band'.")
        else:
            ftype = 'bandpass'
            
    if zs == 's':
        analog = True
    else:
        fs = 2
        
    num, den = signal.butter(n, Wn, ftype, analog=analog, output='ba', fs=fs)
    
    return num, den
