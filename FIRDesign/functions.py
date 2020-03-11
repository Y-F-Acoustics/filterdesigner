# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:34:04 2020

@author: Yuki-F
"""

import numpy as np
import scipy.signal as signal
import scipy as sp
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
    elif type(Wn) == list and len(Wn) == 2 and (ftype in ['default', 'bandpass', 'stop']) == False:
        # When the length of Wn equals to 2.
        raise ValueError("If the length of Wn equals to 2, ftype must be"
                         +" 'default', 'bandpass', or 'stop'.")
    elif type(Wn) == list and len(Wn) >= 3 and (ftype in ['default', 'DC-0', 'DC-1']) == False:
        # When the length of Wn is greater than 2.
        raise ValueError("If the length of Wn is greater than 2, ftype must be"
                         +" 'default', 'DC-0', or 'DC-1'.")
    
    #Define default filter types
    if type(Wn) == float and ftype == 'default':
        #If the length of Wn equals to 1, the default filter type is low-pass
        ftype = 'low'
    
    if type(Wn) == list and len(Wn) == 2 and ftype == 'default':
        #If the length of Wn equals to 2, the default filter type is bandpass
        ftype == 'bandpass'
        pass_zero = False
    
    if type(Wn) == list and len(Wn) >= 3 and ftype == 'default':
        #If the length of Wn is greater than 2, the default filter type is DC-0
        ftype == 'DC-0'
        pass_zero = False
        
    num = signal.firwin(n, Wn, window=window, pass_zero=pass_zero, 
                        scale=scaleopt) # Numerator
    den = 1 # Denominator
    
    return num, den


def fir2(n : int, f, m, npt : int =512, window=None) -> Tuple:
    """
    FIR filter design using the window method.

    From the given frequencies `f` and corresponding gains `m`,
    this function constructs an FIR filter with linear phase and
    (approximately) the given frequency response.

    Parameters
    ----------
    n : int
        The number of taps in the FIR filter.  `n` must be less than
        `npt`.
        
    f : array_like, 1D
        The frequency sampling points. Typically 0.0 to 1.0 with 1.0 being
        Nyquist.
        The values in `f` must be nondecreasing.  A value can be repeated
        once to implement a discontinuity.  The first value in `f` must
        be 0, and the last value must be 1.
        
    m : array_like
        The filter gains at the frequency sampling points. Certain
        constraints to gain values, depending on the filter type, are applied,
        see Notes for details.
        
    npt : int, optional
        The size of the interpolation mesh used to construct the filter.
        The default is 512.  `npt` must be greater than `n/2`.
        
    window : string or (string, float) or float, or None, optional
        Window function to use. Default is "hamming".  See
        `scipy.signal.get_window` for the complete list of possible values.
        If None, no window function is applied.

    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)

    """
    
    if npt <= n/2:
        raise ValueError('`npt` must be larger than `n/2`.')
    
    nfreqs = npt * 2
        
    num = signal.firwin2(n, f, m, nfreqs=nfreqs, window=window)
    den = 1
    
    return num, den


def firls(n : int, f, a, w=None) -> Tuple:
    """
    FIR filter design using least-squares error minimization.

    Calculate the filter coefficients for the linear-phase finite
    impulse response (FIR) filter which has the best approximation
    to the desired frequency response described by `f` and
    `a` in the least squares sense (i.e., the integral of the
    weighted mean-squared error within the specified bands is
    minimized).

    Parameters
    ----------
    n : int
        The number of taps in the FIR filter.  `n` must be odd.
        
    f : array_like
        A monotonic nondecreasing sequence containing the band edges in
        Hz. All elements must be non-negative and less than or equal to
        1.
        
    a : array_like
        A sequence the same size as `f` containing the desired gain
        at the start and end point of each band.
        
    w : array_like, optional
        A relative weighting to give to each band region when solving
        the least squares problem. `w` has to be half the size of
        `f`.

    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)
    """

    if n%2 == 0:
        n += 1
        print('Warning: The filter length you inserted is even.')
        print('         The filter length changed to {}.'.format(n))
    
    num = signal.firls(n, f, a, weight=w)
    den = 1
    
    return num, den


def firpm(n : int, f, a, w=None, ftype : str ='hilbert', lgrid : int =16) -> Tuple:
    """
    Parameters
    ----------
    n : int
        The desired filter order. The number of taps is the filter order plus 
        one.
        
    f : array_like
        A monotonic sequence containing the band edges. All elements must be 
        non-negative and less than 1. The length of `f` must be even.
    
    a : array_like
        A sequence half the size of bands containing the desired gain in each
        of the specified bands.
        
    w : array_like, optional
        A relative weighting to give to each band region. The length of weight
        has to be half the length of bands.
        
    ftype :  {‘bandpass’, ‘differentiator’, ‘hilbert’}, optional
        The type of filter:
            ‘bandpass’ : flat response in bands. This is the default.
            ‘differentiator’ : frequency proportional response in bands.
            ‘hilbert’ : filter with odd symmetry, that is, type III
                        (for even order) or type IV (for odd order) linear 
                        phase filters.
        
    lgrid : int, optional
        Grid density. The dense grid used in remez is of size 
        (numtaps + 1) * grid_density. Default is 16.

    Raises
    ------
    ValueError
        If the length of `f` is odd.

    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)

    """
    
    #Error check
    if len(f)%2 != 0:
        raise ValueError('The length of `f` must be even.')
        
    num = signal.remez(n+1, f, a, weight=w, type=ftype, grid_density=lgrid, 
                       fs=2)
    den = 1
    
    return num, den


def sgolay(order : int, flamelen : int) -> Tuple:
    """
    Parameters
    ----------
    order : int
        The order of the polynomial used to fit the samples. polyorder must be 
        less than flamelen.
        
    flamelen : int
        The length of the filter window (i.e. the number of coefficients). 
        framelen must be an odd positive integer.

    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)

    """
    num = signal.savgol_coeffs(flamelen, order)
    den = 1
    
    return num, den

if __name__ == "__main__":
    x = fir1(127, [0.5, 0.75, 0.9], ftype='DC-1')
    y = fir2(127, [0, 0.5, 0.75, 0.9, 1], [1, 1, 1, 1, 0])
    z = firls(127, [0, 0.5, 0.75, 0.9], [1, 1, 1, 0])
    a = firpm(127, [0, 0.25, 0.5, 0.75, 0.9, 1.0], [1, 0, 0])
    b = sgolay(11, 41)