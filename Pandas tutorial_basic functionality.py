import numpy as np
import pandas as pd

####Functionality of Series####

d1=pd.Series(np.random.rand(5))
# axes function returns list of row axis label
print("the axes are {a}".format(a=d1.axes))
# empty function returns whether the object is empty or not
print("Is the object empty? {b}".format(b=d1.empty))
# ndim function returns the dimensions of the object
print("The dimension of the object is: {c}".format(c=d1.ndim))
# size function returns the number of elements in the data
print("the size of the object is {d}".format(d=d1.size))
# values function return the values of the object
print("The values are: {e}".format(e=d1.values))
#head function return the first n values in the object
print("The first two values are: {f}".format(f=d1.head(2)))
# tail function returns the last n values in the object
print("The last two values are: {g}".format(g=d1.tail(2)))

#####Functionality of DataFrame#####
d2=pd.DataFrame(np.random.rand(10,2),columns=['a','b'])
print(d2)
print("The axes of the object is: {a}".format(a=d2.axes))
print("Is the object empty?: {b}".format(b=d2.empty))
print("The size of the object is: {c}".format(c=d2.size))
print("The values of the object is:\n{d}".format(d=d2.values))
print("The first 3 rows are:\n{e}".format(e=d2.head(3)))
print("The last 3 rows are:\n{f}".format(f=d2.tail(3)))
print("Number of dimensions in this object: {g}".format(g=d2.ndim))
print("The shape of the object is: {h}".format(h=d2.shape))
print("The datatype is:\n {a}".format(a=d2.dtypes))
#T function is used for transpose of rows into columns
print("The transpose is:\n{b}".format(b=d2.T))

#######Math functions########
d3 = pd.DataFrame({'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
    })
print(d3)
print("The sum along column:\n{a}".format(a=d3.sum()))
print("The sum along row is:\n{b}".format(b=d3.sum(1)))
print("The mean of the columns :\n{a}".format(a=d3.mean()))
print("The number of non-null values are:\n{b}".format(b=d3.count()))

"""
The other functions are 
1) median()- Median value
2) mode()- Mode value
3) std()- Standard Deviation
4) min() & max()- Minimum and maximum value
5) abs() & prod()- Absolute value and product of values
6) cumsum() & cumprod()- Cummuative sum and Cummulative product
"""
#summarize only character columns
print("The summary of the characterobject is:\n{a}".format(a=d3.describe(include=['object'])))
#summarize only numeric columns
print("The summary of the numeric columns is:\n{a}".format(a=d3.describe(include=['number'])))
#summarize all type of columns
print("The summary of the entire object is:\n{a}".format(a=d3.describe(include='all')))







