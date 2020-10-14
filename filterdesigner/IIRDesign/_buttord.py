import scipy.signal as signal
from typing import List, Tuple
import numpy as np

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