import numpy as np
import scipy.signal as signal
import scipy.interpolate as ip
from typing import List, Tuple

def fir1(n : int, Wn, ftype : str ='default', window='hamming', scaleopt : bool =True) -> Tuple:
    """
    FIR filter design using the window method.
    
    This function computes the coefficients of a finite impulse response filter. 
    The filter will have linear phase; it will be Type I if n is odd 
    and Type II if numtaps is even.

    Type II filters always have zero response at the Nyquist frequency, 
    so a ValueError exception is raised if firwin is called with n even 
    and having a passband whose right end is at the Nyquist frequency.
    
    
    Parameters
    ----------
        n : int
            Length of the filter (number of coefficients, i.e. the filter 
            order + 1). 
            `n` must be odd if a passband includes the Nyquist frequency.
            
        Wn : float or 1D array_like
            Cutoff frequency of filter (expressed in the same units as fs) 
            OR an array of cutoff frequencies (that is, band edges). 
            In the latter case, the frequencies in `Wn` should be positive 
            and monotonically increasing between 0 and 1. 
            The values 0 and 1 must not be included in `Wn`.
        
        ftype : string, optional
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
        
        window : string or tuple of string and parameter values, optional
            Desired window to use. See 'scipy.signal.get_window' for a list of 
            windows and required parameters.
            
        scaleopt : bool, optional
            Set to True to scale the coefficients so that the frequency response 
            is exactly unity at a certain frequency. That frequency is either:
                
            - 0 (DC) if the first passband starts at 0 (i.e. pass_zero is True)
            - fs/2 (the Nyquist frequency) if the first passband ends at fs/2 
              (i.e the filter is a single band highpass filter); center of 
              first passband otherwise
    
    Returns
    -------
        system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)
                
    Raises
    ------
        ValueError
            -If any value in `Wn` is less than or equal to 0 or greater
             than or equal to 1, if the values in `Wn` are not strictly
             monotonically increasing, or if `n` is even but a passband
             includes the Nyquist frequency.
            -If the length of `Wn` equals to 1 but `ftype` is defined to
             other than 'default', 'low', 'high'.
            -If the length of `Wn` equals to 2 but `ftype` is defined to
             other than 'default', 'bandpass', 'stop'.
            -If the length of `Wn` more than 2 but `ftype` is defined to
             other than 'default', 'DC-0', 'DC-1'.
            -If `ftype` is other than 'default', 'low', 'bandpass', 'high', 
             'stop', 'DC-0', 'DC-1'.
    """
    
    # Default parameters
    filtertype = ['default', 'low', 'bandpass', 'high', 'stop', 'DC-0', 'DC-1']
    pass_zero = True
    
    #Filter type check
    if (ftype in filtertype) == False:
        raise ValueError("ftype must be 'default', 'low', 'bandpass', 'high'"
                         +", 'stop', 'DC-0' or 'DC-1'.")
    
    #Filter length check
    if type(Wn) == float and (ftype in ['default', 'low', 'high']) == False:
        # When the length of Wn equals to 1.
        raise ValueError("If the length of Wn equals to 1, ftype must be"
                         +" 'default', 'low', or 'high'.")
    elif type(Wn) == list and len(Wn) == 2 and (ftype in ['default', 'bandpass', 'stop', 'DC-0', 'DC-1']) == False:
        # When the length of Wn equals to 2.
        raise ValueError("If the length of Wn equals to 2, ftype must be"
                         +" 'default', 'bandpass', 'stop', 'DC-0', 'DC-1'.")
    elif type(Wn) == list and len(Wn) >= 3 and (ftype in ['default', 'DC-0', 'DC-1']) == False:
        # When the length of Wn is greater than 2.
        raise ValueError("If the length of Wn is greater than 2, ftype must be"
                         +" 'default', 'DC-0', or 'DC-1'.")
    
    #Define default filter types
    if type(Wn) == float and ftype == 'default':
        #If the length of Wn equals to 1, the default filter type is low-pass
        ftype = 'low'
    
    if type(Wn) == list and len(Wn) == 2 and (ftype == 'default' or ftype == 'DC-0'):
        #If the length of Wn equals to 2, the default filter type is bandpass
        ftype == 'bandpass'
    
    if type(Wn) == list and len(Wn) >= 3 and ftype == 'default':
        #If the length of Wn is greater than 2, the default filter type is DC-0
        ftype == 'DC-0'
    
    if ftype in ['high', 'bandpass', 'DC-0']:
        pass_zero = False
        
    num = signal.firwin(n, Wn, window=window, pass_zero=pass_zero, 
                        scale=scaleopt) # Numerator
    den = 1 # Denominator
    
    return num, den