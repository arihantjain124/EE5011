
from matplotlib.pyplot import semilogy
from pylab import *
import numpy as np
from scipy import special as sp
from scipy import integrate
import romberg as r
import math
import scipy.interpolate as si

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
err=[]
def trap3(func, a, b, n):
    if(n==1):
        return 0.5*(b-a)*(func(a)+func(b))
    else:
        d = (float)(b-a)/3**(n-1)
        sum=0.0
        x=a+d
        while(x<b):
            sum+=func(x)*d; x+=d;
        sum+=0.5*d*(func(a)+func(b))
        return sum
xx=[]; yy=[]


order=12


for i in range(1,order+1):
    xx.append((20.0/3**(i-1)**2))
    yy.append(trap3(integral,0,20,i))
y,err=r.polint(xx,yy,0)

res=[0.028308865452234523,
 0.051010088463658725,
 0.04623041853121219,
 0.04599729132190436,
 0.046035384924641265,
 0.046039619586256776,
 0.046038888020235834,
 0.04603885392364227,
 0.0460388597483749,
 0.04603886039557746,
 0.046038860284213286]