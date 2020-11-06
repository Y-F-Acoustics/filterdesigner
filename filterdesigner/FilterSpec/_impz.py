import scipy.signal as signal
import warnings
import scipy as sp
import numpy as np
from typing import List, Tuple
import sys

def impz(system:tuple, n:int=None, fs:int=1)->Tuple:
    """
    Impulse response of a digital filter.
    
    Parameters
    ----------
        system : a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)
                
        n : int, optional
            The number of time points to compute.
            
        fs : int optional
            Sampling frequency to calcurate time points. default is 1.
            
    Returns
    -------
        T : ndarray
            A 1-D array of time points.
            
        yout : ndarray
            A 1-D array containing the impulse response of the system (except
            for singularities at zero).
            
    Notes
    -----
        If (num, den) is passed in for ``system``, coefficients for both the
        numerator and denominator should be specified in describing exponent
        order (e.g. ``s^2 + 3s + 5`` would be represented as ``[1, 3, 5]``).
    """
    
    # when FIR filter
    if type(system[1]) == int and system[1] == 1:
        # calcurate time points
        if n == None:
            # automatically determine the length of time points
            T = np.arange(0, (len(system[0]))/fs, 1/fs)
        else:
            # determine the time points which length is n
            T = np.arange(0, n/fs, 1/fs)
            
        # make impulse signal
        x = np.zeros(len(T))
        x[0] = 1
        
        # output the impulse response
        yout = signal.lfilter(system[0], system[1], x)
    else:
        # when IIR filter
        
        # convert to instance of dlti
        dl = signal.dlti(system[0], system[1], dt=1/fs)
        
        # output impulse response of discrete-time system.
        if n == None:
            i_d = signal.dimpulse(dl)
        else:
            i_d = signal.dimpulse(dl, n=n)
            
        # split to time points and impulse response
        T = i_d[0]
        yout = i_d[1][0]
        
    return T, yout
    
