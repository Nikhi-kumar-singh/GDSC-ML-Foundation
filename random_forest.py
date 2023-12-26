import pandas as pd
from sklearn.datasets import load_digits
from matplotlib import pyplot as plt
import seaborn as sn
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from sklearn.ensemble import RandomForestClassifier
# ensemble is used to run multiple algorithm

digits = load_digits()
# print(dir(digits))

# for i in range(40,47,2) :
#     plt.matshow(digits.images[i])
# #     plt.show()

# print(digits.data)
# print(digits.target)
df = pd.DataFrame(digits.data)
df["target"] = digits.target
# print(df.head())


x_train,x_test,y_train,y_test = train_test_split((df.drop("target",axis="columns")),digits.target,test_size=0.2)
# print(len(x_train))
# print(len(y_train))
# print(len(x_test))
# print(len(y_test))

model = RandomForestClassifier(n_estimators=50)
model.fit(x_train,y_train)
y_predicted = model.predict(x_test)
score =  model.score(x_test,y_test)
# print(y_predicted)
# print(score)

cm = confusion_matrix(y_test,y_predicted)
# print(cm)

plt.figure(figsize=(10, 10))
sn.heatmap(cm, annot=True)
plt.xlabel("Truth")
plt.ylabel("Predicted")
plt.show()

