# -*- coding: utf-8 -*-
"""
classifier of cnnArticles

Created on Wed Feb 15 10:40:12 2017

@author: tplab
"""
import numpy as np
import pandas as pd
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier


datamat = np.load('datamatrix.npy')

#categoriesIndex.txt has an extra 1 after index name
#not sure why it is needed but value is not actually
#used. just needed to push down values to right spot
#once added to articledf
categories = pd.read_csv('categoriesIndex.txt')

fileIN = 'featuresnocount.txt'
featwords = np.genfromtxt(fileIN, dtype='U300', converters={0:lambda x: x.decode()})

articledf = pd.DataFrame(data=datamat[:,1:], index=datamat[:,0], columns=featwords[1:])

predictors = featwords[1:]

articledf["category index"] = categories

alg = RandomForestClassifier(random_state=1, n_estimators=1, min_samples_split=4, min_samples_leaf=2)

kf = cross_validation.KFold(articledf.shape[0], n_folds=5, random_state=1)

scores = cross_validation.cross_val_score(alg, articledf[predictors], articledf["category index"],cv=kf)

alg.fit(articledf[predictors], articledf["category index"])

predictions = alg.predict(articledf[predictors])

print(sum(scores)/len(scores))

