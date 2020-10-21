import scipy.io as io
import numpy as np
from typing import List, Tuple

def whosmat(filename:str, byte_order:str=None, matlab_compatible:bool=False)->list:
    """
    List variables inside a MATLAB file.
    
    Parameters
    ----------
    filename : str
        Name of the mat file. 
        Can also pass open file-like object.
        
    byte_order : str or None, optional
        None by default, implying byte order guessed from mat file. 
        Otherwise can be one of (‘native’, ‘=’, ‘little’, ‘<’, ‘BIG’, ‘>’).
        
    matlab_compatible : bool, optional
        Returns matrices as would be loaded by MATLAB.

    Returns
    -------
    variable : list of tuples
        A list of tuples, where each tuple holds the matrix name (a string), 
        its shape (tuple of ints), and its data class (a string). 
        Possible data classes are: int8, uint8, int16, uint16, int32, uint32, 
        int64, uint64, single, double, cell, struct, object, char, sparse, 
        function, opaque, logical, unknown.
    """
    
    # Remove other than '.mat' extension if filename has the other extention.
    if filename[-4:] != '.mat':
        if filename.find('.') != -1:
            bad_ext = filename[filename.find('.'):]
            print('Warning: Filename "'+filename+'" has a bad extension "'+bad_ext+'" .')
            
            filename = filename[0:filename.find('.')]
            print('Renamed to "'+filename+'.mat".')
            
        # Add '.mat' force.
        filename = filename + '.mat'
        
    variables = io.whosmat(filename, appendmat=False, byte_order=byte_order, 
                           matlab_compatible=matlab_compatible)
    
    return variables
    