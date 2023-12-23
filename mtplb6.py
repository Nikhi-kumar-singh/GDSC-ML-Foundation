import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

fruits = ["mango","banana","lichi","guava","pineapple"]
data = [100,50,30,40,10]


plt.pie(data,labels=fruits)
plt.show()


plt.pie(data,labels=fruits,autopct='%0.3f%%',colors=["yellow","blue",'green','brown',"grey"])
plt.show()


plt.pie(data,labels=fruits,autopct='%0.3f%%',colors=["yellow","blue",'green','brown',"grey"],radius=1.5)
plt.pie([1],colors=['w'],radius=0.75)
plt.show()