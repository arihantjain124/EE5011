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
k=4
x=np.linspace(0,10,10)
sinx=np.sin((x*k))
xx=np.linspace(0,10,200)
sinxx=np.sin((xx*k))
max_est_err=[]
max_true_err=[]
order=[3,10]
for i in range(order[0],order[1]):
    n=i
    y=[polint.polint(locate(x,w,n),sinlocate(x,w,n),w)[0] for w in xx]
    dy=[polint.polint(locate(x,w,n),sinlocate(x,w,n),w)[1] for w in xx]
    max_est_err.append(max((np.absolute(dy))))
    max_true_err.append(max((np.absolute([y[j]-sinxx[j] for j in range(len(sinxx))]))))

plt.title("Sampling Theorem")
np.seterr(all="ignore")
plt.yscale("log")
plt.xlabel('Order of Interpolation')
plt.ylabel('Max Error')
plt.plot(range(order[0],order[1]),max_est_err,color='red',label="Estimated Error")
plt.plot(range(order[0],order[1]),max_true_err,color='green',label="True Error")
plt.legend(numpoints=1)
plt.grid() 
plt.savefig("error_theory.jpg")