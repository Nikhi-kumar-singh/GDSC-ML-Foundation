import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics


gold = pd.read_csv("gld_price_data.csv")
# print(gold.head())
# print(gold.shape)
# print(gold.info())
# print(gold.describe())
# print(gold.isnull().sum())

gold = gold.drop("Date",axis='columns')

correlation = gold.corr()
# print(correlation)
# print(correlation["GLD"])

# plt.figure(figsize=(10,10))
# sns.heatmap(correlation,cbar=True,square=True,fmt='.1f',annot_kws={'size:8'},cmap='Blues')
# sns.heatmap(correlation)
# plt.show()

# sns.displot(gold["GLD"],color="red")
# plt.show()

y = gold["GLD"]
x = gold.drop(["GLD"],axis="columns")
# print(x)


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=True)

model = RandomForestRegressor()
model.fit(x_train,y_train)
predict1 = model.predict(x_test)
score1 = model.score(x_test,y_test)
score2 = metrics.r2_score(y_test,predict1)
print("score of the prediction : ",score1)
print("r squared error : ",score2)