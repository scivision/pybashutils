from numpy.testing import assert_almost_equal
#%% findnearest
from findnearest import find_nearest
indf,xf = find_nearest([10,15,12,20,14,33],[32,12.01])
assert_almost_equal(indf,[5,2])
assert_almost_equal(xf,[33.,12.])

