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
x=np.linspace(0,1,5)
sinx=np.sin((x+x**2))
xx=0.4
sinxx=sinx[2]
res=polint.polint(locate(x,xx,n),sinlocate(x,xx,n),xx)
c=res[2]
d=res[3]
for i in range(0,n-1):
    plt.plot([i]*n,c[i]+sinxx,'rx')
    plt.plot([i]*n,d[i]+sinxx,'gx')

route=res[4]+sinxx
plt.plot([i+1]*n,c[i+1]+sinxx,'rx',label="C's")
plt.plot([i+1]*n,d[i+1]+sinxx,'gx',label="D's")
plt.plot(range(0,5),route,label="Route")
plt.xlabel("N increase")
plt.ylabel("M increase")
plt.legend()
plt.grid() 
plt.savefig("Tableau.jpg")