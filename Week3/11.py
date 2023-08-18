from matplotlib.pyplot import semilogy
from pylab import *
from os import system
import spline
import numpy as np
from scipy import special
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def bisection(array,value):
    n = len(array)
    if (value < array[0]):
        return -1
    elif (value > array[n-1]):
        return n
    jl = 0
    ju = n-1
    while (ju-jl > 1):
        jm=(ju+jl) >> 1
        if (value >= array[jm]):
            jl=jm
        else:
            ju=jm
    if (value == array[0]):
        return 0
    elif (value == array[n-1]):
        return n-2
    else:
        return jl

def bi_lin_interpolation(idx_x,idx_y,x,yy):
    den=(h[idx_x]-h[idx_x+1])*(h[idx_y]-h[idx_y+1])
    a=y[idx_x][idx_y]*(x-h[idx_x+1])*(yy-h[idx_y+1])
    b=y[idx_x+1][idx_y]*(h[idx_x]-x)*(yy-h[idx_y+1])
    c=y[idx_x][idx_y+1]*(x-h[idx_x+1])*(h[idx_y]-yy)
    d=y[idx_x+1][idx_y+1]*(h[idx_x]-x)*(h[idx_y]-yy)
    return (a+b+c+d)/den

plt.close()
plt.clf()

n=40
y=np.zeros([n,n])
h=np.linspace(0,2,n)
xx=np.linspace(0,2,n)
yy=np.linspace(0,2,n)
X,Y=np.meshgrid(xx,yy)
y=np.sin(np.pi*X)*np.cos(np.pi*Y)

N=80
xx=np.linspace(0,2,N)
yy=np.linspace(0,2,N)
res=np.zeros([N,N])
for i in range(N):
    for j in range(N):
        res[i][j]=bi_lin_interpolation(bisection(h,xx[i]),bisection(h,yy[j]),xx[i],yy[j])



X, Y = np.meshgrid(xx,yy)
fig = plt.figure()
ax = fig.add_subplot(121)
ax.matshow(res, cmap="jet")
ax = fig.add_subplot(122,projection='3d')
ax.plot_surface(X, Y, res, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('2-D Interpolation Surface Plot')
plt.savefig("q8_2_plot_1.jpg")
plt.clf()
plt.close()


Z=np.sin(np.pi*X)*np.cos(np.pi*Y)
fig = plt.figure()
ax = fig.add_subplot(121)
ax.matshow(Z, cmap="jet")
ax = fig.add_subplot(122,projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('True function Surface Plot')
plt.savefig("q8_2_plot_2.jpg")
plt.clf()
plt.close()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, abs(Z-res), rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('Error Plot')
plt.savefig("q8_2_plot_error_prof.jpg")
plt.clf()
plt.close()


pnt=0
err=[]
till=
for i in range(20,till,10):
    n=i
    y=np.zeros([n,n])
    h=np.linspace(0,2,n)
    xx=np.linspace(0,2,n)
    yy=np.linspace(0,2,n)
    X,Y=np.meshgrid(xx,yy)
    y=np.sin(np.pi*X)*np.cos(np.pi*Y)
    print(i)
    N=i*10
    xx=np.linspace(0,2,N)
    yy=np.linspace(0,2,N)
    res=np.zeros([N,N])
    for i in range(N):
        for j in range(N):
            res[i][j]=bi_lin_interpolation(bisection(h,xx[i]),bisection(h,yy[j]),xx[i],yy[j])
    X,Y=np.meshgrid(xx,yy)
    fx_true=np.sin(np.pi*X)*np.cos(np.pi*Y)
    err.append(max(((abs(fx_true-res)).reshape(N*N))))
    
plt.clf()
figure(1)
semilogy(range(20,till,10),err)
legend(["Max Error"])
grid(True)
figure(1).savefig("q8_2_plot_error.jpg")



