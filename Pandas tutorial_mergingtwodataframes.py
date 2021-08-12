import pandas as pd
import numpy as np

"""
pd.merge(left,right,on=None, how="inner", left_on=None, right_on=None, sort=True, left_index=False, right_index=False)
left- one dataframe
right- another dataframe

"""

left=pd.DataFrame(data={'id':[1,2,3,4,5],
                        'Name':['ram','rishi','madu','manoj','ebin'],
                        'subject-id':['sub1','sub2','sub4','sub6','sub5']})

right = pd.DataFrame(data={'id':[1,2,3,4,5],
                           'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
                           'subject-id':['sub2','sub4','sub3','sub6','sub5']})
print(left)
print("#########")
print(right)

#merge left and right dataframes
merge1=pd.merge(left=left,right=right,on="id")
print(merge1)
print("#########")

#merge with multiple keys
merge2=pd.merge(left=left,right=right,on=["id","subject-id"])
print(merge2)

#left,right,inner and outer joins
merge3=pd.merge(left=left,right=right,on=['id','subject-id'],how="left")
print(merge3)

merge4=pd.merge(left=left,right=right,on=['id','subject-id'],how="right")
print(merge4)

merge5=pd.merge(left=left,right=right,on=['id','subject-id'],how="outer")
print(merge5)

merge6=pd.merge(left=left,right=right,on=['id','subject-id'],how="inner")
print(merge6)
