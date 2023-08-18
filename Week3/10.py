from matplotlib.pyplot import semilogy
from pylab import *
from os import system
import numpy as np
from scipy import special
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import spline

plt.close()
plt.clf()
n=20
y=np.zeros([n,n])
y_2=np.zeros([n,n])
h=np.linspace(0,2,n)
for i in range(n):
    for j in range(n):
        y[i][j]=(np.sin(np.pi*h[i])*np.cos(np.pi*h[j]))
        y_2[i][j]=(-1*(np.pi**2))*np.sin(np.pi*h[i])*np.cos(np.pi*h[j])

N=80
temp=np.zeros(n)
y2a=np.zeros(n)
xx=np.linspace(0,2,N)
yy=np.linspace(0,2,N)
y2a=np.zeros(n)
res=np.zeros([N,N])
for i in range(N):
    for k in range(n):
            temp[k]=spline.splint(h,y[k],y_2[k],xx[i])
            y2a=spline.splinenak(h,temp)
    for j in range(N):
        res[i][j]=spline.splint(h,temp,y2a,yy[j])
        
X, Y = np.meshgrid(xx,yy)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, res, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('2-D Interpolation Surface Plot');
plt.savefig("q8_plot_1.jpg")
plt.clf()
plt.close()

fig = plt.figure()
ax = plt.axes(projection='3d')
Z=np.sin(np.pi*X)*np.cos(np.pi*Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('True function Surface Plot');
plt.savefig("q8_plot_2.jpg")
plt.clf()
plt.close()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, abs(Z-res), rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('Error Plot');
plt.savefig("q8_plot_error_cubic.jpg")
plt.clf()
plt.close()

pnt=0
err=[]
till=200
for i in range(20,till,10):
    n=i
    y=np.zeros([n,n])
    y_2=np.zeros([n,n])
    h=np.linspace(0,2,n)
    for i in range(n):
        for j in range(n):
            y[i][j]=(np.sin(np.pi*h[i])*np.cos(np.pi*h[j]))
            y_2[i][j]=(-1*(np.pi**2))*np.sin(np.pi*h[i])*np.cos(np.pi*h[j])
    N=i*10
    print(i)
    temp=np.zeros(n)
    y2a=np.zeros(n)
    xx=np.linspace(0,2,N)
    yy=np.linspace(0,2,N)
    y2a=np.zeros(n)
    res=np.zeros([N,N])
    for i in range(N):
        for k in range(n):
                temp[k]=spline.splint(h,y[k],y_2[k],xx[i])
                y2a=spline.splinenak(h,temp)
        for j in range(N):
            res[i][j]=spline.splint(h,temp,y2a,yy[j])
    X,Y=np.meshgrid(xx,yy)
    fx_true=np.sin(np.pi*X)*np.cos(np.pi*Y)
    err.append(max(((abs(fx_true-res)).reshape(N*N))))
    
plt.clf()
figure(1)
semilogy(range(20,till,10),err)
legend(["Max Error"])
grid(True)
figure(1).savefig("q8_2_plot_error_cubic.jpg")