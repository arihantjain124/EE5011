import polint
import math
import numpy as np
import matplotlib.pyplot as plt
plt.clf()
x=np.linspace(0.5,1.5,5)
sinx=np.sin((x+x**2))
xx=np.linspace(0.5,1.5,200)
y=[polint.polint(x,sinx,w)[0] for w in xx]
dy=[polint.polint(x,sinx,w)[1] for w in xx]
plt.title("Interpolation Vs Sin function")
sinxx=np.sin((xx+xx**2))
plt.plot(x,sinx,'ro',xx,y,'r',xx,sinxx,'g')
plt.title("Interpolating sin")
plt.legend(["Table Values","Interpolated Values","True Function"])
plt.grid() 
plt.savefig("sin_que1.jpg")
plt.clf()
plt.title("Error estimate")
np.seterr(all="ignore")
plt.yscale("symlog")
plt.plot(xx,np.log(np.absolute(dy)),color='red',label="Estimated Error")
plt.plot(xx,np.log(np.absolute(y-sinxx)),color='green',label="True Error")
plt.legend(numpoints=1)
plt.grid() 
plt.savefig("error_que1.jpg")
