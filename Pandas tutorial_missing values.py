import pandas as pd
import numpy as np
"""
two method to fill NA values:
1) ffill - fill the na forward
2) bfill- fill the na backward
"""


d1=pd.DataFrame(data={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),
                      'two':pd.Series([10,11,12,13,14,15],index=['a','c','e','f','g','h'])})
print(d1)
print("#########")
print(d1.isnull())
print("##########")
print(d1.isna())
print("###########")
print(d1.notnull())
print("######")
print(d1.sum())
print("#########")
d2=d1.fillna(0)
print(d2)
d3=d1.fillna(method="ffill")
print(d3)

d4=d1.fillna(method="bfill")
print(d4) #the last three values are filled because there is no more data available after the na

d5=d1.dropna()
print(d5)

d6=d1.replace({1:100,2:200})
print(d6)

d7=d1.copy(deep=True)
d7.iloc[:]['one'].fillna(0,inplace=True)
print(d7)


