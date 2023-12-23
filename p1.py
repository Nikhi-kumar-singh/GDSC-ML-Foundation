# panda : panel data
# single-dimensional : series object
# multi - dimensional : data-frame

import pandas as pd

s1 = pd.Series([84,8419,849,84,96,498])

print(s1)
print(s1.size)
print(type(s1))
print("\n")

s1 = pd.Series([84,8419,849,84,96,498],index=["a","b","c","d","e","f"])
print(s1)
print(s1.array)
print("\n")

s1 = pd.Series({'a':10,'b':20,'c':30})
print(s1)
s1 = pd.Series({'a':10,'b':20,'c':30},index=['z','a','b','y','c'])
print(s1)