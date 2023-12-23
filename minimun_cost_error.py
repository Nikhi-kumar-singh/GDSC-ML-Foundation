# the aim of the code is to minimise the cost

import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 1000
    m = len(x)
    learning_rate = 0.01

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/m) * sum([val**2 for val in (y-y_predicted)])
        # md = -(2/m)*(x*(y-y_predicted))
        # bd = -(2/m)*(y-y_predicted)
        md = -(2 / m) * sum(x * (y - y_predicted))
        bd = -(2 / m) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, iteration {},cost {}".format(m_curr,b_curr,i,cost))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)


plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x,y,color="blue",marker="+")
plt.show()