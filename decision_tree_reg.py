# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 21:45:54 2022

@author: dell
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\dell\Documents\DS\Machine Learning\SVR & Desicion tree\1.SVR\Position_Salaries.csv')

x = data.iloc[:,1:2]
y = data.iloc[:,2]

#from sklearn.model_selection import train_test_split
#x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)

#from sklearn.tree import DecisionTreeRegressor
#dec = DecisionTreeRegressor(random_state=0)
#dec.fit(x,y)

from sklearn.ensemble import RandomForestRegressor
ram = RandomForestRegressor()
ram.fit(x,y)
y_pred = ram.predict([[6.5]])
