import numpy as np
from matplotlib import pyplot as plt

x = [10,20,30,40,50,60,70,80,90,100]
y1 = [8,5,7,2,6,0,9,1,3,4]
y2 = [2,9,6,3,5,1,4,7,0,8]


# c=color , s=size
plt.scatter(x,y1,c='r',marker='*',s=50)
plt.scatter(x,y2,c='g',marker='.',s=50)
plt.show()


# c=color , s=size
plt.subplot(1,2,1)
plt.scatter(x,y1,c='r',marker='*',s=50)
plt.subplot(1,2,2)
plt.scatter(x,y2,c='g',marker='.',s=50)
plt.show()

plt.subplot(2,1,1)
plt.scatter(x,y1,c='r',marker='*',s=50)
plt.subplot(2,1,2)
plt.scatter(x,y2,c='g',marker='.',s=50)
plt.show()