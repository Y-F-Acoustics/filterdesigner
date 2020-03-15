# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 01:00:17 2020

@author: Yuki Fukuda
"""

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
        
    ftype : {'default', 'lowpass', 'highpass', 'bandpass', 'bandstop'}, optional
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
        if type(Wn) in [float, np.float, np.float16, np.float32, np.float64]:
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
        if type(Wn) in [float, np.float, np.float16, np.float32, np.float64]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'stop'.")
        else:
            ftype = 'bandstop'
    else:
        #bandpass filter
        if type(Wn) in [float, np.float, np.float16, np.float32, np.float64]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'band'.")
        else:
            ftype = 'bandpass'
            
    if zs == 's':
        analog = True
    else:
        fs = 2
        
    num, den = signal.butter(n, Wn, ftype, analog=analog, output='ba', fs=fs)
    
    return num, den


def buttord(Wp, Ws, Rp, Rs, zs:str='z')->Tuple:
    """
    Butterworth filter order selection.
    
    Return the order of the lowest order digital or analog Butterworth filter 
    that loses no more than Rp dB in the passband and has at least Rs dB 
    attenuation in the stopband.
    
    Parameters
    ----------
    Wp, Ws : float
        Passband and stopband edge frequencies.
        For digital filters, these are in the same units as fs. By default, 
        fs is 2 half-cycles/sample, so these are normalized from 0 to 1, 
        where 1 is the Nyquist frequency. 
        (wp and ws are thus in half-cycles / sample.) 
        
        For example:
            ・ Lowpass: wp = 0.2, ws = 0.3
            ・ Highpass: wp = 0.3, ws = 0.2
            ・ Bandpass: wp = [0.2, 0.5], ws = [0.1, 0.6]
            ・ Bandstop: wp = [0.1, 0.6], ws = [0.2, 0.5]
            
        For analog filters, wp and ws are angular frequencies (e.g. rad/s).
        
    Rp : float
        The maximum loss in the passband (dB).
        
    Rs : float
        The minimum attenuation in the stopband (dB).
        
    zs : {'z', 's'}, optional
        When 's', return an analog filter, otherwise a digital filter is 
        returned.
        The default is 's'.
        
    Returns
    -------
    n : int
        The lowest order for a Butterworth filter which meets specs.
        
    Wn : ndarray or float
        The Butterworth natural frequency (i.e. the “3dB frequency”). 
        Should be used with butter to give filter results. 
    """
    
    zslist = ['z', 's']
    
    # Default parameters.
    analog = False
    fs = None
    
    # Digital or analog
    if (zs in zslist) == False:
        raise ValueError("`zs` must be 'z' or 's'.")
    
    # When analog filter
    if zs == 's':
        analog = True
    else:
        fs = 2
      
    # Calcurate filter order and cutoff frequencies using signal.buttord
    n, Wn = signal.buttord(Wp, Ws, Rp, Rs, analog=analog, fs=fs)
    
    # Return results.
    return int(n), Wn
    
    


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    
    n, Wn = buttord(0.6, 0.7, 1, 120)
    num, den = butter(n, Wn)
    x = signal.freqz(num, den, worN = None, fs = 2.0)
    plt.plot(x[0], np.abs(x[1]))