import scipy.signal as signal
import warnings
import scipy as sp
import numpy as np
from typing import List, Tuple
import sys

def isstable(system)->bool:
    """
    Determine whether filter is stable.

    Parameters
    ----------
    system : a tuple of array_like describing the system.
        The following gives the number of elements in the tuple and
        the interpretation:
                
            * (num, den)
        
    Returns
    -------
    flag : bool
        If `system` is a stable filter, returns True.
        

    """
    _, p, _ = zplane(system, show=False)
    frag = np.max(np.abs(p)) - 1.0 <= (sys.float_info.epsilon ** (2/3))   
    
    return frag
    