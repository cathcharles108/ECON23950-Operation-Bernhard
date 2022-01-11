import matplotlib.pyplot as plt
import numpy as np
import math

# Setting up equilibrium values
pim=1
pig=1
# Setting up parameters
u=1
q = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
r=0.05
util = []
welfare = []
xaxis = int(input())

if (xaxis==1):
    start = 1
    finish = 50
else:
    start = 39
    finish = 40

for i in q:
    germany = []
    britain = []
    for x in range(start,finish+1,1):
        x = x/100
        y = x
        f = (1-2*y)/i
        M = ((1-f*i)-2*y)/(2*((1-f*i)-x))
        W = (u*y*(1-f*i)**2)/(4*(1-f*i-y))
        profit = (u/(4*r*W)) - i*(math.log(i)-1)
        germany.append(profit)
        britain.append(W)
    util.append(germany)
    welfare.append(britain)

xpoints = np.array(range(start,finish+1,1))
ypoints = []
selection = int(input())

for i in range(10):
    if (selection==1):
        ypoints.append(np.array(util[i]))
        plt.title(r"Simulation of foreign government utility")
        plt.ylabel(r"Foreign government utility")
        plt.xlabel("Probability of liking the good (%)")
        plt.plot(xpoints, ypoints[i], label=('q = ' + str(q[i])))
        plt.legend(loc="upper right")
    elif (selection==2):
        ypoints.append(np.array(welfare[i]))
        plt.title(r"Simulation of local government welfare")
        plt.ylabel(r"Local government welfare")
        plt.xlabel("Probability of liking the good (%)")
        plt.plot(xpoints, ypoints[i], label=('q = ' + str(q[i])))
        plt.legend(loc="upper left")

plt.show()
