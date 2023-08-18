import os
import numpy as np
import matplotlib.pyplot as plt


plt.clf()
plt.figure(figsize=(10,10))
cmd="gcc Lagrange.c -lm"        # Command to compile c code using GCC
os.system(cmd)                  # executing cmd in terminal
cmd="./a.out"                   # command to execute output file which creates out.txt
os.system(cmd)

figure,axis=plt.subplots(2,figsize=(10,10))

d=np.loadtxt("out.txt").transpose()         #numpy loads out.txt and changes its shape from 100,2 to 2,100
axis[0].plot(d[0],d[1])                     #Lagrange interpolation plot
axis[0].set_title("Lagrange Interpolation")


axis[1].plot(d[0],np.sin(d[0]))                   #Original Function Plot
axis[1].set_title("Sin function")

plt.savefig("Lagrange_3_order.png")                     # saving figure to png file

plt.figure(figsize=(12,6))
#plt.yscale("symlog")
#np.seterr(divide="ignore")
plt.plot(d[0],(np.absolute((d[1])-np.sin(d[0]))))  #plot of absolute error between the two
plt.grid() 
plt.title("Error with 9 points at 8rd order")
plt.savefig("Error_8_without_log.png") 
plt.close('all')