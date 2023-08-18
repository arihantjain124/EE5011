import scipy.special as sp
from scipy import integrate
from scipy.special import jv
import numpy as np
import sing_intg as si
import math
from pylab import *
from matplotlib.pyplot import loglog

def f1(u):
    return u*sp.jv(3,2.7*u)**2

def f2(u):
    return u*sp.kv(3,1.2*u)**2

print(integrate.quad(f1,0,1,epsabs=1e-12,epsrel=1e-12,full_output=0))
print(integrate.quad(f2,1,np.inf,epsabs=1e-12,epsrel=1e-12,full_output=0))