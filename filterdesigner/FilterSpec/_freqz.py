import scipy.signal as signal
import warnings
import scipy as sp
import numpy as np
from typing import List, Tuple
import sys    
        
def freqz(system, worN:int=512, fs=2*np.pi, outform:str='complex')->Tuple:
    """
    Frequency response of a digital filter.
    
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
                
        h : ndarray
            The frequency response, as complex numbers.
    """
    
    #Calcurate frequency response
    w, h = signal.freqz(system[0], system[1], worN=worN, fs=fs)
    
    if outform == 'complex':
        #If outform is 'complex', return the value
        return w, h
    
    elif outform == 'dB':
        #If outform is 'dB', return 20*np.log10(np.abs(h))
        h = 20 * np.log10(np.abs(h))
        return w, h
    
    elif outform == 'abs':
        #If outform is 'abs', return np.abs(h)
        h = np.abs(h)
        return w, h
    
    else:
        #If the others raise the exception.
        raise ValueError("Parameter outform is must be 'complex', 'dB', or"
                         +"'abs'.")
    