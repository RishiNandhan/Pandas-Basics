import numpy as np
import pandas as pd

d1=pd.DataFrame(np.random.rand(10,3),columns=['a','b','c'])
print(d1)
print("########")
d1.reindexed=d1.reindex(index=[0,2,5],columns=['a'])
print(d1.reindexed)

df1=pd.DataFrame(data=d1,columns=['a','b','c'])
df2=pd.DataFrame(data=np.random.rand(5,3),columns=['a','b','c'])
print(df1)
print("###########")
df1.reindexed=df1.reindex_like(df2)
print(df1.reindexed)
print("#########")
"""
There are three methods for the attribute method.
1) ffill- Forward fill
2) bfill- Backward fill
3) nearest- Fill from the nearest index

The limit atribute determines till what index the values must be filled.If not specified it fills for the entire object.
"""
df2.reindexed=df2.reindex_like(df1,method='ffill',limit=2)
print(df2.reindexed)

###Rename##
df3=pd.DataFrame(data=np.random.rand(6,3),columns=['a','b','c'])
print(df3)
print("#####")
df3=df3.rename(columns={'a':'col1','b':'col2'},index={0:'zero',1:'one',2:'two',3:'three'})
print(df3)



