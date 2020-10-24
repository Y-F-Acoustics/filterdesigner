import scipy.signal as signal
from typing import Tuple

def tf2zpk(system:Tuple)->Tuple:
    """
    Convert transfer function filter parameters to zero-pole-gain form

    Inputs
    ------
        system :a tuple of array_like describing the system.
            The following gives the number of elements in the tuple and
            the interpretation:
                
                * (num, den)

    
    Returns
    -------
        z :np.ndarray
            Zeros of the transfer function.

        p :np.ndarray
            Poles of the transfer function.

        k :float
            system gain
    """

    z, p, k = signal.tf2zpk(system[0], system[1])

    return z, p, k