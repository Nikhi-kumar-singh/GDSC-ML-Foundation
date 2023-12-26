from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_digits


digits = load_digits()


score = cross_val_score(LinearRegression(),digits.data,digits.target)
print(score)
# changing n_estimators is uesd in parameter tuning
score = cross_val_score(RandomForestClassifier(n_estimators=100),digits.data,digits.target)
print(score)
score = cross_val_score(SVC(),digits.data,digits.target)
print(score)