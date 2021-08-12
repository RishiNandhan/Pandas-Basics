import pandas as pd
import numpy as np

############Series############
#create and empty series
s=pd.Series()
print(s)

#create a series from numpy array
arr=np.array([1,2,3,4,5])
s1=pd.Series(data=arr)
print(s1)

#create a series with manual index
arr1=np.array([2,3,4,5,6])
s2=pd.Series(data=arr1,index=[11,12,13,14,15],dtype="float")
print(s2)

#create a series using dict
dic={'key2':10,'key1':20,'key3':30}
s3=pd.Series(data=dic)
print(s3)

dic1={'key1':10,'key2':20,'key3':30}
s4=pd.Series(data=dic,index=[1,2,'key2','key1'])
print(s4)

#access data from position
arr2=np.array([1,2,3,4,5,6])
s5=pd.Series(data=arr2,dtype="int")
print(s5[3:])

#retrieve data using index
arr3=np.array([10,11,12,13,14,15,16])
s6=pd.Series(data=arr3)
print(s6[[0,1,2,3]])

########Data Frame##########

#create and empty dataframe
d1=pd.DataFrame()
print(d1)

#create a dataframe using a list of 1D
ar1=[1,2,3,4,5,6]
d2=pd.DataFrame(data=ar1)
print(d2)





