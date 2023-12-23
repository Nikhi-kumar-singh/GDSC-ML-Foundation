import pandas as pd

s1 = pd.Series([84,8419,849,84,96,498])
s2 = pd.Series([10,20,50,5])

print(s1[0::])
print("\n")
print(s1[1::])
print("\n")
print(s1[-2::])
print("\n")
print(s1[0:4:])
print("\n")
print(s1[::-1])
print("\n")
print(s1[4::-1])
print("\n")
print(s1[4:0:-1])
print("\n")

print(s1%5)
print("\n")
print(s1+s2)
print("\n")