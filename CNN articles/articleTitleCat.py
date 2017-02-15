# -*- coding: utf-8 -*-
"""
extracts title and link for easier manual classifying

Created on Wed Feb 15 11:25:26 2017

@author: tplab
"""

import numpy as np


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
                         
                           
    newrow = []
    
    
    for word in datalist:
        if word != "By" and word != "Set" and word != "StaffUpdated" and word != "Updated":
            newrow.append(word)
        else:
            break

    
    #print(newrow)
    artcounter += 1
    combineddata.append(newrow)
    
    