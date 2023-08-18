
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


plt.clf()
figure(1)
err=[]
err2=[]
counts=[]
for i in range(4,21):
    x1=linspace(0,1,2**(i-1))
    counts.append(2**(i-1))
    y1=[integral(i) for i in x1]
    tck1=si.splrep(x1,y1)
    I1=si.splint(0,1,tck1)
    x2=linspace(1,20,2**(i-1))
    y2=[integral(i) for i in x2]
    tck2=si.splrep(x2,y2)
    I2=si.splint(1,20,tck2)
    err.append(abs(I1+I2-exact()))


loglog(counts,err,'r')

grid(True)
figure(1).savefig("q7_2.jpg")
counts=[]
for i in range(4,21):
    x=linspace(0,20,2**i)
    counts.append(2**(i))
    y=[integral(i) for i in x]
    tck=si.splrep(x,y)
    I=si.splint(0,20,tck)
    err2.append(abs(I-exact()))


    
loglog(counts,err2,'g')
legend(["Split Integration","Non-split integration"])
xlabel("Number of points")
ylabel("log(absolute error)")
grid(True)
figure(1).savefig("q7_1.jpg")