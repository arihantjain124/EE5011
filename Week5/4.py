from scipy import integrate
from scipy.special import jv
import numpy as np
import sing_intg as si
import math
from pylab import *
from matplotlib.pyplot import loglog

def f(t):
    return np.exp(-t-2)/jv(1,np.sqrt(1-t**2))


plt.clf()
figure(1)

res=[]
err=[]
calls=[]

res.append(si.qromo(f,-1,1,eps=1e-5))
res.append(si.qromo(f,-1,1,eps=1e-6))
res.append(si.qromo(f,-1,1,eps=1e-7))


calls=[x[2] for x in res]
err=[x[1] for x in res]
loglog(calls,err,color='red',label="Estimated Error")

title("Convergence after Transformation by open romberg")

xlabel('Function Evaluations')
ylabel('Error')
legend(numpoints=1)
grid() 
figure(1).savefig("q1_4.jpg")
    
