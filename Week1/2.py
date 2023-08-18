import os
import numpy as np
import matplotlib.pyplot as plt


plt.clf()
plt.figure(figsize=(10,10))
cmd="gcc Lagrange.c -lm"        # Command to compile c code using GCC
os.system(cmd)                  # executing cmd in terminal
cmd="./a.out"                   # command to execute output file which creates out.txt
os.system(cmd)

plt.figure(figsize=(12,6))

d=np.loadtxt("out.txt").transpose()         #numpy loads out.txt and changes its shape from 100,2 to 2,100
plt.plot(d[0],d[1],"x",color='black',label="Lagrange Interpolation") #Lagrange interpolation plot
plt.title("Lagrange Interpolation Vs Sin function")
plt.plot(d[0],np.sin(d[0]),color='green',label="Sin Function") #Original Function Plot
plt.legend(numpoints=1)
plt.grid() 
plt.savefig("Lagrange_8_order.png")  # saving figure to png file
plt.clf()
plt.figure(figsize=(12,6))
plt.yscale("symlog")
err=d[1]-np.sin(d[0])
plt.plot(d[0],np.log(np.absolute(err)))  #plot of absolute error between the two
plt.title("Error with 9 points at 8rd order")
plt.grid() 
plt.savefig("Error_8.png") 
plt.close('all')