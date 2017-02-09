#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyzer for cnn news articles

Created on Thu Feb  9 12:28:40 2017

@author: tp-mate
"""

import numpy as np

INfile = "tokenizedOutput1_1.txt"

OUTfile = "Outputt.txt"

data = np.array([["hello,", 1], ["there,", 2], ["hi", 3]], dtype=str)

for word in data:
    if word[0][-1] == ",":
        word[0] = word[0][:-1]
        
for word in data:
    print(word)
    
