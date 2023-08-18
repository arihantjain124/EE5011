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
n=5
x=np.linspace(0,1,30)
sinx=np.sin((x+x**2))
xx=np.linspace(-0.5,1.5,200)
sinxx=np.sin((xx+xx**2))
y=[polint.polint(locate(x,w,n),sinlocate(x,w,n),w)[0] for w in xx]
dy=[polint.polint(locate(x,w,n),sinlocate(x,w,n),w)[1] for w in xx]
plt.title("Interpolation Vs Sin function")
plt.plot(x,sinx,'ro',xx,y,'r',xx,sinxx,'g')
plt.title("Interpolating sin")
plt.legend(["Table Values","Interpolated Values","True Function"])
plt.grid() 
plt.savefig("sin_que2.jpg")
plt.clf()
plt.title("Error estimate")
np.seterr(all="ignore")
plt.yscale("symlog")
plt.plot(xx,np.log(np.absolute(dy)),color='red',label="Estimated Error")
plt.plot(xx,np.log(np.absolute(y-sinxx)),color='green',label="True Error")
plt.legend(numpoints=1)
plt.grid() 
plt.savefig("error_que2.jpg")