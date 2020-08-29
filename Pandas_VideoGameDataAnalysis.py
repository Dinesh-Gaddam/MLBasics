import pandas as dataanalyizer

# Using pandas over num_py as we can columns of different datatypes like float/string/int 
# which is bit difficult in num_py
class Pandas_VideoGameDataAnalysis(object):
    """description of class"""

    # By default we need to pass self or we get error takes 0 positional arg but 1 was given
    def readData_iloc_loc_Style(self):
        reviews = dataanalyizer.read_csv("./Data/Pandas/ign.csv")
        #First first 5 rows,similarly tail will give last 5 rows
        #print(reviews.head())
        #print(reviews.shape)

        #indexing  [0:5,:] this means first 5 rows all columsn 
        #print(reviews.iloc[0:5,:])
        #print(reviews.iloc[:,0]) # first column all data 
        
        #Remove the first column as we don't need that 
        #reviews = reviews.iloc[:,1:]
        #print(reviews.head())

        #DataAccess using Labels getting two columns of 5 rows data
        print(reviews.loc[:5,['score','release_year']])

    def pandas_SeriesObjects(self):
        reviews = dataanalyizer.read_csv("./Data/Pandas/ign.csv")
        # series ob
        print(type(reviews.loc[:,'score'])) 
        print(type(reviews['score']))
        # For multiple columsn we need to use 
        print(reviews[['score','release_year']])

    def pandas_CreateSeriesObjects(self):
        serieobj1 = dataanalyizer.Series([1,2])
        serieobj2 = dataanalyizer.Series(['Can have strings',2])
        
        dfusingSeriesObject = dataanalyizer.DataFrame([serieobj1,serieobj2])
        print('dfusingSeriesObject \n %r'%(dfusingSeriesObject))

        dfusingInnerList = dataanalyizer.DataFrame(
            [
                [1,2],
                ['dinesh','sasi']                                           
            ]
            )

        print('dfusingInnerList \n %r'%(dfusingInnerList))

        dfusingInnerListWithColumnHeaders = dataanalyizer.DataFrame(
            [
                [1,2],
                ['dinesh','sasi']                                           
            ],
            columns = ['intdata','stringdata']
            )
        print('dfusingInnerListWithColumnHeaders \n %r'%(dfusingInnerListWithColumnHeaders))

        dfusingInnerListColumnHeadersWithDictionary = dataanalyizer.DataFrame(
        {
            'intdata':[1,2],
            'stringdata':['dinesh','sasi']
        }
        )
        print('dfusingInnerListColumnHeadersWithDictionary \n %r'%(dfusingInnerListColumnHeadersWithDictionary))

    def pandas_DataFrameMethods(self):
        reviews = dataanalyizer.read_csv("./Data/Pandas/ign.csv")
        #We can get given column head/tail 
        print('Given column title header \n %r' %(reviews[['title','score']].head()) )
        #to do math operations like mean
        print('Max value of score column \n %r' %(reviews['score'].max()) )
        #todo filter data using condition 
        # to get xbox one data who has score greater than 7
        filter_condition = (reviews['score'] > 7) & (reviews['platform'] == 'Xbox One')
        print('First five values of xbox filter condtion \n %r' %(reviews[filter_condition].head() ))
        # columns for corelation not sure how to use them 

    def pandas_Plotting(self):
       reviews = dataanalyizer.read_csv("./Data/Pandas/ign.csv")
       # plot using underhood matplotlib 
       filter_cond = reviews['platform'] == 'Xbon One'
       #Line graph
       reviews[filter_cond]['score'].plot()
       #Histogram
       reviews[filter_cond]['score'].plot(kind='hist')

pd = Pandas_VideoGameDataAnalysis()
#pd.pandas_SeriesObjects()
#pd.pandas_CreateSeriesObjects()
#pd.pandas_DataFrameMethods()
pd.pandas_Plotting()



