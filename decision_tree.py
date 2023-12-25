import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("salary.csv")
# print(df.head(3))
# print(df.tail(3))

inputs = df.drop(["salary_more_than_k"],axis="columns")
targets = df.salary_more_than_k
# print(inputs)
# print(targets)

le = LabelEncoder()

inputs["company_n"] = le.fit_transform(inputs["company"])
inputs["job_n"] = le.fit_transform(inputs["job"])
inputs["degree_n"] = le.fit_transform(inputs["degree"])
# print(inputs.head())
# print(inputs.tail())

inputs_n = inputs.drop(["company","job","degree"],axis="columns")
# print(inputs_n)

x_train,x_test,y_train,y_test = train_test_split(inputs_n,targets,test_size=0.2)
# print(x_train)

dtc = DecisionTreeClassifier()
dtc.fit(x_train,y_train)
prediction = dtc.predict(x_test)
accuracy = dtc.score(x_test,y_test)
print(prediction)
print("\n")
print(accuracy)
