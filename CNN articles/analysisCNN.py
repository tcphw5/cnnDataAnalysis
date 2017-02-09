# -*- coding: utf-8 -*-
"""
analysis of CNN articles

Created on Wed Feb  8 11:23:03 2017

@author: tpwin10
"""

import numpy as np

tokenizedOutput = "tokenizedOutput1_1.txt"

#data = np.loadtxt(tokenizedOutput, dtype=np.dtype(str))
data = np.genfromtxt(tokenizedOutput, dtype=str)

datalist = data.tolist()

for x in range(len(data)):
    if data[x][-1] == "," or data[x][-1] == "." or data[x][-1] == ")":
        data[x] = data[x][:-1]

datafixed = np.array(data)


"""
for word in np.nditer(data, op_flags=['readwrite']):
    if word == "," or word == "." or word == ")":
        #print("hi")
        word[...] = word[0:-1]
        print(word)
"""


unique, counts = np.unique(datafixed, return_counts=True)

wordcounts = np.asarray((unique, counts)).T

sortedwordcounts = wordcounts[np.argsort(wordcounts[:, 1])[::-1]]

fileOUT = open('Output.txt', 'w', encoding='utf-8')


for word in sortedwordcounts:
    fileOUT.write(word[0] + " " + word[1] + "\n")