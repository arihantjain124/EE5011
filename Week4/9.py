from matplotlib.pyplot import semilogy
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
for i in range(5,21,1):
    temp=r.qromb(integral,0,20,10**-8,i)
    err.append(abs(temp[1]))
    counts.append(temp[2])

plt.clf()
figure(1)
semilogy(range(5,21,1),counts)
xlabel("Order of Romberg Integration")
ylabel("Number of Function Calls")
grid(True)
figure(1).savefig("q5_1.jpg")