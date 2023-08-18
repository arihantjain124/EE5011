from matplotlib.pyplot import semilogy
from pylab import *
import numpy as np
from scipy import special as sp
from scipy import integrate
import romberg as r
import math

def func(x):
    return 0.08046*math.exp(-1.2*x)

plt.clf()
figure(1)
x=np.arange(15,21,1)
y=[func(i) for i in x]
semilogy(x,y)
xlabel("Value of a")
ylabel("Value of f(a)")
grid(True)
figure(1).savefig("q1_3.jpg")