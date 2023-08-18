
from os import system
from matplotlib.pyplot import semilogy
from pylab import *
import spline
import numpy as np
from scipy import special


def fn(w):
    return (w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3))))

def fn_1(w):
    return (-1*(((w**special.j0(w))*((-100*(w**3))+(2*((100*(w**3))-(100*(w**2))+w-1)*special.j0(w))-((2*((100*(w**3))-(100*(w**2)) +w-1)*w*np.log(w)*special.j1(w))+w-2)))))/(2*(((-100*(w**3))+(100*(w**2)) -w+1)**1.5))

def deri1(x):
    y=0.0
    y=-(((x**special.j0(x))*(-100*x**3 + 2*(100*x**3 - 100*x**2 + x-1)*special.j0(x) - (2*(100*x**3 - 100*x**2 + x-1)*x*math.log10(x)*special.j1(x)) +x-2))/(2*(-100*x**3 + 100*x**2 -x +1)**1.5))
    return y

xa=np.arange(0.1,0.9005,0.05)
xx=np.arange(0.1,0.9001,0.001)
fx=[fn(w) for w in xa]
fx_t=[fn(w) for w in xx]
d=[0.1,0.9]
fx_1=[deri1(w) for w in d]
y2b=spline.splinenak(xa,fx)

yyb=spline.splintn(xa,fx,y2b,xx)