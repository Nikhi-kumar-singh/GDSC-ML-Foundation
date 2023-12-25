import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("carprice.csv")
# print(df.head())
# print("\n")
# print(df)

plt.scatter(df.mileage,df.sellprice,color="blue",marker="*")
# plt.show()

x=df[["mileage","age"]]
y=df["sellprice"]
# print(x)
# print("\n")
# print(y)


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
# print(x_train)
# print("\n")
# print(x_test)
# print("\n")
# print(y_train)
# print("\n")
# print(y_test)

lr = LinearRegression()
lr.fit(x_train,y_train)

# print(x_test)
# print("\n")
# print(lr.predict(x_test))
# print(lr.predict([[22000,2]]))
# print(lr.predict([[72000,5]]))

print(lr.score(x_test,y_test))

