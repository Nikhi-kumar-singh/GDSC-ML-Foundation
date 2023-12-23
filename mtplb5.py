import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

one = [1,2,3,4,5,6,7,8,9,0]
two = [1,2,3,4,5,4,3,2,1,0]
three = [6,7,8,9,0,0,0,0,0,0,9,8,7,6]

data = list([one,two,three])


plt.boxplot(data)
plt.show()

plt.violinplot(data,showmedians=True)
plt.show()
