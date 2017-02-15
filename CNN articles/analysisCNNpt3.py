#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analysis of CNN articles pt3

creates data matrix using feature word counts for each article.
performs euclidean, cosine, and jaccard similarity comparisons for all pairs
and outputs results for each in 4 different files (two different jaccard 
methods)

Created on Fri Feb 10 16:16:24 2017

@author: tp-mate
"""

import numpy as np
from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import jaccard_similarity_score
from operator import itemgetter

fileIN = 'featuresnocount.txt'
featwords = np.genfromtxt(fileIN, dtype='U300', converters={0:lambda x: x.decode()})

featwords = featwords.tolist()

#print(featwords)
artcounter = 1;

#fileOUT = open('Output2.txt', 'w', encoding='utf-8')


counterINT = 0
numofArticles = 105; #constant. needs to be changed if number changes
#articles 70 and 75 are not found


combineddata = []

for x in range(numofArticles):
    fileIN2 = "tokenizedOutput" + str(x+1) + ".txt"
    data = np.genfromtxt(fileIN2, dtype='U300', converters={0:lambda x: x.decode()})
        
    datalist = data.tolist()
    
    
        
    
    for x in range(len(datalist)):
        if datalist[x][-1] == "," or datalist[x][-1] == "." or datalist[x][-1] == ")":
            datalist[x] = datalist[x][:-1]
            
    np.asarray(datalist)

    unique, counts = np.unique(datalist, return_counts=True)
    
    wordcounts = np.asarray((unique, counts)).T
                           
    #print(wordcounts)
                           
    newrow = []
    #newrow.append(datalist[0])
    
    for word in featwords:
        
        #print(word)
        
        try:
            y = counts[np.where(unique == word)[0][0]]
        except IndexError:
            y = 0
        
        #print(y)
    
        newrow.append(y)
        
             
        #print(y)
    
    #print(newrow)
    newrow[0] = artcounter
    artcounter += 1
    combineddata.append(newrow)
    
    
#print(combineddata)
#save
articletable = np.array(combineddata, dtype=int)

i = articletable[1][1:]
j = articletable[2][1:]

dist = 1 - spatial.distance.cosine(i, j)
dist2 = 1 - spatial.distance.jaccard(i, j)
print(dist)
print(dist2)

eudistmatrix = []
neweudistrow = []

eudisttable = []
cosdisttable = []
jacdisttable = []
jacdisttable2 = []

cosdistmatrix = []
newcosdistrow = []

jacdistmatrix = []
newjacdistrow = []

jacdistmatrix2 = []
newjacdistrow2 = []

for i in range(0, numofArticles):
    for j in range(0, numofArticles):        
        if i != j:
            a = articletable[i][1:]
            b = articletable[j][1:]
            #euclidian sim calculation
            dist = np.linalg.norm(a-b)
            eusim = 1/(1 + dist)
            #cos sim calculation
            cossim = 1 - spatial.distance.cosine(a, b)
            cossim = cosine_similarity(a.reshape(1, -1), b.reshape(1, -1))
            if np.isnan(cossim):
                cossim = 0
            
            #jaccard sim calculation with both scipy and skikit learn
            jacsim = 1 - spatial.distance.jaccard(a, b)
            if np.isnan(jacsim):
                jacsim = 0
                
            jacsim2 = jaccard_similarity_score(a, b)
            if np.isnan(jacsim2):
                jacsim2 = 0
            
            eudisttable.append((i+1, j+1, eusim))
            cosdisttable.append((i+1, j+1, cossim))
            jacdisttable.append((i+1, j+1, jacsim))
            jacdisttable2.append((i+1, j+1, jacsim2))
            
            
            neweudistrow.append(eusim)
            newcosdistrow.append(cossim)
            newjacdistrow.append(jacsim)
            newjacdistrow2.append(jacsim2)
            #print("between " + str(i) + " and " + str(j))
            #print(eusim)
        else:
            neweudistrow.append(-1)
            newcosdistrow.append(-1)
            newjacdistrow.append(-1)
            newjacdistrow2.append(-1)
    
    eudistmatrix.append(neweudistrow)
    cosdistmatrix.append(newcosdistrow)
    jacdistmatrix.append(newjacdistrow)
    jacdistmatrix2.append(newjacdistrow2)
    neweudistrow = []
    newcosdistrow = []
    newjacdistrow = []
    newjacdistrow2 = []
#save
eudistmatrix = np.array(eudistmatrix)
#save
cosdistmatrix = np.array(cosdistmatrix)
#save
jacdistmatrix = np.array(jacdistmatrix)
#save
jacdistmatrix2 = np.array(jacdistmatrix2)

#matrix not actually used but may be helpful for the future?

eudisttable = sorted(eudisttable, key=itemgetter(2), reverse=True)
cosdisttable = sorted(cosdisttable, key=itemgetter(2), reverse=True)
jacdisttable = sorted(jacdisttable, key=itemgetter(2), reverse=True)
jacdisttable2 = sorted(jacdisttable2, key=itemgetter(2), reverse=True)

eufile = open('euSimOutput.txt', 'w', encoding='utf-8')
cosfile = open('cosSimOutput.txt', 'w', encoding='utf-8')
jacfile = open('jacSimOutput.txt', 'w', encoding='utf-8')
jac2file = open('jac2SimOutput.txt', 'w', encoding='utf-8')

for tup in eudisttable:
    eufile.write(str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + "\n")
    
for tup in cosdisttable:
    cosfile.write(str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2][0][0]) + "\n")

for tup in jacdisttable:
    jacfile.write(str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + "\n")

for tup in jacdisttable2:
    jac2file.write(str(tup[0]) + " " + str(tup[1]) + " " + str(tup[2]) + "\n")