import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("hp1.csv")
# print(df)
# print("\n")
median_bedrooms = math.floor(df.bedrooms.median())
df.bedrooms.fillna(median_bedrooms,inplace=True)
# print(df)

reg = LinearRegression()
reg.fit(df[["area","bedrooms","age"]],df.price)
print(reg.coef_)
print(reg.intercept_)