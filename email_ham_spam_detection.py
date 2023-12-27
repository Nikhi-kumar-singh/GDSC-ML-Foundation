import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


df = pd.read_csv("spam.csv")
# print(df.head())
# print(df.groupby("Category").describe())

df["spam"] = df["Category"].apply(lambda x : 1 if x== "spam" else 0)
df = df.drop(["Category"],axis="columns")


x_train,x_test,y_train,y_test = train_test_split(df.Message,df.spam,test_size=0.2)
# print(x_train.head())

v = CountVectorizer()
x_train_count = v.fit_transform(x_train.values)
# print(x_train_count.toarray()[:,3])


model = MultinomialNB()
model.fit(x_train_count,y_train)
emails = {
    "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's"
}
email_count = v.transform(emails)
predict1 = model.predict(email_count)
# print(predict1)

x_test_count = v.transform(x_test)
score = model.score(x_test_count,y_test)
print(score)
