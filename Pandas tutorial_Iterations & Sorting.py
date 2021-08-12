import numpy as np
import pandas as pd
df1=pd.DataFrame(data=np.random.rand(10,3),columns=['a','b','c'])
print(df1)

"""
Iteration on different object type:
1) Series- return the values
2) Dataframe- return the column name
3) Panel- return the item name
"""
for i in df1:
    print("column name: "+i)
print("#####")
"""
1) iteritems()- return key,value for each row
2) iterrows()- returns index,series in the dataframe
3) itertuples()- returns the tuple of each row
"""

for key,value in df1.iteritems():
    print(key,value)
print("########")
for index,series in df1.iterrows():
    print(index,series)
print("#########")
for row in df1.itertuples():
    print(row)
print("#########")
"""
while iterating over the data....any changes made will not be reflected as 
it is a view of the original data. So any changes made will not reflect in the data.
"""
df2=pd.DataFrame(data=np.random.rand(10,2),columns=['a','b'],index=[3,4,6,8,2,1,0,5,7,9])
print(df2)
print("######")
#sort by index
sort_index= df2.sort_index()
print(sort_index)
print("#######")
#sort by values
sort_values1=df2.sort_values(by=['a','b'])
print(sort_values1)
print("##########")
#sort by values using algorithm
sort_values2=df2.sort_values(by=['a','b'],kind="mergesort")
print(sort_values2)
"""
There are 3 kinds of sorting algorithm
1) mergesort
2) quicksort
3) heapsort
"""
