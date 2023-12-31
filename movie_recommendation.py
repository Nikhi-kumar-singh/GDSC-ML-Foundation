import pandas as pd
import numpy as np
from difflib import get_close_matches
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


data = pd.read_csv("movies.csv")

selected_features = ["genres","keywords","tagline","cast","director"]

for feature in selected_features :
    data[feature] = data[feature].fillna("")

combined_features = data["genres"]+" "+data["keywords"]+" "+data["tagline"]+" "+data["cast"]+" "+data["director"]

# converting text data into numerical data
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Calculate cosine similarity
similarity = cosine_similarity(feature_vectors)

# creating a list with movie names in the dataset
movie_list = data["title"].tolist()

movie_name = input("enter your favourite movie name : ")

find_match = get_close_matches(movie_name,movie_list)

close_match = find_match[0]

index_of_movie = data[data.title == close_match]["index"].values[0]

similarity_score =  list(enumerate(similarity[index_of_movie]))

# sorting movies based on their similarity score
sorted_similar_movie = sorted(similarity_score,key = lambda x : x[1],reverse=True)

# print the name of similar movie based on index
print("movies suggested for you : \n")
i=1
for movie in sorted_similar_movie:
    index = movie[0]
    title_from_index = data[data.index == index]["title"].values[0]
    if (i<31):
        print(i," ",title_from_index)
        i=i+1
