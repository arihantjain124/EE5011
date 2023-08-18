

from matplotlib.pyplot import semilogy
from pylab import *
from os import system
import spline
import numpy as np
from scipy import special


pnt=0
err=[]
fx_1=[0.117288,1.71855]
till=1000
h=np.linspace(0.1,0.9,5)
parts=10
for i in range(20,till,10):
    xa=np.concatenate([np.linspace(0.1,h[2],int(3*i/parts),endpoint=False),np.linspace(h[2],h[3],int(2*i/parts),endpoint=False),np.linspace(h[3],h[-1],int(5*i/parts))])
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
figure(1).savefig("q7_1_plot_1.jpg")

i=pnt
xa=np.concatenate([np.linspace(0.1,h[2],int(3*i/parts),endpoint=False),np.linspace(h[2],h[3],int(2*i/parts),endpoint=False),np.linspace(h[3],h[-1],int(5*i/parts))])
fx=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xa]
y2a=spline.spline(xa,fx,fx_1[0],fx_1[1])
xx=np.linspace(0.1,0.9,i*10)
yya=spline.splintn(xa,fx,y2a,xx)
fx_true=[(w**(1+special.j0(w)))/(np.sqrt(1-w+(100*(w**2))-(100*(w**3)))) for w in xx]

plt.clf()
figure(1)
semilogy(xx,abs(yya-fx_true),'r')
legend(["Error Profile"])
grid(True)
figure(1).savefig("q7_1_plot_2.jpg")