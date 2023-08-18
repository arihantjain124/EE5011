from scipy import integrate
from scipy.special import jv
import numpy as np
import math
from pylab import *
from matplotlib.pyplot import semilogy

def integrand(x):
    return np.exp(-x)/jv(1,np.sqrt(-x**2+4*x-3))
res=integrate.quad(integrand,1,3,full_output=1)
print (res[0])
print (res[1])
print (res[2]["neval"])