# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 01:00:17 2020

@author: Yuki Fukuda
"""

import scipy.signal as signal
from typing import List, Tuple

def butter(n : int, Wn, ftype :str='default', ds :str= 'd') -> Tuple[float, float]:
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
        
    ftype : {'default', 'lowpass', 'highpass', 'bandpass', 'bandstop'}, optional
        The type of filter. The default is 'default'.
        
    ds : {'d', 's'}, optional
        When 's', return an analog filter, otherwise a digital filter is returned. 
        The default is 'd'.

    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)

    """
    
    ftypelist = ['low', 'high', 'bandpass', 'stop', 'default']
    dslist = ['d', 's']
    analog = False
    fs = None
    
    if (ftype in ftypelist) == False:
        raise ValueError("`ftype` must be 'low', 'high', 'bandpass', 'stop',"
                         + " or 'default'.")
        
    if (ds in dslist) == False:
        raise ValueError("`ds` must be 'd' or 's'.")
        
    if ds == 'd':
        if type(Wn) == list:
            if max(Wn) >= 1.0 or min(Wn) < 0.0:
                raise ValueError("When `ds` is 'd', value of `Wn` must be from"
                                 + "0 to 1.")
        else:
            if Wn >= 1.0 or Wn < 0.0:
                raise ValueError("When `ds` is 'd', value of `Wn` must be from"
                                 + "0 to 1.")
            
        
    if ftype == 'default':
        if type(Wn) == float:
            ftype = 'lowpass'
        else:
            ftype = 'bandpass'
    elif ftype == 'low':
        if type(Wn) == list:
            raise ValueError("`Wn` must be float when `ftype` is 'low'.")
        else:
            ftype = 'lowpass'
    elif ftype == 'high':
        if type(Wn) == list:
            raise ValueError("`Wn` must be float when `ftype` is 'high'.")
        else:
            ftype = 'highpass'
    elif ftype == 'stop':
        if type(Wn) == float:
            raise ValueError("`Wn` must be sequence when `ftype` is 'stop'.")
        else:
            ftype = 'bandstop'
    else:
        #bandpass filter
        if type(Wn) == float:
            raise ValueError("`Wn` must be sequence when `ftype` is 'band'.")
        else:
            ftype = 'bandpass'
            
    if ds == 's':
        analog = True
    else:
        fs = 2
        
    num, den = signal.butter(n, Wn, ftype, analog=analog, output='ba', fs=fs)
    
    return num, den


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    
    num, den = butter(21, 0.6)
    x = signal.freqz(num, den, worN = None, fs = 2.0)
    plt.plot(x[0], np.abs(x[1]))