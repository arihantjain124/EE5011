from matplotlib.pyplot import semilogy
from pylab import *
from os import system
import spline
import numpy as np
from scipy import special
pnt=0
err=[]
till=1000
for i in range(20,till,10):
    xa=np.linspace(0.1,0.9,i)
    fx=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xa]
    y2a=spline.splinenak(xa,fx)
    xx=np.linspace(0.1,0.9,i*10)
    yya=spline.splintn(xa,fx,y2a,xx)
    fx_1=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xx]
    if max(abs(yya-fx_1))<(10**-6) and pnt==0:
        pnt=i
        pnt_err=max(abs(yya-fx_1))
    err.append(max(abs(yya-fx_1)))


plt.clf()
figure(2)
semilogy(range(20,till,10),err,'r',pnt,pnt_err,'gx')
s="we get six digit accuracy at "+str(pnt)
legend(["Max Error",s])
grid(True)
figure(2).savefig("q4_plot_2.jpg")


xa=np.linspace(0.1,0.9,pnt)
fx=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xa]
y2a=spline.splinenak(xa,fx)
xx=np.linspace(0.1,0.9,pnt*10)
yya=spline.splintn(xa,fx,y2a,xx)
fx_1=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xx]

plt.clf()
figure(1)
semilogy(xx,abs(yya-fx_1),'r')
s="Error Profile at "+str(pnt)+" points"
legend([s])
grid(True)
figure(1).savefig("q4_plot_1.jpg")


