import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# from sklearn.matrics import confusion_matrix

digits = load_digits()
# print(dir(digits))
# print("\n")
# print(digits.feature_names)

# for i in range(10):
#     plt.matshow(digits.images[i])
#     plt.show()

# for i in range(10):
#     print(digits.images[i])

# for i in digits.target[:5]:
#     print(i)

x_train,x_test,y_train,y_test = train_test_split(digits.data,digits.target,test_size=0.2)

lr = LogisticRegression()
lr.fit(x_train, y_train)

# prediction_score = lr.score(x_test,y_test)
# print(prediction_score)
plt.matshow(digits.images[15])
plt.show()
print(digits.target[15])
lr.predict(digits.data[6])

