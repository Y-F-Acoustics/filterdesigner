import numpy as np
import scipy.signal as signal
import scipy.interpolate as ip
from typing import Tuple

def kaiserord(f:np.ndarray, a:np.ndarray, dev:np.ndarray, fs:float=2)->Tuple:
    """Kaiser window FIR filter design estimation parameters

    Parameters
    ----------
    f : ndarray
        Band edges. The length of `f` is the length of `2*len(a)-2`.

    a : ndarray
        Band amplitude. The amplitude is specified on the bands defined by `f`. 
        Together, `f` and `a` define a piecewise-constant response function.

    dev : ndarray
        Maximum allowable deviation. 
        `dev` is a vector the same size as `a` that specifies the maximum allowable
        deviation between the frequency response of the output filter and its band 
        amplitude, for each band. The entries in dev specify the passband ripple 
        and the stopband attenuation. Specify each entry in `dev` as a positive number, 
        representing absolute filter gain (unit-less).

    fs : float, optional
        Sample rate in Hz. Use this syntax to specify band edges scaled to a particular 
        application's sample rate. The frequency band edges in f must be from 0 to fs/2.
        Default is 2.

    
    Raises
    ------
    ValueError
        If the length of `f` is not same as `2*len(a)-2`.
        If the length `a` and `dev` is not the same.
        If `dev` includes minus value.

    
    Returns
    -------
    n : int
        Filter order.

    Wn : ndarray
        Normalized frequency band edges.

    beta : float
        The `beta` parameter to be used in the formula for a Kaiser window.

    ftype : string
        Filter type of filter('low', 'high', 'bandpass', 'stop', 'DC-0' 
            or 'DC-1').
            Specified as one of the following.
            
            1. 'low' specifies a lowpass filter with cutoff frequency Wn. 
               'low' is the default for scalar Wn.
            2. 'high' specifies a highpass filter with cutoff frequency Wn.
            3. 'bandpass' specifies a bandpass filter if Wn is a two-element vector. 
               'bandpass' is the default when Wn has two elements.
            4. 'stop' specifies a bandstop filter if Wn is a two-element vector.
            5. 'DC-0' specifies that the first band of a multiband filter is 
               a stopband. 
               'DC-0' is the default when Wn has more than two elements.
            6. 'DC-1' specifies that the first band of a multiband filter is 
               a passband.
               
    """
    if type(f) != np.ndarray:
        if type(f) == list:
            f = np.array(f)
        else:
            f = np.array([f])
    
    if type(a) != np.ndarray:
        if type(a) == list:
            a = np.array(a)
        else:
            a = np.array([a])

    if type(dev) != np.ndarray:
        if type(dev) == list:
            dev = np.array(dev)
        else:
            dev = np.array([dev])

    # Parameter check
    if len(f) != 2*len(a)-2:
        raise ValueError("The length of 'f' must be the length of 2*len(a)-2.")

    if np.any(a[0:len(a)-2] != a[2:len(a)]):
        raise ValueError("Pass and stop bands in a must be strictly alternating.")

    if (len(dev) != len(a)) and (len(dev) != 1):
        raise ValueError("'dev' and 'a' must be the same size.")

    dev = np.min(dev)
    if dev <= 0:
        raise ValueError("'dev' must be larger than 0.")

    # Calcurate normalized frequency band edges.
    Wn = (f[0:len(f):2]+f[1:len(f):2])/fs


    # Determine ftype
    if len(Wn) == 1:
        if a[0] > a[1]:
            ftype = 'low'
        else:
            ftype = 'high'
    elif len(Wn) == 2:
        if a[0] > a[1]:
            ftype = 'stop'
        else:
            ftype = 'bandpass'
    else:
        if a[0] > a[1]:
            ftype = 'DC-1'
        else:
            ftype = 'DC-0'
    
    # Calcurate beta
    A = -20*np.log10(dev)
    beta = signal.kaiser_beta(A)

    # Calcurate n from beta and dev
    width = 2*np.pi*np.min(f[1:len(f):2]-f[0:len(f):2])/fs
    n = np.max((1, int(np.ceil((A-8)/(2.285*width)))))

    # If last band is high, make sure the order of the filter is even
    if ((a[0] > a[1]) == (len(Wn) % 2 == 0)) and (n % 2 == 1):
        n += 1
        
    if len(Wn) == 1:
        Wn = Wn[0]

    return int(n), Wn, beta, ftype
