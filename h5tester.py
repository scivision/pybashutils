#!/usr/bin/env python
"""
recursive list of hdf5 file contents
can also simply in Terminal type:   h5ls -r myFile.h5
this is just an example of traversing the h5 contents, it may not be useful
in and of itself.
Michael Hirsch 2014

Note that if a CHUNK is corrupted AND fletcher32 is enabled for that variable, an attempt to read that chunk will raise an error:
visititems: RuntimeError
f[variable]: OSError either Can't read data (Wrong b-tree signature) or Can't read data (Inflate() failed)

That is, the only way to check an HDF5 file for corruption is to read every chunk of the file. We do that with .value
"""
from pathlib import Path
from sys import stderr
import h5py

VERBOSE=False

def checkh5(fn,var=None):
    fn = Path(fn).expanduser()
    assert fn.is_file(),f'{fn} is not a file'

    try:
        with h5py.File(fn,'r',libver='latest') as f:
            f.visititems(h5print)
    except RuntimeError as e:
        print(f'Error reading {fn}',file=stderr)
        if var:
            testh5var(var)

def h5print(name, obj):

    if isinstance(obj,h5py.Dataset):
        if VERBOSE:
            print('{name}: {obj.dtype}  {obj.shape}')
    elif isinstance(obj,h5py.Group):
        obj.visititems(h5print)

def testh5var(var):
    print('checking',var)
    with h5py.File(p.fn,'r',libver='latest') as f:
        print(f[var].fletcher32)
        print(f[var].chunks)
        print(f[var].shape)
        Nframe = f[var].shape[0]  # my files are Nframe x Y x X and are chunked (1, Y, X)
        for i in range(Nframe):
            try:
                f[var][i]
                if not i % 100:
                    print(i)
            except OSError as e:
                print(i,e,file=stderr)

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('fn',help='path to glob or HDF5 filename')
    p.add_argument('var',help='variable to check on error',nargs='?')
    p.add_argument('-v','--verbose',action='count',default=0)
    p = p.parse_args()

    flist = Path(p.fn)
    if flist.is_dir():
        flist = flist.glob('*.h5')
    elif flist.is_file():
        flist = [flist]
    else:
        raise IOError(f'What is {flist}. It is not a path or file.')

    for fn in flist:
        checkh5(fn,p.var)
