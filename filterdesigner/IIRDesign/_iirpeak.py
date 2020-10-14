import scipy.signal as signal
from typing import List, Tuple
import numpy as np 

def iirpeak(w0:float, bw:float)->Tuple:
    """
    Design second-order IIR peak (resonant) digital filter.
    
    A peak filter is a band-pass filter with a narrow bandwidth 
    (high quality factor). 
    It rejects components outside a narrow frequency band.

    Caution : This function is not supported variable magnitude response.

    Parameters
    ----------
    w0 : float
        Peak frequency, specified as a positive scalar in the range 
        0.0 < w0 < 1.0, where 1.0 corresponds to π radiance per sample in 
        the frequency range.
        
    bw : float
        Bandwidth at the –3 dB point, specified as a positive scalar in 
        the range 0.0 < w0 < 1.0.

    Returns
    -------
    system :a tuple of array_like describing the system.
        The following gives the number of elements in the tuple and
        the interpretation:
                
                * (num, den)

    """
    
    if (type(w0) in [float, np.float, np.float16, np.float32, np.float64]) == False:
        raise ValueError("`w0` must be a float.")
        
    if (type(bw) in [float, np.float, np.float16, np.float32, np.float64]) == False:
        raise ValueError("`bw` must be a float.")
        
    # Calcurate quality factor
    Q = w0/bw
    num, den = signal.iirpeak(w0, Q, fs = 2.0);
    
    return num, den
    