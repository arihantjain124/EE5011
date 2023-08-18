from matplotlib.pyplot import loglog
from pylab import *
import numpy as np
from scipy import special as sp
from scipy import integrate
import romberg as r
import math
count=0
def exact():
    return sp.jv(3,2.7)**2-sp.jv(4,2.7)*sp.jv(2,2.7)+abs(sp.jv(3,2.7)/sp.kv(3,1.2))**2*(sp.kv(4,1.2)*sp.kv(2,1.2)-sp.kv(3,1.2)**2)

def func(u):
    return 2*u*sp.jv(3,2.7*u)**2   

def func2(u):
    return 2*sp.kv(3,1.2*u)**2*u*abs(sp.jv(3,2.7)/sp.kv(3,1.2))**2

def integral(u):
    global count
    count+=1
    if u<1.0:                                                     
        return func(u)
    else: 
        return func2(u)

order=6
s_out=0.0
xx=[]; yy=[]	

for j in range():

    for i in range(1,order+1):
        s_out=r.trapzd(integral,0,20,s_out,i)
        xx.append((20.0/(2**(i-1)))**2)
        yy.append(s_out)

    y.append(polint(xx,yy,0))	