import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

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

# print(x)
# print(y)

model.fit(x,y)
# print(model.predict([[2000,0,1]]))


# predicts the correct prediction percentage
# print(model.score(x,y))

le = LabelEncoder()
dfle = df
dfle.town=le.fit_transform(dfle.town)
# print(dfle)

w = df[["town","area"]].values
z = dfle.price
# print(w)
# print("\n")
# print(z)

# ohe = OneHotEncoder(categorical_features=[0])
# m = ohe.fit_transform(w).toarray()
# print(m)
# print(m[:,1:])