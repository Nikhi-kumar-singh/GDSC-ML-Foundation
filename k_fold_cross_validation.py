import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.datasets import load_digits


digits = load_digits()
# print(digits)

x_train,x_test,y_train,y_test = train_test_split(digits.data,digits.target,test_size=0.2)
# print(len(x_train))
# print(len(x_test))

lr = LogisticRegression()
lr.fit(x_train,y_train)
lr_score = lr.score(x_test,y_test)
print("linear regression score : ",lr_score)

svm = SVC()
svm.fit(x_train,y_train)
svm_score = svm.score(x_test,y_test)
print("svm score : ",svm_score)

rfc = RandomForestClassifier()
rfc.fit(x_train,y_train)
rfc_score = rfc.score(x_test,y_test)
print("rfc score : ",rfc_score)

kf = KFold(n_splits=3)
for train_index , test_index in kf.split([1,2,3,4,5,6,7,8,9]):
    print(test_index,test_index)
