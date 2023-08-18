from matplotlib.pyplot import loglog
from pylab import *
import numpy as np
from scipy import special as sp
from scipy import integrate
import romberg as r
import math
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

counts=[]
err=[]
ans=exact()
for i in range(-1,-11,-1):
    x1=r.qromb(integral,0,1,10**i)
    x2=r.qromb(integral,1,20,10**i)
    counts.append(x1[2]+x2[2])
    err.append(abs(x1[0]+x2[0]-exact()))

plt.clf()
figure(1)
loglog(counts,err)
ylabel("Order of Error")
xlabel("Number of Function Calls")
grid(True)
figure(1).savefig("q4_1.jpg")
