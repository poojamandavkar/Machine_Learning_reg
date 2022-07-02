# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 19:11:40 2022

@author: dell
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import matplotlib
import warnings
warnings.filterwarnings("ignore") # Don't want to see the warnings in the notebook
from sklearn import svm


Dataset = pd.read_csv(r'C:\Users\dell\Documents\Practice DS\avocado.csv')
Dataset.shape
Dataset.isnull().sum()
Dataset.info()
Dataset.describe().round()
