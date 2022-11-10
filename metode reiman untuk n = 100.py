# untuk n = 100 
import numpy as np
import matplotlib.pyplot as plt
def func(x):
    return (x**2)*np.exp(-x)
a =1
b =10
n =100
x = np.linspace(a,b,n)
dx = (x[-1]-x[0])/(n-1)
hasil = 0
for i in range(n-1):
    hasil +=dx*func(x[i])
print(hasil) 

xp = np.linspace(a,b)
plt.plot(xp,func(xp))
for i in range (n -1 ):
    plt.bar (x[i],func(x[i]),align = 'edge',width = dx, color='grey', edgecolor = 'black')
plt.show()
