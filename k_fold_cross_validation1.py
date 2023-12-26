import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.datasets import load_digits



def get_score(model,x_train,x_test,y_train,y_test):
    model.fit(x_train,y_train)
    return model.score(x_test,y_test)


digits = load_digits()
x_train,x_test,y_train,y_test = train_test_split(digits.data,digits.target,test_size=0.2)

# finding the score of every individual models
# print("answer : ",get_score(RandomForestClassifier(),x_train,x_test,y_train,y_test))


folds = StratifiedKFold(n_splits=10)
kf = KFold(n_splits=5)


# for train_index,test_index in kf.split(digits.data):
#     x_train,x_test,y_train,y_test = digits.data[train_index],digits.data[test_index],digits.target[train_index],digits.target[test_index]
#     print(get_score(LogisticRegression(),x_train,x_test,y_train,y_test))
#     print(get_score(LinearRegression(), x_train, x_test, y_train, y_test))
#     print(get_score(RandomForestClassifier(), x_train, x_test, y_train, y_test))
#     print("\n")


score_l = []
score_svm = []
score_rfc = []

for train_index,test_index in kf.split(digits.data):
    x_train,x_test,y_train,y_test = digits.data[train_index],digits.data[test_index],digits.target[train_index],digits.target[test_index]
    score_l.append(get_score(LinearRegression(),x_train,x_test,y_train,y_test))
    score_svm.append(get_score(SVC(), x_train, x_test, y_train, y_test))
    score_rfc.append(get_score(RandomForestClassifier(n_estimators=40), x_train, x_test, y_train, y_test))
    print("\n")


print(score_l)
print(score_svm)
print(score_rfc)
