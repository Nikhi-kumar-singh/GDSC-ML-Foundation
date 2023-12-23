import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("hp.csv")
x = df[["area"]]
y = df["price"]

rg = LinearRegression()
rg.fit(x, y)
predicted_price = rg.predict(np.array([[3300]]))

print(predicted_price)
print("Coefficient:", rg.coef_)
print("Intercept:", rg.intercept_)

df["predicted_price"] = rg.predict(x)
df.to_csv("prediction.csv", index=False)
print(df)

plt.xlabel("area")
plt.ylabel("price")
plt.scatter(x, y, color="brown", marker="*")
plt.plot(df["area"], rg.predict(df[["area"]]), color="blue")  # Corrected this line
plt.show()
