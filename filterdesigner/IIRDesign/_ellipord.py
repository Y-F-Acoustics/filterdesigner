import scipy.signal as signal
from typing import List, Tuple
import numpy as np 

def ellipord(Wp, Ws, Rp:float, Rs:float, zs='z')->Tuple:
    """
    Elliptic (Cauer) filter order selection.
    
    Return the order of the lowest order digital or analog elliptic filter that 
    loses no more than Rp dB in the passband and has at least Rs dB 
    attenuation in the stopband.
    
    Parameters
    ----------
    Wp, Ws : float
        Passband and stopband edge frequencies, specified as a scalar or 
        a two-element vector with values between 0 and 1 inclusive, with 
        1 corresponding to the normalized Nyquist frequency, π rad/sample. 
        
        For digital filters, the unit of passband corner frequency is in 
        radians per sample. 
        For example,
        ・Lowpass: wp = 0.2, ws = 0.3
        ・Highpass: wp = 0.3, ws = 0.2
        ・Bandpass: wp = [0.2, 0.5], ws = [0.1, 0.6]
        ・Bandstop: wp = [0.1, 0.6], ws = [0.2, 0.5]
        
        For analog filters, passband corner frequency is in radians per second,
        and the passband can be infinite.
        
    Rp : float
        The maximum loss in the passband (dB).
        
    Rs : float
        The minimum attenuation in the stopband (dB).
        
    zs : {'z', 's'}, optional
        When 's', return an analog filter, otherwise a digital filter is 
        returned.
        
    Returns
    -------
    n : int
        The lowest order for a Chebyshev type I filter that meets specs.
        
    Wp : ndarray or float
        The Chebyshev natural frequency (the “3dB frequency”) for use with 
        cheby1 to give filter results. 
    """
    
    #Default parameters
    analog = False
    fs = None
    
    zslist = ['z', 's']
    
    # Digital or Analog
    if (zs in zslist) == False:
        raise ValueError("`zs` must be 'z' or 's'.")
    
    #Check the consistency of `Wp` and `Ws`
    if type(Wp) in [float, np.float, np.float16, np.float32, np.float64,
                   int, np.int, np.int0, np.int16, np.int32, np.int64, np.int8]:
        if type(Wp) != type(Ws):
            raise ValueError("`Wp` and `Ws` must be the same type.")
    elif type(Wp) == list or tuple or np.array:
        if type(Wp) != type(Ws):
            raise ValueError("`Wp` and `Ws` must be the same type.")
        elif len(Wp) != len(Ws):
            raise ValueError("`Wp` and `Ws` must have the same length.")
    else:
        raise("`Wp` and `Ws` must be float , list or tuple.")
        
    # Check the type of Rp
    if (type(Rp) in [int, np.int, np.int0, np.int16, np.int32, np.int64\
        , np.int8, float, np.float, np.float16, np.float32, np.float64]) == False:
        raise ValueError("`Rp` must be the number.")
    
    # Check the type of Rs
    if (type(Rs) in [int, np.int, np.int0, np.int16, np.int32, np.int64\
        , np.int8, float, np.float, np.float16, np.float32, np.float64]) == False:
        raise ValueError("`Rp` must be the number.")
    
    # Change the default parameters
    if zs == 's':
        analog = True
    else:
        fs = 2
        
    # calcurate the filter parameters
    n, Wp = signal.ellipord(Wp, Ws, float(Rp), float(Rs), analog=analog, fs=fs)
    
    return int(n), Wp
