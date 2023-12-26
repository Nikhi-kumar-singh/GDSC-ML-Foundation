import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("income.csv")
# print(df.head())

# plt.scatter(df.age,df.income,color="violet",marker="*")
# plt.xlabel("age",color="brown")
# plt.ylabel("income",color="brown")
# plt.show()

km = KMeans(n_clusters=3)
predicted = km.fit_predict(df[["age","income"]])
# print(predicted)

df["cluster"] = predicted
# print(df)

# plt.scatter(df.cluster,df.age)
# plt.show()
# plt.scatter(df.cluster,df.income)
# plt.show()

df0 = df[df.cluster==0]
df1 = df[df.cluster==1]
df2 = df[df.cluster==2]
# print(df0)
# print("\n")
# print(df1)
# print("\n")
# print(df2)


# scaler = MinMaxScaler()
# scaler.fit(df[["income"]])
# df.income = scaler.transform(df.income)
# print(df)

# below is used to print the centrid of the clusters
# print(km.cluster_centers_)

# plt.scatter(df0.age,df0.income,color="red",label="df0 and age")
# plt.scatter(df1.age,df1.income,color="green")
# plt.scatter(df2.age,df2.income,color="blue")
# plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color="yellow",label="centroid")
# plt.xlabel("age")
# plt.ylabel("income")
# plt.show()

k_rng = range(1,10)
sse= []
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[["age","income"]])
    sse.append(km.inertia_)   #this value gives the

# print(sse)

plt.xlabel("k")
plt.ylabel("sum of square error")
plt.plot(k_rng,sse)
plt.show()
