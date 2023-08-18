
from matplotlib.pyplot import loglog
from pylab import *
import numpy as np
from scipy import special as sp
from scipy import integrate
import romberg as r
import math
import scipy.interpolate as si
def exact():
    return sp.jv(3,2.7)**2-sp.jv(4,2.7)*sp.jv(2,2.7)+abs(sp.jv(3,2.7)/sp.kv(3,1.2))**2*(sp.kv(4,1.2)*sp.kv(2,1.2)-sp.kv(3,1.2)**2)

def func(u):
    return 2*u*sp.jv(3,2.7*u)**2   

def func2(u):
    return 2*sp.kv(3,1.2*u)**2*u*abs(sp.jv(3,2.7)/sp.kv(3,1.2))**2

def integral(u):
    if u<1.0:                                                     
        return func(u)
    else: 
        return func2(u)
err=[]
counts=[]
for i in range(4,21):
    x=linspace(0,20,2**i)
    counts.append(2**i)
    y=[integral(i) for i in x]
    tck=si.splrep(x,y)
    I=si.splint(0,20,tck)
    err.append(abs(I-exact()))

plt.clf()
figure(1)
loglog(counts,err)
xlabel("Number of points")
ylabel("log(absolute error)")
grid(True)
figure(1).savefig("q6_1.jpg")