import pandas as pd
import numpy as np
s1=pd.Series(data=[1,2,3,4,5])
#percent change function
print(s1.pct_change())

d1=pd.DataFrame(data={'a':[1,2,3,4,5,6,7],'b':[1,10,100,2,20,200,3]})
print(d1)
print(d1.pct_change())

#correlation function

d2=pd.DataFrame(data=np.random.rand(10,4),columns=['a','b','c','d'])
print(d2)
print(d2.corr()) #returns correlation of all columns
print("#######")
print(d2['a'].corr(d2['b'])) #returns correlation of the specified two columns
print("#######")
#covariance

print(d2.cov())
print("#########")
print(d2['a'].cov(d2['b']))

#data ranking returns the rank of the data....if ties occured then the mean rank is assigned

d3=pd.Series(data=[1,2,3,3,6,5,4])
print(d3)
print(d3.rank())
#we can assign the method incase of tied rank...
# the different method are average, min,max,first
print(d3.rank(method="min"))
print(d3.rank(method="max"))
print(d3.rank(method="first"))




