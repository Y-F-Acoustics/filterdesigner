import scipy.io as io
import numpy as np
from typing import List, Tuple

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
    