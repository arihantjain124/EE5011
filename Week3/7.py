

from matplotlib.pyplot import semilogy
from pylab import *
from os import system
import spline
import numpy as np
from scipy import special


pnt=0
err=[]
fx_1=[0.117288,1.71855]
till=1200
for i in range(20,till,10):
    xa=np.linspace(0.1,0.9,i)
    fx=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xa]
    y2a=spline.spline(xa,fx,fx_1[0],fx_1[1])
    xx=np.linspace(0.1,0.9,i*10)
    yya=spline.splintn(xa,fx,y2a,xx)
    fx_true=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xx]
    if max(abs(yya-fx_true))<(10**-6) and pnt==0:
        pnt=i
        pnt_err=max(abs(yya-fx_true))
    err.append(max(abs(yya-fx_true)))


plt.clf()
figure(1)
semilogy(range(20,till,10),err,'r',pnt,pnt_err,'gx')
s="we get six digit accuracy at "+str(pnt)
legend(["Max Error",s])
grid(True)
figure(1).savefig("q5_plot_1.jpg")
xa=np.linspace(0.1,0.9,pnt)
fx=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xa]
y2a=spline.splinenak(xa,fx)
xx=np.linspace(0.1,0.9,pnt*10)
yya=spline.splintn(xa,fx,y2a,xx)
fx_true=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xx]

plt.clf()
figure(2)
semilogy(xx,abs(yya-fx_true),'r')
s="Error Profile at "+str(pnt)+" points"
legend([s])
grid(True)
figure(2).savefig("q5_plot_2.jpg")