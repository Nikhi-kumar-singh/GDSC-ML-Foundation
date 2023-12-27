from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from sklearn.model_selection import train_test_split



df = pd.read_csv("spam.csv")
# print(df)

df["spam"] = df["Category"].apply(lambda x : 1 if x=="spam" else 0)
print(df.spam)

x_train,x_test,y_train,y_test = train_test_split(df.Message,df.spam)


clf = Pipeline([
    ('vectorizer',CountVectorizer()),
    ('nb',MultinomialNB())
])

v = CountVectorizer()
clf.fit(x_train,y_train)

email = {"Nah I don't think he goes to usf, he lives around here though"}
email_count = v.fit_transform(email)
predict1 = clf.predict(email)
print(predict1)

email = ["Nah I don't think he goes to usf, he lives around here though"]
predict2 = clf.predict(email)
score = clf.score(x_test,y_test)
print(predict2)

