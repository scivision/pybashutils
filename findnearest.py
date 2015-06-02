"""
This find_nearest function does NOT assume sorted input

inputs:
x: array (float, int, datetime) within which to search for x0
x0: singleton or array of values to search for in x

outputs:
idx: index of x nearest to x0
xidx: x[idx]

Observe how bisect.bisect() gives the incorrect result!

idea based on http://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array

Michael Hirsch
GPLv3+
"""
from numpy import empty_like,absolute,atleast_1d,asanyarray
from bisect import bisect

def find_nearest(x,x0):
    x = asanyarray(x) #for indexing upon return
    x0 = atleast_1d(x0)
    ind = empty_like(x0,dtype=int)

    for i,xi in enumerate(x0):
       ind[i] = absolute(x-xi).argmin()

    return ind.squeeze(), x[ind].squeeze()

def INCORRECTRESULT_using_bisect(x,X0): #pragma: no cover
    X0 = atleast_1d(X0)
    x.sort()
    ind = [bisect(x,x0) for x0 in X0]

    x = asanyarray(x)
    return asanyarray(ind),x[ind]

#if __name__ == '__main__': 

    #print(find_nearest([10,15,12,20,14,33],[32,12.01]))

    #print(INCORRECTRESULT_using_bisect([10,15,12,20,14,33],[32,12.01]))
