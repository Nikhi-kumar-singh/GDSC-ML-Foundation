import numpy as np
from matplotlib import pyplot as plt

student = {"nikhil":85,"manish":78,"rahul":87,"prince":50,"pawan":60}
student1 = {"nikhil":84,"manish":79,"rahul":79,"prince":50,"pawan":60}
names = list(student.keys())
marks = list(student.values())
marks1 = list(student1.values())



plt.bar(names,marks1,color='g')
plt.title("student marks distribution - ")
plt.xlabel("name of students -")
plt.ylabel("marks of students - ")
plt.show()


plt.barh(names,marks,color='r')
plt.title("student marks distribution - ")
plt.xlabel("name of students -")
plt.ylabel("marks of students - ")
plt.show()