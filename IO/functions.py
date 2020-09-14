# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:22:27 2020

@author: yuki1
"""


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


def savenpy(filename:str, arr:np.array, allow_pickle=True, fix_imports=True):

    """
    Save an array to a binary file in NumPy ``.npy`` format.

    Parameters
    ----------
    file : file, str, or pathlib.Path
        File or filename to which the data is saved.  If file is a file-object,
        then the filename is unchanged.  If file is a string or Path, a ``.npy``
        extension will be appended to the filename if it does not already
        have one.
    
    arr : array_like
        Array data to be saved.
    
    allow_pickle : bool, optional
        Allow saving object arrays using Python pickles. Reasons for disallowing
        pickles include security (loading pickled data can execute arbitrary
        code) and portability (pickled objects may not be loadable on different
        Python installations, for example if the stored objects require libraries
        that are not available, and not all pickled data is compatible between
        Python 2 and Python 3).
        Default: True
    
    fix_imports : bool, optional
        Only useful in forcing objects in object arrays on Python 3 to be
        pickled in a Python 2 compatible way. If `fix_imports` is True, pickle
        will try to map the new Python 3 names to the old module names used in
        Python 2, so that the pickle data stream is readable with Python 2.
    
    
    See Also
    --------
    savez : Save several arrays into a ``.npz`` archive
    savetxt, load
    
    
    Notes
    -----
    For a description of the ``.npy`` format, see :py:mod:`numpy.lib.format`.
    Any data saved to the file is appended to the end of the file.
    
    
    Examples
    --------
    >>> from tempfile import TemporaryFile
    >>> outfile = TemporaryFile()
    >>> x = np.arange(10)
    >>> np.save(outfile, x)
    >>> _ = outfile.seek(0) # Only needed here to simulate closing & reopening file
    >>> np.load(outfile)
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> with open('test.npy', 'wb') as f:
    ...     np.save(f, np.array([1, 2]))
    ...     np.save(f, np.array([1, 3]))
    >>> with open('test.npy', 'rb') as f:
    ...     a = np.load(f)
    ...     b = np.load(f)
    >>> print(a, b)
    # [1 2] [1 3]
    """
        
    # Remove other than '.npy' extension if filename has the other extention.
    if filename[-4:] != '.npy':
        if filename.find('.') != -1:
            bad_ext = filename[filename.find('.'):]
            print('Warning: Filename "'+filename+'" has a bad extension "'+bad_ext+'" .')

            filename = filename[0:filename.find('.')]
            print('Renamed to "'+filename+'.npy".')
            
        # Add '.npy' force.
        filename = filename + '.npy'

    np.save(filename, arr, allow_pickle, fix_imports)


def savenpz(filename:str, *args, **kwds):
    
    """
    Save several arrays into a single file in uncompressed ``.npz`` format.
    If arguments are passed in with no keywords, the corresponding variable
    names, in the ``.npz`` file, are 'arr_0', 'arr_1', etc. If keyword
    arguments are given, the corresponding variable names, in the ``.npz``
    file will match the keyword names.
    
    Parameters
    ----------
    file : str or file
        Either the filename (string) or an open file (file-like object)
        where the data will be saved. If file is a string or a Path, the
        ``.npz`` extension will be appended to the filename if it is not
        already there.
    
    args : Arguments, optional
        Arrays to save to the file. Since it is not possible for Python to
        know the names of the arrays outside `savez`, the arrays will be saved
        with names "arr_0", "arr_1", and so on. These arguments can be any
        expression.
    
    kwds : Keyword arguments, optional
        Arrays to save to the file. Arrays will be saved in the file with the
        keyword names.
    
    
    Returns
    -------
    None
    
    
    See Also
    --------
    save : Save a single array to a binary file in NumPy format.
    savetxt : Save an array to a file as plain text.
    savez_compressed : Save several arrays into a compressed ``.npz`` archive
    
    
    Notes
    -----
    The ``.npz`` file format is a zipped archive of files named after the
    variables they contain.  The archive is not compressed and each file
    in the archive contains one variable in ``.npy`` format. For a
    description of the ``.npy`` format, see :py:mod:`numpy.lib.format`.
    When opening the saved ``.npz`` file with `load` a `NpzFile` object is
    returned. This is a dictionary-like object which can be queried for
    its list of arrays (with the ``.files`` attribute), and for the arrays
    themselves.
    When saving dictionaries, the dictionary keys become filenames
    inside the ZIP archive. Therefore, keys should be valid filenames.
    E.g., avoid keys that begin with ``/`` or contain ``.``.
    
    
    Examples
    --------
    >>> from tempfile import TemporaryFile
    >>> outfile = TemporaryFile()
    >>> x = np.arange(10)
    >>> y = np.sin(x)
    Using `savez` with \\*args, the arrays are saved with default names.
    >>> np.savez(outfile, x, y)
    >>> _ = outfile.seek(0) # Only needed here to simulate closing & reopening file
    >>> npzfile = np.load(outfile)
    >>> npzfile.files
    ['arr_0', 'arr_1']
    >>> npzfile['arr_0']
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    Using `savez` with \\**kwds, the arrays are saved with the keyword names.
    >>> outfile = TemporaryFile()
    >>> np.savez(outfile, x=x, y=y)
    >>> _ = outfile.seek(0)
    >>> npzfile = np.load(outfile)
    >>> sorted(npzfile.files)
    ['x', 'y']
    >>> npzfile['x']
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    """

    # Remove other than '.npz' extension if filename has the other extention.
    if filename[-4:] != '.npz':
        if filename.find('.') != -1:
            bad_ext = filename[filename.find('.'):]
            print('Warning: Filename "'+filename+'" has a bad extension "'+bad_ext+'" .')

            filename = filename[0:filename.find('.')]
            print('Renamed to "'+filename+'.npz".')
            
        # Add '.npz' force.
        filename = filename + '.npz'

    np.savez(filename, *args, **kwds)


if __name__ == '__main__':
    from os.path import dirname, join as pjoin
    
    # savemat
    a = np.arange(20)
    mdic = {"a": a, "label": "experiment"}
    savemat("./matlab_matrix.mat", mdic)

    # loadmat
    mdic2 = loadmat("./matlab_matrix.mat")

    # whosmat
    x = whosmat("./matlab_matrix.mat")

    # savenpy
    b = np.arange(30)
    savenpy("./numpy_matrix.npy", b)

    # savenpz
    savenpz("./numpy_matrixs.npz", a, b)