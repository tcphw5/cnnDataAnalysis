# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 19:04:51 2017

@author: tpwin10
"""

#fileIN = open('articleOutput.txt', 'r')
#fileOUT = open('tokenizedOutput.txt', 'w', encoding='utf-8')

counterINT = 0



for x in range(13):
    fileIN = open('articleOutput' + str(x+1) + '.txt', 'r', encoding='utf-8')
    fulltext = fileIN.read()
    
    tokenizedArticles = fulltext.split()


    for tok in tokenizedArticles:
        if tok[0:5] == 'http:':
            counterINT += 1
            fileOUT = open('tokenizedOutput' + str(x+1) + "_" + str(counterINT) + '.txt', 'w', encoding='utf-8')
        
        fileOUT.write(tok + "\n")
        

fileOUT.close()
fileIN.close()