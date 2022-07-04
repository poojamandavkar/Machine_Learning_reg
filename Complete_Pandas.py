# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:52:50 2022

@author: dell
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

list1 = [ 
        {"name": "Ginger", "breed": "Dachshund", "height_cm": 22,"weight_kg": 10, "date_of_birth": "2019-03-14"},
        {"name": "Scout", "breed": "Dalmatian", "height_cm": 59,"weight_kg": 25, "date_of_birth": "2019-05-09"}
      ]

#list = pd.DataFrame(list1)

list2= {
         'name': ['Ginger','Scout'],
         'breed': ['Dachshund','Dalmatian'],
         'height_cm': [22,59]
        }

list = pd.DataFrame(list2)

Dataset = pd.read_csv(r'C:\Users\dell\Documents\Practice DS\avocado.csv')

#add Date as index_col
data = pd.read_csv(r'C:\Users\dell\Documents\Practice DS\avocado.csv',index_col='Date')

new = data.set_index(['region'])
data.isnull().sum()

#remove index from Dataframe
data = data.reset_index(drop=False)   #index_col date addes as normal column if we pass False
data = data.reset_index(drop=True)#It will  remove index col_Date

data.to_csv('test_write.csv')    #write records in test_weite.csv

data.head(10)
data.tail()
data.info()   #to get a concise summary of the DataFrame)
data.shape
data.describe()
data.values  #eturn a Numpy representation of the given DataFrame
data.columns

even = pd.Series([2,4,6,8,10])
odd = pd.Series([1,3,5,7,9])

res = even.append(odd)
res

data.sort_values(["AveragePrice", "year"], ascending=[True, False])

#sorting by index
data.sort_index(ascending=True)

#subsetting of data
data['AveragePrice']
data[['AveragePrice','Total Volume','year']]   # subsetting multiple columns
subset= data[data['type'].isin(['organic'])]

data['AveragePrice']<1      #it will return True/False
data[data['AveragePrice']<1]

data[data['type']=='organic']
data[data['Date'] <="2015-02-04"]

data[(data['Date']<="2015-02-04")& (data['type']=='organic')]

#multiple parrameters filtering

sub1 = data['region'].isin(["Boston", "SanDiego"])
sub2 = data['year'].isin([2016,2017])
final = data[sub1 & sub2]

data.isna().sum()        #counting missing values
data.isna().any()        # give true/false for null columns

data.dropna()
data.fillna(avg_value)

data['average'] = data['AveragePrice'] * 100    # add new column in dataset

del data['average']
data = data.drop(['average'],axis=1)

data["AveragePrice"].mean()
data['Date'].max()

#data.drop_duplicate(subset=["year"])
data['year'].value_counts()

data.groupby(['year','type'])['AveragePrice'].agg([min,max])


#visualization of Data

data['AveragePrice'].hist()

x=data.groupby(['region'])['AveragePrice'].mean().head(10)
x.plot(kind='bar')

data.plot(x='AveragePrice',y='Total Volume',kind= 'scatter')
