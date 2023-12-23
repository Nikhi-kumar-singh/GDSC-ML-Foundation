import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0,11)
y1 = 2*x
y2 = x*x
y3 = x*x*x
print(y1)
print(y2)
print(y3)

plt.plot(x,y1,color="b",linestyle="-",linewidth = 1)
plt.plot(x,y2,color="r",linestyle=":",linewidth = 1)
plt.plot(x,y3,color="g",linestyle="-.",linewidth = 1)
plt.title("line plot",color='y')
plt.xlabel("this is x label")
plt.ylabel("this is y label")
plt.grid(True)
plt.show()


plt.subplot(1,3,1)
plt.plot(x,y1,color="b",linestyle="-",linewidth = 1)
plt.subplot(1,3,2)
plt.plot(x,y2,color="r",linestyle=":",linewidth = 1)
plt.subplot(1,3,3)
plt.plot(x,y3,color="g",linestyle="-.",linewidth = 1)
plt.title("line plot",color='y')
plt.xlabel("this is x label")
plt.ylabel("this is y label")
plt.grid(True)
plt.show()



plt.subplot(3,1,1)
plt.plot(x,y1,color="b",linestyle="-",linewidth = 1)
plt.subplot(3,1,2)
plt.plot(x,y2,color="r",linestyle=":",linewidth = 1)
plt.subplot(3,1,3)
plt.plot(x,y3,color="g",linestyle="-.",linewidth = 1)
plt.title("line plot",color='y')
plt.xlabel("this is x label")
plt.ylabel("this is y label")
plt.grid(True)
plt.show()

