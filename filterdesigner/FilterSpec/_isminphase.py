import scipy.signal as signal
from ._zplane import zplane
import warnings
import scipy as sp
import numpy as np
from typing import List, Tuple
import sys

def isminphase(system, tol:float=sys.float_info.epsilon**(2/3))->bool:
    """
    Determine whether is minimum phase.

    Parameters
    ----------
    system : a tuple of array_like describing the system.
        The following gives the number of elements in the tuple and
        the interpretation:
                
            * (num, den)

    Returns
    -------
    flag : bool
        If `system` is minimum phase, return True.

    """
    z, _, _ = zplane(system, show=False)
    frag = np.max(np.abs(z)) <= 1.0 - tol
    
    return frag
    