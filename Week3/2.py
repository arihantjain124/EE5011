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

fx_t=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xx]

d=[xa[0],xa[-1]]

fx_1=[(-1*(   ((w**special.j0(w))*    ((-100*(w**3))+(2*((100*(w**3))-(100*(w**2))+w-1)*special.j0(w))-((2*((100*(w**3))-(100*(w**2)) +w-1)*w*np.log(w)*special.j1(w))+w-2)))))/(2*(((-100*(w**3))+(100*(w**2)) -w+1)**1.5)) for w in d]

y2a=spline.spline(xa,fx,fx_1[0],fx_1[1])
yyb=spline.splintn(xa,fx,y2a,xx)
y2a[0]=y2a[-1]=0
yyc=spline.splintn(xa,fx,y2a,xx)

y2a[0]= ((xa[2]-xa[0])*y2a[1])/(xa[2]-xa[1])+((xa[0]-xa[1])*y2a[2])/(xa[2]-xa[1])
y2a[-1]=((xa[-3]-xa[-1])*y2a[-2])/(xa[-3]-xa[-2])+((xa[-1]-xa[-2])*y2a[-3])/(xa[-3]-xa[-2])
yyd=spline.splintn(xa,fx,y2a,xx)

figure(1)
figure(1).clf()
semilogy(xx,abs(yyc-yyb))
grid(True)
figure(1).savefig("Error_plot_2.jpg")

figure(2)
figure(2).clf()
semilogy(xx,abs(yyd-yyb))
grid(True)
figure(2).savefig("Error_plot_3.jpg")