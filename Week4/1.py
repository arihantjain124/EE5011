from matplotlib.pyplot import semilogy
from pylab import *
import numpy as np
from scipy import special as sp

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
x=np.logspace(-3,7,200)
y=[integral(i) for i in x]
semilogx(x,y)
xlabel("u")
ylabel("f(x)")
figure(1).savefig("q1.jpg")