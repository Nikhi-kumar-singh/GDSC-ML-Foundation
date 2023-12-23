import pandas as pd

def half(s):
    return s*0.5
def double(s):
    return s*2

shop = pd.read_csv("pd1.csv")
print(f"mean - \n",shop.mean())
print("\n")
print(f"median - \n",shop.median())
print("\n")
print(f"minimun - \n",shop.min())
print("\n")
print(f"maximum - \n",shop.max())
print("\n")

print(shop.head())
print("\n")

print(f"half - \n",shop[["date","flour"]].apply(half))
print("\n")

print(f"half - \n",shop[["sugar","rice","pulses"]].apply(double))
print("\n")

print(f"count - \n",shop["sugar"].value_counts())
print("\n")

print(f"sort - \n",shop.sort_values(by="date"))
print("\n")



