#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analysis of CNN articles pt2

Created on Fri Feb 10 16:16:24 2017

@author: tp-mate
"""

import numpy as np

fileIN = 'featuresnocount.txt'
featwords = np.genfromtxt(fileIN, dtype='U300', converters={0:lambda x: x.decode()})

featwords = featwords.tolist()

print(featwords)
artcounter = 1;

fileOUT = open('Output2.txt', 'w', encoding='utf-8')
counterINT = 0
numofArticles = 105; #constant. needs to be changed if number changes

#articletable = np.empty((0,100))
#articletable = np.append(articletable, featwords, axis=0)

combineddata = [featwords]

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
                           
    print(wordcounts)
                           
    newrow = []
    #newrow.append(datalist[0])
    
    for word in featwords:
        
        print(word)
        
        try:
            y = counts[np.where(unique == word)[0][0]]
        except IndexError:
            y = 0
        
        print(y)
    
        newrow.append(y)
        
             
        #print(y)
    
    #print(newrow)
    newrow[0] = artcounter
    artcounter += 1
    combineddata.append(newrow)
    
    
#articletablenp = np.array(articletable, ndmin = 2)
print(combineddata)
articletable = np.array(combineddata)
            
    
    
#print(datalist)