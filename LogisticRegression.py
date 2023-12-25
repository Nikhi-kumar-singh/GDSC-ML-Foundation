import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Read the dataset
df = pd.read_csv("age_insurance.csv")

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(df[["age"]], df["insurance"], test_size=0.2)

# Create a logistic regression model
lr = LogisticRegression()

# Fit the model on the training data
lr.fit(x_train, y_train)

# Make predictions on the test data
predictions = lr.predict(x_test)
predictions1 = lr.predict([[46]])

# Print the predictions
print(predictions)
print("\n")
print(predictions1)

# Evaluate the accuracy of the model
# accuracy = accuracy_score(y_test, predictions)
# accuracy = lr.score(x_test,y_test)
# print("Accuracy:", accuracy)

