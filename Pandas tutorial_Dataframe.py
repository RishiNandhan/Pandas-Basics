import pandas as pd
import numpy as np

########Data Frame##########

#create and empty dataframe
d1=pd.DataFrame()
print(d1)

#create a dataframe using a list of 1D
ar1=[1,2,3,4,5,6]
d2=pd.DataFrame(data=ar1)
print(d2)

#create a dataframe using a list of 2D
ar2=[['ram',10],['rishi',21],['ebin',30]]
d3=pd.DataFrame(data=ar2,columns=["name","age"])
print(d3)

ar3={'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
d4=pd.DataFrame(data=ar3,index=['rank1','rank2','rank3','rank4'])
print(d4)

ar4 = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
       'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
d5 = pd.DataFrame(ar4)
print(d5)

#Column selection, addition and deletion

ar5={'key1':pd.Series(data=[1,2,3,4,5]),'key2':pd.Series(data=[10,11,12,13,14,15,16])}
d6=pd.DataFrame(data=ar5)
print(d6)

print(d6['key2']) #selecting column key2

d6['key3']=pd.Series(data=[20,21,22,23,24,25,26,27]) #addition of new column
print(d6) # 27 is added as in went out of index

del d6['key2'] #deleting a column
print(d6)

d6['key4']=d6['key1']+d6['key3'] #creating new column using the other columns.
print(d6)

#row selection, addition and deletion

print(d5.loc['c']) #loc function is used for string index
print(d5.iloc[2]) #iloc function is used for int index
print(d5.iloc[1:]) #slicing of rows

d7=pd.DataFrame(data=np.array(np.random.randn(5,2)),columns=['a','b'])

print(d7)

#adding new rows
d8 = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
d9 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
d8=d8.append(d9)
print(d8)

#deleting rows
d7=d7.drop(0)
print(d7)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
import random
from sklearn.utils import shuffle

lr1=LogisticRegression(n_jobs=-1,penalty="l2",random_state=0)
#lr1.fit()
#lr1.predict()
#lr1.score()
from sklearn.preprocessing import StandardScaler
#classification_report()
s=StandardScaler()
import numpy as np

aa=np.array(np.arange(0,40)).reshape(8,5)
print(aa)
aaa=s.fit_transform(aa)
print(aaa)
