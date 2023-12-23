import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = [1,1,2,2,2,2,3,3,6,9,8,5,8,9,6,4,7,5,6,8,4,0]

iris = pd.read_csv("data.csv")
print(iris.head())
plt.hist(iris["p.length"],bins=20,color='b')
plt.show()

plt.hist(data,color='y',bins=25)
plt.show()

plt.hist(data,color='g',bins=20)
plt.show()
