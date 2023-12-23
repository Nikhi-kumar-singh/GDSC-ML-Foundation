import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("houseprices1.csv")
dummies = pd.get_dummies(df.town)
# print(dummies)

merged = pd.concat([df,dummies],axis="columns")
# print(merged)

# merged.drop is used to drop a particular column from
final = merged.drop(['town','west'],axis='columns')
# print(final)

model = LinearRegression()
x = final.drop("price",axis="columns")
y = final.price

print(x)
print(y)

model.fit(x,y)
print(model.predict([[2000,0,1]]))

# predicts the correct prediction percentage
print(model.score(x,y))