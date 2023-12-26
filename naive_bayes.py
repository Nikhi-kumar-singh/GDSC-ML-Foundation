import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


df = pd.read_csv("../data_files/train.csv")
# print(df.head())
# print(dir(df))

df = df.drop(["PassengerId","Name","SibSp","Parch","Ticket","Cabin","Embarked"],axis="columns")
# print(df.head())

feature = df.drop(["Survived"],axis="columns")
target = df.Survived
# print(feature.head())
# print(target.head())

Sex = pd.get_dummies(df.Sex)
# print(Sex.head())

feature = feature.drop(["Sex"],axis="columns")
# print(feature.head())
feature = pd.concat([feature,Sex],axis="columns")
# print(feature.head())


# print(feature.Age)
# filling NaN values with mean values of available age
feature.Age = feature.Age.fillna(feature.Age.mean())
# print(feature.Age)

# splitting data into training and testing set
x_train,x_test,y_train,y_test = train_test_split(feature,target,test_size=0.2)


# using gaussianNB() model
model = GaussianNB()
model.fit(x_train,y_train)
predicted = model.predict(x_test)
predicted1 = model.predict(x_test[:10])
predicted2 = model.predict_proba(x_test[:10])
score = model.score(x_test,y_test)
# print(score)
# print(predicted)
# print(predicted1)
print(predicted2)
