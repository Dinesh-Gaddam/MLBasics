
import pandas as pd
import numpy as np

series = pd.Series([1,2,3,4,5,6,np.nan,8,9,10])

# 
print(series)

#data range 
dates = pd.date_range('20200301',periods=10)

print(dates)

dataframe = pd.DataFrame(np.random.randn(10,4),index=dates,columns=['col1','col2','col3','col4'])

print(dataframe)

#How to view data 
print(dataframe.head()) 
print(dataframe.tail())
print(dataframe.index)
print(dataframe.columns)

print(dataframe.to_numpy())



dataframeDic = pd.DataFrame({'A':[1,2,3,4],
                             'B':pd.Timestamp('20200301'),
                             'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                             'D':np.array([5]*4,dtype='int32'),
                             'E':pd.Categorical(['true','false','True','False'])
    
    
    })

print(dataframeDic)


