import polint
import math
import numpy as np
import matplotlib.pyplot as plt

def locate(x,q,n):
    x = np.asarray(x)
    idx = (np.abs(x - q)).argmin()
    if idx-n//2<1:
        return x[0:n]
    elif idx+n//2>len(x):
        return x[-n:]
    return x[idx-n//2:idx+n//2+1]


def sinlocate(x,q,n):
    x = np.asarray(x)
    idx = (np.abs(x - q)).argmin()
    if idx-n//2<1:
        return sinx[0:n]
    elif idx+n//2>len(x):
        return sinx[-n:]
    return sinx[idx-n//2:idx+n//2+1]

plt.clf()
x=np.linspace(0.1,0.9,80)
sinx=[np.sin(math.pi*i)/math.sqrt(1-i**2) for i in x]
xx=np.linspace(0.1,0.9,1000)
sinxx=[np.sin(math.pi*i)/math.sqrt(1-i**2) for i in xx]
max_est_err=[]
max_true_err=[]
n=60
y=[polint.polint(locate(x,w,n),sinlocate(x,w,n),w)[0] for w in xx]
dy=[polint.polint(locate(x,w,n),sinlocate(x,w,n),w)[1] for w in xx]

plt.title("Interpolation Vs True function")
plt.plot(xx,y,'r',xx,sinxx,'g')
plt.legend(["Interpolated Values","True Function"])
plt.grid() 
plt.savefig("sin_que5_order30.jpg")