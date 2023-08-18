from matplotlib.pyplot import semilogy
from pylab import *
import numpy as np
from scipy import special as sp
from scipy import integrate

def exact():
    return sp.jv(3,2.7)**2-sp.jv(4,2.7)*sp.jv(2,2.7)+abs(sp.jv(3,2.7)/sp.kv(3,1.2))**2*(sp.kv(4,1.2)*sp.kv(2,1.2)-sp.kv(3,1.2)**2)

def integral(u):
    if u<1.0:                                                     
        return 2*u*sp.jv(3,2.7*u)**2 
    else: 
        return 2*sp.kv(3,1.2*u)**2*u*abs(sp.jv(3,2.7)/sp.kv(3,1.2))**2
print(integrate.quad(integral,0,20,full_output=1)[0])
print(integrate.quad(integral,0,20,full_output=1)[0]-exact())
print(integrate.quad(integral,0,20,full_output=1)[2]['neval'])