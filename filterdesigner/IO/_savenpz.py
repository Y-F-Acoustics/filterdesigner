import scipy.io as io
import numpy as np
from typing import List, Tuple

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
    