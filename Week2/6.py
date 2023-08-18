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
x=np.linspace(0,1,16)
sinx=np.sin((x+x**2))
xx=np.linspace(-0.5,1.5,200)
sinxx=np.sin((xx+xx**2))
plt.title("Error estimate for order 12 to 16")
np.seterr(all="ignore")
plt.yscale("symlog")
order=[12,16]
for i in range(order[0],order[1]):
    n=i
    y=[polint.polint(locate(x,w,n),sinlocate(x,w,n),w)[0] for w in xx]
    dy=[polint.polint(locate(x,w,n),sinlocate(x,w,n),w)[1] for w in xx]
    plt.plot(xx,np.log(np.absolute(dy)),color='red',label="Estimated Error")
    plt.plot(xx,np.log(np.absolute(y-sinxx)),color='green',label="True Error")
plt.legend(["Estimated Error","True Error"])
plt.grid() 
plt.savefig("error_que3_12_16.jpg")