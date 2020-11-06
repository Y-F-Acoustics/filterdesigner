import scipy.signal as signal
import warnings
import scipy as sp
import numpy as np
from typing import List, Tuple
import sys

def grpdelay(system, worN:int=512, fs=2*np.pi)->Tuple:
    """
    Group delay of a digital filter.
    
    Parameters
    ----------
        system : a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
            
                * (num, den)
                
        worN : {None, int, array_like}, optional
            If a single integer, then compute at that many frequencies 
            (default is N=512). This is a convenient alternative to:

                np.linspace(0, fs if whole else fs/2, N, endpoint=False)
            
            Using a number that is fast for FFT computations can result in 
            faster computations (see Notes).
            If an array_like, compute the response at the frequencies given. 
            These are in the same units as fs.
            
        fs : float, optional
            The sampling frequency of the digital system.
            Defaults to 2*pi radians/sample (so w is from 0 to pi).
            
    Returns
    -------
        w : ndarray
            The frequencies at which h was computed, in the same units as fs.
            By default, w is normalized to the range [0, pi) (radians/sample).
            
        gd : ndarray
            The group delay.
    """
    
    # Calcurate the group delay of the digital filter
    w, gd = signal.group_delay(system, w = worN, fs = fs)
    
    if type(system[1]) in [float, np.float, np.float16, np.float32, np.float64,  
                       int, np.int, np.int0, np.int16, np.int32, np.int64, np.int8] and system[1] == 1:
        # If filter is FIR, round the group_delay
        gd = np.round(gd)
    
    # Return the frequency and group delay
    return w, gd
    
