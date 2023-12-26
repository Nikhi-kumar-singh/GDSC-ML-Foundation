# gamma and regularization
# kernel

import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

iris = load_iris()
# print(iris)
# print(dir(iris))
# print(iris.feature_names)

df = pd.DataFrame(iris.data,columns=iris.feature_names)
# print(df.head())
# print('\n')
# print(df.tail())

df["target"] = iris.target
df["flower_name"] = df.target.apply(lambda x : iris.target_names[x])
# print(df.head())
# print(df[df.target == 1].head())
# print(df[df.target == 1].tail())
# print(df.flower_name)
# print(df)

df0 = df[df.target == 0]
df1 = df[df.target == 1]
df2 = df[df.target == 2]
# print(df0.head())
# print(df1.head())
# print(df2.head())

# plt.scatter(df0["sepal length (cm)"],df0["sepal width (cm)"],color="red",marker="+")
# plt.scatter(df1["sepal length (cm)"],df1["sepal width (cm)"],color="yellow",marker="*")
# plt.scatter(df2["sepal length (cm)"],df2["sepal width (cm)"],color="green",marker="+")
# plt.xlabel("sepal length",color="brown")
# plt.ylabel("sepal width",color="brown")
# plt.show()

# print(df.head())
x = df.drop(["target","flower_name"],axis="columns")
y = df.target
# print(x.head())

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

# C=10,gamma=10,kernel="linear" or kernel="rbf"
model1 = SVC(C=10,gamma=1)

model = SVC()
model.fit(x_train,y_train)

prediction = model.predict(x_test)
score = model.score(x_test,y_test)

print("score : ",score)
print("prediction : ",prediction)
