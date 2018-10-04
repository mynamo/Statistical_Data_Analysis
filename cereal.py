#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:10:10 2018

@author: aditikulkarni
"""

import pandas as pd
import numpy as np
from pandas.tools import plotting
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/aditikulkarni/Downloads/PracticeProjects/Cereal/cereal.csv', sep = ";")
data.drop(data.index[0], inplace = True)
print(data.head(5))
print(data.shape)
print(data.describe())
print(data["mfr"].value_counts()) # especially useful for categorical variables
data['calories']  = [int(c) for c in data['calories']]
data['cups']  = [float(c) for c in data['cups']]
data['rating']  = [float(c) for c in data['rating']]
groupby_type = data.groupby('type',axis = 0)
print(groupby_type)
for t,val in groupby_type['calories']:
    print(t)
    print(val.mean())
    print(val.count())
    

mfr_count = data["mfr"].value_counts()
print(mfr_count[0:5])

data.hist('rating',bins = 10)
data.boxplot(column = 'rating',by = 'type')
#groupby_type.boxplot()
print(data[data['calories']<=data['calories'].quantile(0.5)]) # quantile of 0.9 gives the value of the percentile or the value at 90% of the sorted series

#print(data[['calories','cups']].apply(lambda x,y:x*y, axis = 1))
print(data['calories'].transform((lambda x: (x-x.mean())/x.std())))
#print(data['calories'].)

#plotting.scatter_matrix(data[['calories','cups','rating']])
corr = data.corr()
fig,ax = plt.subplots()
fig_corr = sns.heatmap(corr,ax = ax, xticklabels = corr.columns.values,yticklabels = corr.columns.values,cmap = 'coolwarm' )

