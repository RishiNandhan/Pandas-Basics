import pandas as pd
import numpy as np

## Label based Indexing (.loc[])

d1=pd.DataFrame(data=np.random.rand(8,4),columns=['a','b','c','d'])
print(d1)
print("#####")
print(d1.loc[:,'a'])
print("#####")
print(d1.loc[:,['a','c']])
print("#######")
print(d1.loc[:,:])
print("#######")
print(d1.loc[0:5,:])
print("########")
print(d1.loc[[0,2,4,6],['a','c']])

##integer based indexing (.iloc[])

d2=pd.DataFrame(data=np.random.rand(10,4),columns=['a','b','c','d'])
print(d2)
print("#######")
print(d2.iloc[1:5,1:3])


##.ix[] is a mix of both integer and label






