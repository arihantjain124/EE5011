
from matplotlib.pyplot import semilogy
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
    global count
    count+=1
    if u<1.0:                                                     
        return func(u)
    else: 
        return func2(u)
err=[]
count=0
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

plt.clf()
figure(1)

s=0
count=1
counts=[]
err=[]
ans=exact()
for i in range(1,20):
    s=r.trapzd(integral,0,20,s,i)
    err.append(abs(s-ans))
    counts.append(count+math.pow(2,i-2))
    count=0
loglog(counts,err,'r')


counts=[]
err=[]
ans=exact()
for i in range(-1,-11,-1):
    temp=r.qromb(integral,0,20,10**i)
    err.append(abs(temp[1]))
    counts.append(temp[2])
loglog(counts,err,'g')

counts=[]
err=[]
ans=exact()
for i in range(-1,-11,-1):
    x1=r.qromb(integral,0,1,10**i)
    x2=r.qromb(integral,1,20,10**i)
    counts.append(x1[2]+x2[2])
    err.append(abs(x1[0]+x2[0]-exact()))
loglog(counts,err,'b')


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

loglog(counts,err,'y')

counts=[]
for i in range(4,21):
    x=linspace(0,20,2**i)
    counts.append(2**(i))
    y=[integral(i) for i in x]
    tck=si.splrep(x,y)
    I=si.splint(0,20,tck)
    err2.append(abs(I-exact()))

loglog(counts,err2,'black')

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

err2=[abs(exact()-x) for x in res]
counts=[1+(3**i)  for i in range(4,15)]

loglog(counts,err2,'cyan')

ylabel("Order of Error")
xlabel("Number of Function Calls")
legend(["Trapezoidal","Romberg","Romberg Split","B-spline Split","B-Spline","trap/3"])
grid(True)
figure(1).savefig("q13_2.jpg")