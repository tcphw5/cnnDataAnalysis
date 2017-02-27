# -*- coding: utf-8 -*-
"""
analysis of CNN articles pt1

gets the unified vocabulary for all articles in one file with word counts

Created on Wed Feb  8 11:23:03 2017

@author: tpwin10
"""

import numpy as np


fileOUT = open('Output.txt', 'w', encoding='utf-8')
fileOUT2 = open('Output2.txt', 'w', encoding='utf-8')
counterINT = 0
numofArticles = 105; #constant. needs to be changed if number changes

totalwordcounts = np.array([])
combineddata = []

for x in range(105):
    fileIN = "tokenizedOutput" + str(x+1) + ".txt"
    data = np.genfromtxt(fileIN, dtype='U20', converters={0:lambda x: x.decode()})
    
    datalist = data.tolist()
        
    
    for x in range(len(datalist)):
        if datalist[x][-1] == "," or datalist[x][-1] == "." or datalist[x][-1] == ")":
            datalist[x] = datalist[x][:-1]
    
    combineddata = datalist + combineddata
    
np.asarray(combineddata)

unique, counts = np.unique(combineddata, return_counts=True)
    
wordcounts = np.asarray((unique, counts)).T

sortedwordcounts = wordcounts[np.argsort(wordcounts[:, 1])[::-1]]

sortedwordcounts = wordcounts[np.argsort(wordcounts[:, 1].astype(int))[::-1]]
 
for word in sortedwordcounts:
    fileOUT.write(word[0] + " " + word[1] + "\n")
    fileOUT2.write(word[0] + "\n")