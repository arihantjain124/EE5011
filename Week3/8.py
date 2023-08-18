

from matplotlib.pyplot import semilogy
from pylab import *
from os import system
import spline
import numpy as np
from scipy import special


xa=np.linspace(0.1,0.9,100)
fx=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xa]
fx_1=[0.117288,1.71855]
y2a=spline.spline(xa,fx,100*fx_1[0],100*fx_1[1])
xx=np.linspace(0.1,0.9,1000)
yya=spline.splintn(xa,fx,y2a,xx)
y2a=spline.spline(xa,fx,fx_1[0],fx_1[1])
yyb=spline.splintn(xa,fx,y2a,xx)
fx_true=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xx]


plt.clf()
figure(1)
figure(1).set_size_inches(10,8)
semilogy(xx,abs(yya-fx_true),'r')
semilogy(xx,abs(yyb-fx_true),'g')
legend(["100*y'","y'"])
grid(True)
figure(1).savefig("q6_plot_1.jpg")

plt.clf()
figure(2)
figure(2).set_size_inches(10,8)
semilogy(xx,abs(yya-fx_true)-abs(yyb-fx_true),'r')
grid(True)
figure(2).savefig("q6_plot_2.jpg")