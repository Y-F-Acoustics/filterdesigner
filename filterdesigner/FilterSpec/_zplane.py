import scipy.signal as signal
import warnings
import scipy as sp
import numpy as np
from typing import List, Tuple
import sys

def zplane(system, show:bool=True, figsize:Tuple[int, int]=(8, 8)):
    """
    Zero-pole plot of a digital filter.
    
    Parameters
    ----------
        system : a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)
                
        show : bool, optional
            If True, a zero-pole plot of the digital filter is shown 
            by matplorlib.pyplot.
            Default is True.
            
        figsize : tuple, optional
            If show is True, you can set the figure size of zero-pole plot.
            Default is (8, 8)
            
    Returns
    -------
        z : array_like
            Zeros of a digital filter.
            
        p : array_like
            Poles of a digital filter.
            
        k : array_like
            Gain of a digital filter.
    """
    b = system[0]
    a = system[1]

    #The coefficients are less than 1, normalize the coefficients
    if np.max(b) > 1:
        kn = np.max(b)
        b /= float(kn)
    else:
        kn = 1
    
    if np.max(a) > 1:
        kd = np.max(a)
        a /= float(kd)
    else:
        kd = 1

    # Get the poles, zeros and gains
    p = np.round(np.roots(a), decimals=2)
    z = np.round(np.roots(b), decimals=2)
    k = kn / float(kd)
    
    if show == True:
        plt.figure(figsize=figsize)
        ax = plt.subplot(111)
        uc = patches.Circle((0, 0), radius=1, fill=False,
                            color='black', ls='dashed')
        ax.add_patch(uc)
        plt.plot(z.real, z.imag, 'go', ms=10)
        plt.plot(p.real, p.imag, 'rx', ms=10)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        r = 1.5
        plt.axis('scaled')
        plt.axis([-r, r, -r, r])
        ticks = [-1, -.5, .5, 1]
        plt.xticks(ticks)
        plt.yticks(ticks)

    return z, p, k
    