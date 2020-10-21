import scipy.io as io
import numpy as np
from typing import List, Tuple

def savemat(filename:str, mdict:dict, comp:bool=False, oned_as:str='row'):
    """
    Save variables as MATLAB-style .mat file.
    
    This saves the array objects in the given dictionary to a MATLAB- style .mat file.
    
    Parameters
    ----------
        filename : str
            Name of the .mat file. Can also pass open file_like object.
            
        mdict : dict
            Dictionary from which to save matfile variables.
            
        comp : bool, otional
            Whether or not to compress matrices on write. Default is False.
            
        oned_as : {'row', 'column'}, optional
            If ‘column’, write 1-D numpy arrays as column vectors. 
            If ‘row’, write 1-D numpy arrays as row vectors.
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
        
    # Save MATLAB-like .mat file
    io.savemat(filename, mdict, appendmat=False, long_field_names=True, 
               do_compression=comp, oned_as=oned_as)
    