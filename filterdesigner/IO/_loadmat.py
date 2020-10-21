import scipy.io as io
import numpy as np
from typing import List, Tuple

def loadmat(filename:str, mdict:dict, byte_order:str=None, 
            matlab_compatible:bool=False, verify_compressed_data_integrity:bool=True, 
            variable_names=None)->dict:
    
    """
    Load MATLAB file.
    
    Parameters
    ----------
        filename : str
            Name of the mat file. 
            Can also pass open file-like object.
        
        mdict : dict
            Dictionary in which to insert matfile variables.
        
        byte_order : str or None, optional
            None by default, implying byte order guessed from mat file. 
            Otherwise can be one of (‘native’, ‘=’, ‘little’, ‘<’, ‘BIG’, ‘>’).
        
        matlab_compatible : bool, optional
            Returns matrices as would be loaded by MATLAB.
        
        verify_compressed_data_integrity : bool, optional
            Whether the length of compressed sequences in the MATLAB file 
            should be checked, to ensure that they are not longer than we expect. 
            It is advisable to enable this (the default) because overlong 
            compressed sequences in MATLAB files generally indicate that the 
            files have experienced some sort of corruption.
        
        variable_names : None or sequence, optional
            If None (the default) - read all variables in file. 
            Otherwise variable_names should be a sequence of strings, 
            giving names of the MATLAB variables to read from the file. 
            The reader will skip any variable with a name not in this sequence,
            possibly saving some read processing.
            
            
    Returns
    -------
        mat_dict : dict
            dictionary with variable names as keys, and loaded matrices as 
            values.
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
        
    # Load MATLAB-like .mat file
    mat_dict = io.loadmat(filename, mdict, appendmat=False, byte_order=byte_order, 
                          matlab_compatible=matlab_compatible, 
                          verify_compressed_data_integrity=verify_compressed_data_integrity, 
                          variable_names=variable_names)
    
    return mat_dict
    