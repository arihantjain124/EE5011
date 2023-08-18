from matplotlib.pyplot import semilogy
from pylab import *
from os import system
import spline
import numpy as np
from scipy import special

def fn(w):
    return (w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3))))

def fn_1(w):
    return (-1*(((w**special.j0(w))*((-100*(w**3))+(2*((100*(w**3))-(100*(w**2))+w-1)*special.j0(w))-((2*((100*(w**3))-(100*(w**2)) +w-1)*w*np.log(w)*special.j1(w))+w-2)))))/(2*(((-100*(w**3))+(100*(w**2)) -w+1)**1.5))

xa=np.arange(0.1,0.9,0.005)
xx=np.arange(0.1,0.9,0.001)
fx=[fn(w) for w in xa]
fx_t=[fn(w) for w in xx]
d=[xa[0],xa[-1]]
fx_1=[fn_1(w) for w in d]
y2a=spline.spline(xa,fx,fx_1[0],fx_1[1])