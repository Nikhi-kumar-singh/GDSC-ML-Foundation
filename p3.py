import pandas as pd

iris = pd.read_csv("pd.csv")
print(iris)
print("\n")
print(iris.head())
print("\n")
print(iris.tail())
print("\n")
print(f"shape : ",iris.shape)
print("\n")
print(f"description : \n",iris.describe())
print("\n")


req = iris.iloc[5:9,0:]
print(req)
print("\n")

req = iris.loc[5:9,("name","age")]
print(req)
print("\n")

# drop column named - marks and axis =1
req = iris.drop("marks",axis=1)
print(req)
print("\n")
# drop rows that are - 1,2,3,4 and axis =0
req = iris.drop([1,2,3,4,5],axis=0)
print(req)
print("\n")


shop = pd.read_csv("pd1.csv")
print(f"mean - \n",shop.mean())
print("\n")
print(f"median - \n",shop.median())
print("\n")
print(f"minimun - \n",shop.min())
print("\n")
print(f"maximum - \n",shop.max())
print("\n")
