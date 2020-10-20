import scipy.signal as signal
import warnings
import scipy as sp
import numpy as np
from typing import List, Tuple
import sys
    
def phasez(system, worN:int=512, fs=2*np.pi, deg:bool=False)->Tuple:
    """
    Phase response of a digital filter.
    
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
            
        deg : bool, optional
            If True, the phase response is returned as degree.
            Default is False.
            
    Returns
    -------
        w : ndarray
            The frequencies at which h was computed, in the same units as fs.
            By default, w is normalized to the range [0, pi) (radians/sample).
            
        phase : ndarray
            The phase response.
    """
    
    # Calcurate the frequency response of the digital filter.
    w, h = freqz(system, worN = worN, fs = fs)
    
    # Calcurate the phase response from frequency response.
    phase = sp.unwrap(sp.angle(h))
    
    # If deg is True, return the phase response as degree
    if deg == True:
        phase = np.rad2deg(phase)
    
    return w, phase
    