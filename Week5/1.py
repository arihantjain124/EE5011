from scipy.special import jv
import numpy as np
import math
from pylab import *
from matplotlib.pyplot import semilogy

def integrand(x):
    return np.exp(-x)/jv(1,np.sqrt(-x**2+4*x-3))

eps=1e-6
x=np.linspace(1+eps,3-eps,1000)

plt.clf()
figure(1)
semilogy(x,integrand(x))

xlabel("X")
ylabel("F(x)")
grid(True)
figure(1).savefig("q1_1.jpg")
    
