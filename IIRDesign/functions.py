# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 01:00:17 2020

@author: Yuki Fukuda
"""

import scipy.signal as signal
from typing import List, Tuple
import numpy as np

def butter(n : int, Wn, ftype :str='default', zs :str= 'z') -> Tuple:
    """
    Butterworth digital and analog filter design.

    Design an Nth-order digital or analog Butterworth filter and return the 
    filter coefficients.

    Parameters
    ----------
    n : int
        The order of the filter.
        
    Wn : array_like
        The critical frequency or frequencies. For lowpass and highpass 
        filters, Wn is a scalar; for bandpass and bandstop filters, 
        Wn is a length-2 sequence.
        For a Butterworth filter, this is the point at which the gain drops to
        1/sqrt(2) that of the passband (the “-3 dB point”).
        For digital filters, Wn are in the same units as fs. 
        By default, fs is 2 half-cycles/sample, so these are normalized from 
        0 to 1, where 1 is the Nyquist frequency. 
        (Wn is thus in half-cycles / sample.)
        For analog filters, Wn is an angular frequency (e.g. rad/s).
        
    ftype : {'default', 'low', 'high', 'bandpass', 'stop'}, optional
        The type of filter. The default is 'default'.
        
    zs : {'z', 's'}, optional
        When 's', return an analog filter, otherwise a digital filter is returned. 
        The default is 'z'.

    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)

    """
    
    ftypelist = ['low', 'high', 'bandpass', 'stop', 'default']
    zslist = ['z', 's']
    analog = False
    fs = None
    
    if (type(n) in [int, np.int, np.int0, np.int16, np.int32, np.int64, 
           np.int8]) == False:
        raise ValueError("`n` must be an integer.")
    
    if (ftype in ftypelist) == False:
        raise ValueError("`ftype` must be 'low', 'high', 'bandpass', 'stop',"
                         + " or 'default'.")
        
    if (zs in zslist) == False:
        raise ValueError("`zs` must be 'z' or 's'.")
        
    if zs == 'z':
        if type(Wn) in [list, np.ndarray]:
            if np.max(Wn) >= 1.0 or np.min(Wn) < 0.0:
                raise ValueError("When `zs` is 'z', value of `Wn` must be from"
                                 + "0 to 1.")
        else:
            if Wn >= 1.0 or Wn < 0.0:
                raise ValueError("When `zs` is 'z', value of `Wn` must be from"
                                 + "0 to 1.")
            
        
    if ftype == 'default':
        if type(Wn) in [float, np.float, np.float16, np.float32, np.float64]:
            ftype = 'lowpass'
        else:
            ftype = 'bandpass'
    elif ftype == 'low':
        if type(Wn) in [list, np.ndarray]:
            raise ValueError("`Wn` must be float when `ftype` is 'low'.")
        else:
            ftype = 'lowpass'
    elif ftype == 'high':
        if type(Wn) in [list, np.ndarray]:
            raise ValueError("`Wn` must be float when `ftype` is 'high'.")
        else:
            ftype = 'highpass'
    elif ftype == 'stop':
        if type(Wn) in [float, np.float, np.float16, np.float32, np.float64]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'stop'.")
        else:
            ftype = 'bandstop'
    else:
        #bandpass filter
        if type(Wn) in [float, np.float, np.float16, np.float32, np.float64]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'band'.")
        else:
            ftype = 'bandpass'
            
    if zs == 's':
        analog = True
    else:
        fs = 2
        
    num, den = signal.butter(n, Wn, ftype, analog=analog, output='ba', fs=fs)
    
    return num, den


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
    
    
def cheby1(n:int, Rp:float, Wp, ftype:str='default', zs:str='z')->Tuple:
    
    """
    Chebyshev type I digital and analog filter design.
    
    Design an Nth-order digital or analog Chebyshev type I filter and return
    the filter coefficients.
    
    Parameters
    ----------
    n : int
        The order of the filter.
        
    Rp : float
        The maximum ripple allowed below unity gain in the passband.
        Specified in decibels, as a positive number.
        
    Wp : array_like
        A scalar or length-2 sequence giving the critical frequencies.
        For Type I filters, this is the point in the transition band at which
        the gain first drops below -Rp.
        For digital filters, the passband edge frequencies must lie 
        between 0 and 1, where 1 corresponds to the Nyquist rate—half the 
        sample rate or π rad/sample.
        For analog filters, the passband edge frequencies must be expressed in 
        radians per second and can take on any positive value.
        
    ftype : {'default', 'law', 'high', 'bandpass', 'stop'}, optional
        The type of filter. Default is ‘lowpass’.
        
    zs : {'z', 's'}, optional
        When 's', return an analog filter, otherwise a digital filter is
        returned.
        
    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)
    """
    
    zslist = ['z', 's']
    ftypelist = ['low', 'bandpass', 'high', 'stop', 'default']
    
    # Default parameters
    analog = False
    fs = None
    
    # Filter type
    if (ftype in ftypelist) == False:
        raise ValueError("`ftype` must be 'low', 'high', 'bandpass', 'stop',"
                         + " or 'default'.")
    
    # Digital or Analog
    if (zs in zslist) == False:
        raise ValueError("`zs` must be 'z' or 's'.")
        
    if (type(n) in [int, np.int, np.int0, np.int16, np.int32, np.int64, 
           np.int8]) == False:
        raise ValueError("`n` must be an integer.")
        
    #If digital filter.    
    if zs == 'z':
        if type(Wp) in [list, np.ndarray]:
            if np.max(Wp) >= 1.0 or np.min(Wp) < 0.0:
                raise ValueError("When `zs` is 'z', value of `Wp` must be from"
                                 + "0 to 1.")
        else:
            if Wp >= 1.0 or Wp < 0.0:
                raise ValueError("When `zs` is 'z', value of `Wp` must be from"
                                 + "0 to 1.")
                
    # Filter types
    if ftype == 'default':
        if type(Wp) in [float, np.float, np.float16, np.float32, np.float64]:
            ftype = 'lowpass'
        else:
            ftype = 'bandpass'
    elif ftype == 'low':
        if type(Wp) in [list, np.ndarray]:
            raise ValueError("`Wn` must be float when `ftype` is 'low'.")
        else:
            ftype = 'lowpass'
    elif ftype == 'high':
        if type(Wp) in [list, np.ndarray]:
            raise ValueError("`Wn` must be float when `ftype` is 'high'.")
        else:
            ftype = 'highpass'
    elif ftype == 'stop':
        if type(Wp) in [float, np.float, np.float16, np.float32, np.float64]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'stop'.")
        else:
            ftype = 'bandstop'
    else:
        #bandpass filter
        if type(Wp) in [float, np.float, np.float16, np.float32, np.float64]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'band'.")
        else:
            ftype = 'bandpass'
        
    # When analog filter
    if zs == 's':
        analog = True
    else:
        fs = 2
        
    # Calcurate the filter coefficients
    num, den = signal.cheby1(n, Rp, Wp, btype=ftype, analog=analog, output='ba'  
                             , fs=fs)
    
    return num, den


def cheb1ord(Wp, Ws, Rp, Rs, zs:str='z')->Tuple[int, float]:
    """
    Chebyshev type I filter order selection.
    
    Return the order of the lowest order digital or analog Chebyshev Type I 
    filter that loses no more than Rp dB in the passband and has at least 
    Rs dB attenuation in the stopband.
    
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
    if type(Wp) in [float, np.float, np.float16, np.float32, np.float64]:
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
    n, Wp = signal.cheb1ord(Wp, Ws, float(Rp), float(Rs), analog=analog, fs=fs)
    
    return int(n), Wp


def cheby2(n:int, Rs:float, Ws, ftype:str='default', zs:str='z')->Tuple:
    """
    Chebyshev type II digital and analog filter design.

    Design an Nth-order digital or analog Chebyshev type II filter and return 
    the filter coefficients.
    
    Parameters
    ----------
    n : int
        The order of the filter.
        
    Rs : float
        The minimum attenuation required in the stop band. 
        Specified in decibels, as a positive number.
        
    Ws : array_like
        A scalar or length-2 sequence giving the critical frequencies. 
        For Type II filters, this is the point in the transition band at which 
        the gain first reaches -Rs.
        For digital filters, the stopband edge frequencies must lie between 
        0 and 1, where 1 corresponds to the Nyquist rate—half the sample rate 
        or π rad/sample.
        For analog filters, the stopband edge frequencies must be expressed in 
        radians per second and can take on any positive value.
        
    ftype : {'default', 'law', 'high', 'bandpass', 'stop'}, optional
        The type of filter. Default is ‘lowpass’.
        
    zs : {'z', 's'}, optional
        When 's', return an analog filter, otherwise a digital filter is
        returned.
        
    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)
    """
    
    # default parameters
    analog = False
    fs = None
    
    zslist = ['z', 's']
    ftypelist = ['default', 'low', 'high', 'bandpass', 'stop']
    
    # Filter type
    if (ftype in ftypelist) == False:
        raise ValueError("`ftype` must be 'low', 'high', 'bandpass', 'stop',"
                         + " or 'default'.")
    
    # Digital or Analog
    if (zs in zslist) == False:
        raise ValueError("`zs` must be 'z' or 's'.")
        
    if (type(n) in [int, np.int, np.int0, np.int16, np.int32, np.int64, 
           np.int8]) == False:
        raise ValueError("`n` must be an integer.")
        
    # Filter types
    if ftype == 'default':
        if type(Ws) in [float, np.float, np.float16, np.float32, np.float64]:
            ftype = 'lowpass'
        else:
            ftype = 'bandpass'
    elif ftype == 'low':
        if type(Ws) in [list, np.ndarray]:
            raise ValueError("`Wn` must be float when `ftype` is 'low'.")
        else:
            ftype = 'lowpass'
    elif ftype == 'high':
        if type(Ws) in [list, np.ndarray]:
            raise ValueError("`Wn` must be float when `ftype` is 'high'.")
        else:
            ftype = 'highpass'
    elif ftype == 'stop':
        if type(Ws) in [float, np.float, np.float16, np.float32, np.float64]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'stop'.")
        else:
            ftype = 'bandstop'
    else:
        #bandpass filter
        if type(Ws) in [float, np.float, np.float16, np.float32, np.float64]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'band'.")
        else:
            ftype = 'bandpass'
            
    # When analog filter
    if zs == 's':
        analog = True
    else:
        fs = 2
        
    # Calcurate the filter coefficients
    num, den = signal.cheby2(n, Rs, Ws, btype=ftype, analog=analog, output='ba'  
                             , fs=fs)
    
    return num, den


def cheb2ord(Wp, Ws, Rp:float, Rs:float, zs:str='z')->Tuple:
    """
    Chebyshev type II filter order selection.
    
    Return the order of the lowest order digital or analog Chebyshev Type II 
    filter that loses no more than Rp dB in the passband and has at least 
    Rs dB attenuation in the stopband.
    
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
        The lowest order for a Chebyshev type II filter that meets specs.
        
    Ws : ndarray or float
        The Chebyshev natural frequency (the “3dB frequency”) for use with 
        cheby2 to give filter results. 
    """
    
    #Default parameters
    analog = False
    fs = None
    
    zslist = ['z', 's']
    
    # Digital or Analog
    if (zs in zslist) == False:
        raise ValueError("`zs` must be 'z' or 's'.")
    
    #Check the consistency of `Wp` and `Ws`
    if type(Wp) in [float, np.float, np.float16, np.float32, np.float64]:
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
    n, Ws = signal.cheb2ord(Wp, Ws, float(Rp), float(Rs), analog=analog, fs=fs)
    
    return int(n), Ws
    

def ellip(n:int, Rp:float, Rs:float, Wp, ftype:str='default', zs:str='z')->Tuple:
    """
    Elliptic (Cauer) digital and analog filter design.
    
    Design an Nth-order digital or analog elliptic filter and return the filter
    coefficients.
    
    Parameters
    ----------
    n : int
        The order of the filter.
        
    Rp : float
        The maximum ripple allowed below unity gain in the passband. 
        Specified in decibels, as a positive number.
        
    Rs : float
        The minimum attenuation required in the stop band. 
        Specified in decibels, as a positive number.
        
    Wp : array_like
        Passband edge frequency, specified as a scalar or a two-element vector.
        The passband edge frequency is the frequency at which the magnitude 
        response of the filter is –Rp decibels. 
        Smaller values of passband ripple, Rp, and larger values of stopband 
        attenuation, Rs, both result in wider transition bands.
        
    ftype : {'default', 'law', 'high', 'bandpass', 'stop'}, optional
        The type of filter. Default is ‘lowpass’.
        
    zs : {'z', 's'}, optional
        When 's', return an analog filter, otherwise a digital filter is
        returned.
    
    Returns
    -------
    system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)
    """
    
    zslist = ['z', 's']
    ftypelist = ['default', 'low', 'high', 'bandpass', 'stop']
    
    # Default parameters
    analog = False
    fs = None
    
    if (zs in zslist) == False:
        raise ValueError("`zs` must be 'z' or 's'.")
        
    if (type(n) in [int, np.int, np.int0, np.int16, np.int32, np.int64, 
           np.int8]) == False:
        raise ValueError("`n` must be an integer.")
    
    if (ftype in ftypelist) == False:
        raise ValueError("`ftype` must be 'low', 'high', 'bandpass', 'stop',"
                         + " or 'default'.")
        
    #If digital filter.    
    if zs == 'z':
        if type(Wp) in [list, np.ndarray]:
            if np.max(Wp) >= 1.0 or np.min(Wp) < 0.0:
                raise ValueError("When `zs` is 'z', value of `Wp` must be from"
                                 + "0 to 1.")
        else:
            if Wp >= 1.0 or Wp < 0.0:
                raise ValueError("When `zs` is 'z', value of `Wp` must be from"
                                 + "0 to 1.")
                
    # Filter types
    if ftype == 'default':
        if type(Wp) in [float, np.float, np.float16, np.float32, np.float64]:
            ftype = 'lowpass'
        else:
            ftype = 'bandpass'
    elif ftype == 'low':
        if type(Wp) in [list, np.ndarray]:
            raise ValueError("`Wn` must be float when `ftype` is 'low'.")
        else:
            ftype = 'lowpass'
    elif ftype == 'high':
        if type(Wp) in [list, np.ndarray]:
            raise ValueError("`Wn` must be float when `ftype` is 'high'.")
        else:
            ftype = 'highpass'
    elif ftype == 'stop':
        if type(Wp) in [float, np.float, np.float16, np.float32, np.float64]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'stop'.")
        else:
            ftype = 'bandstop'
    else:
        #bandpass filter
        if type(Wp) in [float, np.float, np.float16, np.float32, np.float64]:
            raise ValueError("`Wn` must be sequence when `ftype` is 'band'.")
        else:
            ftype = 'bandpass'
    
    # When analog filter
    if zs == 's':
        analog = True
    else:
        fs = 2
        
    # Calcurate the filter coefficients
    num, den = signal.ellip(n, Rp, Rs, Wp, btype=ftype, analog=analog, output='ba'  
                             , fs=fs)
    
    return num, den

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
    if type(Wp) in [float, np.float, np.float16, np.float32, np.float64]:
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

    
def iirnotch(w0:float, bw:float)->Tuple:
    """
    Design second-order IIR notch digital filter.
    
    A notch filter is a band-stop filter with a narrow bandwidth 
    (high quality factor). 
    It rejects a narrow frequency band and leaves the rest of the spectrum 
    little changed.
    
    Caution : This function is not supported variable magnitude response.
    
    Parameters
    ----------
    w0 : float
        Notch frequency, specified as a positive scalar in the range 
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
    num, den = signal.iirnotch(w0, Q, fs = 2.0);
    
    return num, den

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    
    n, Wn = buttord([60/500, 200/500], [50/500, 250/500], 1, 40)
    num, den = butter(n, Wn)
    x = signal.freqz(num, den, worN = None, fs = 2.0)
    plt.plot(x[0], np.abs(x[1]))
    
    
    n, Wp = cheb1ord([60/500, 200/500], [50/500, 250/500], 1, 40)
    num, den = cheby1(n, 1, Wp)
    x = signal.freqz(num, den, worN = None, fs = 2.0)
    plt.figure()
    plt.plot(x[0], np.abs(x[1]))
    
    
    n, Ws = cheb2ord([60/500, 200/500], [50/500, 250/500], 1, 40)
    num, den = cheby2(n, 40, Ws)
    x = signal.freqz(num, den, worN = None, fs = 2.0)
    plt.figure()
    plt.plot(x[0], np.abs(x[1]))
    
    n, Wp = ellipord([60/500, 200/500], [50/500, 250/500], 1, 40)
    num, den = ellip(n, 1, 40, Wp)
    x = signal.freqz(num, den, worN = None, fs = 2.0)
    plt.figure()
    plt.plot(x[0], np.abs(x[1]))