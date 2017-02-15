#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analysis of CNN articles pt2

replaced by pt3

Created on Fri Feb 10 16:16:24 2017

@author: tp-mate
"""

import numpy as np

fileIN = 'featuresnocount.txt'
featwords = np.genfromtxt(fileIN, dtype='U300', converters={0:lambda x: x.decode()})

featwords = np.array([featwords])


fileOUT = open('Output2.txt', 'w', encoding='utf-8')
counterINT = 0
numofArticles = 105; #constant. needs to be changed if number changes

articletable = np.empty((0,100))
articletable = np.append(articletable, featwords, axis=0)

combineddata = []

for x in range(105):
    fileIN2 = "tokenizedOutput" + str(x+1) + ".txt"
    data = np.genfromtxt(fileIN2, dtype='U300', converters={0:lambda x: x.decode()})
    
    datalist = data.tolist()
        
    
    for x in range(len(datalist)):
        if datalist[x][-1] == "," or datalist[x][-1] == "." or datalist[x][-1] == ")":
            datalist[x] = datalist[x][:-1]
            
    np.asarray(datalist)

    unique, counts = np.unique(datalist, return_counts=True)
    
    wordcounts = np.asarray((unique, counts)).T
                           
    newrow = []
    newrow.append(datalist[0])
    
    for word in featwords:
        
        print(word)
        y = counts[np.where(unique == word[0])]
        
        if len(y) != 0:
            newrow.append(y[0])
            #print(y)
            #print(newrow)
        
        if len(y) == 0 and word[0] != 'ArticleLink':
            y = np.append(y, [0])
            newrow.append(y[0])
            #print(newrow)
            #print(y)
             
        #print(y)
    
    #print(newrow)
    npnewrow = np.array(newrow)
    articletable = np.append(articletable, npnewrow, axis=0)
    
    
#articletablenp = np.array(articletable, ndmin = 2)
print(articletable)
            
    
    
#print(datalist)