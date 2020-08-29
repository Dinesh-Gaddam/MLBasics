import pandas as pd
dataops = pd.DataFrame([
    {'column1':[3,27]},
    {'column2':['sahasra','sasi']}
    ])

dataops
dataops1 = pd.DataFrame(
    [
    {'column1':[3,27],
     'column2':['sahasra','sasi']
    }    
        
    ]
    
    )
dataops1
dataops2 = pd.DataFrame(
    {'column1':[3,27],
     'column2':['sasi','sahasra']
    }    
    )
dataops2
dataops2.iloc[:]
dataops2.iloc[1:,:]
dataops2.iloc[1:,0]
dataops2.iloc[0:,0]
dataops2.iloc[:,0]
dataops2.loc[:]
dataops2.loc['column2']
dataops2.loc[['column2']]
dataops2.loc[:,['column2']]
serops1 = pd.Series([1,2,3])
serops2 = pd.Series([4,5,6])
serops1
dataopsserobject = pd.DataFrame([serops1,serops2])
dataopsserobject
serops2
dataopsserobject1 = pd.DataFrame(serops1,serops2)
dataopsserobject1
