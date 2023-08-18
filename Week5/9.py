import romberg as r
import gauss_quad
import scipy.special as sp
from scipy import integrate
from scipy.special import jv
import numpy as np
import sing_intg as si
import math
from pylab import *
from matplotlib.pyplot import loglog, semilogy


def f1(u):
    return u*sp.jv(3,2.7*u)**2


def f2(u):
    return u*sp.kv(3,1.2*u)**2

def both(x):
    if x<1:
        return f1(x)
    else:
        return f2(x)
x=np.linspace(0.1,10,10)
y=[both(i) for i in x]

plt.clf()
figure(1)
semilogy(x,y)

xlabel("X")
ylabel("F(x)")
grid(True)
figure(1).savefig("q3_1.jpg")