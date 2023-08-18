from matplotlib.pyplot import semilogy
from pylab import *
from os import system
import spline
import numpy as np
from scipy import special

plt.clf()
xa=np.arange(0.1,0.9,0.005)
xx=np.arange(0.1,0.9,0.001)
fx=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xa]
d=[xa[0],xa[-1]]
fx_1=[(-1*(   ((w**special.j0(w))*    ((-100*(w**3))+(2*((100*(w**3))-(100*(w**2))+w-1)*special.j0(w))-((2*((100*(w**3))-(100*(w**2)) +w-1)*w*np.log(w)*special.j1(w))+w-2)))))/(2*(((-100*(w**3))+(100*(w**2)) -w+1)**1.5)) for w in d]

y2a=spline.spline(xa,fx,fx_1[0],fx_1[1])
'''
figure(1)
plot(xa,fx,'r')
legend(["fx"])
grid(True)
figure(1).savefig("q1_plot_1.jpg")'''



yyb=spline.splintn(xa,fx,y2a,xx)
plt.clf()
figure(2)
plot(xx,yyb,'g',xa,fx,'r')
legend(["True Function"])
grid(True)
figure(2).savefig("q1_plot_1.jpg")




