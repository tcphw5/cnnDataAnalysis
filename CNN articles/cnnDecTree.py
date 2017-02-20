# -*- coding: utf-8 -*-
"""
classifier of cnnArticles

Created on Wed Feb 15 10:40:12 2017

@author: tplab
"""
import numpy as np
import pandas as pd


datamat = np.load('datamatrix.npy')

fileIN = 'featuresnocount.txt'
featwords = np.genfromtxt(fileIN, dtype='U300', converters={0:lambda x: x.decode()})



articledf = pd.DataFrame(data=datamat[:,1:], index=datamat[:,0], columns=featwords[1:])

