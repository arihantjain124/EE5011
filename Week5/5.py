from scipy import integrate
from scipy.special import jv
import numpy as np
import sing_intg as si
import math
from pylab import *
from matplotlib.pyplot import loglog, semilogy


plt.clf()
figure(1)

def f(t):
    return np.exp(-t-2)*np.sqrt(1-t**2)/jv(1,np.sqrt(1-t**2))

def guassquad(x,w):
    sum=0.0
    for i in range(len(x)):
        sum+=f(x[i])*w[i]
    return sum

x=np.array(range(20))
x=np.cos(np.pi*(x-0.5)/20)
w=np.full(20,np.pi/20)
ans=guassquad(x,w)

errors=[]

for i in range(1,20):
    x=np.array(range(i))
    y=np.cos(np.pi*(x-0.5)/i)
    w=np.full(i,np.pi/i)
    temp=guassquad(y,w)
    errors.append(abs(temp-ans))

semilogy(range(1,20),errors)
xlabel("No. of points")
ylabel("Error")

grid() 
figure(1).savefig("q2_2.jpg")