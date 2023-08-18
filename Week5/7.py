import gauss_quad
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

def f3(u):
    return f2(u+1)*np.exp(u)

res=[0,0,0]
res[1]=integrate.quad(f1,0,1,epsabs=1e-12,epsrel=1e-12)

res[2]=integrate.quad(f2,1,np.inf,epsabs=1e-12,epsrel=1e-12,full_output=0)


x,w=gauss_quad.gauleg(0,1,10)

integral=0.0
for i in range(len(x)):
    integral+=f1(x[i])*w[i]
print (integral, integral-res[1][0])


x,w=gauss_quad.gaulag(120,0.0)
integral=0.0
for i in range(len(x)):
    integral+=f3(x[i])*w[i]
print (integral, integral-res[2][0])