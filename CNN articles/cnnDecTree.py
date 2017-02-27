# -*- coding: utf-8 -*-
"""
classifier of cnnArticles

Created on Wed Feb 15 10:40:12 2017

@author: tplab
"""
import numpy as np
import pandas as pd
#from sklearn import cross_validation
#from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score
from sklearn import tree
import pydotplus
import random

datamat = np.load('datamatrix.npy')

#categoriesIndex.txt has an extra 1 after index name
#not sure why it is needed but value is not actually
#used. just needed to push down values to right spot
#once added to articledf
categories = pd.read_csv('categoriesIndex.txt')

fileIN = 'Output2.txt'
#fileIN = 'featuresnocount.txt'
featwords = np.genfromtxt(fileIN, dtype='U300', converters={0:lambda x: x.decode()})

articledf = pd.DataFrame(data=datamat[:,1:], index=datamat[:,0], columns=featwords[1:])

trainingdfold1 = pd.DataFrame(columns=featwords[1:])
testingdfold1 = pd.DataFrame(columns=featwords[1:])

trainingdfold2 = pd.DataFrame(columns=featwords[1:])
testingdfold2 = pd.DataFrame(columns=featwords[1:])

trainingdfold3 = pd.DataFrame(columns=featwords[1:])
testingdfold3 = pd.DataFrame(columns=featwords[1:])

trainingdfold4 = pd.DataFrame(columns=featwords[1:])
testingdfold4 = pd.DataFrame(columns=featwords[1:])

trainingdfold5 = pd.DataFrame(columns=featwords[1:])
testingdfold5 = pd.DataFrame(columns=featwords[1:])  

predictors = featwords[1:]

articledf["category index"] = categories

#alg = RandomForestClassifier(random_state=1, n_estimators=1, min_samples_split=4, min_samples_leaf=2)

kval = 6

alg1 = DecisionTreeClassifier(random_state=0)
alg12 = KNeighborsClassifier(n_neighbors=kval)

alg2 = DecisionTreeClassifier(random_state=0)
alg22 = KNeighborsClassifier(n_neighbors=kval)

alg3 = DecisionTreeClassifier(random_state=0)
alg32 = KNeighborsClassifier(n_neighbors=kval)

alg4 = DecisionTreeClassifier(random_state=0)
alg42 = KNeighborsClassifier(n_neighbors=kval)

alg5 = DecisionTreeClassifier(random_state=0)
alg52 = KNeighborsClassifier(n_neighbors=kval)

Datasplits = [x for x in range(106) if x != 0]

random.shuffle(Datasplits)

part1 = Datasplits[0:21]
part2 = Datasplits[21:42]
part3 = Datasplits[42:63]
part4 = Datasplits[63:84]
part5 = Datasplits[84:105]

icounter = 0

for i in part1:
    testingdfold1 = testingdfold1.append(articledf[i-1:i])

for i in part2:
    trainingdfold1 = trainingdfold1.append(articledf[i-1:i])
    
for i in part3:
    trainingdfold1 = trainingdfold1.append(articledf[i-1:i])
    
for i in part4:
    trainingdfold1 = trainingdfold1.append(articledf[i-1:i])
    
for i in part5:
    trainingdfold1 = trainingdfold1.append(articledf[i-1:i])
    
    
for i in part1:
    trainingdfold2 = trainingdfold2.append(articledf[i-1:i])

for i in part2:
    testingdfold2 = testingdfold2.append(articledf[i-1:i])
    
for i in part3:
    trainingdfold2 = trainingdfold2.append(articledf[i-1:i])
    
for i in part4:
    trainingdfold2 = trainingdfold2.append(articledf[i-1:i])
    
for i in part5:
    trainingdfold2 = trainingdfold2.append(articledf[i-1:i])
    
    
for i in part1:
    trainingdfold3 = trainingdfold3.append(articledf[i-1:i])

for i in part2:
    trainingdfold3 = trainingdfold3.append(articledf[i-1:i])
    
for i in part3:
    testingdfold3 = testingdfold3.append(articledf[i-1:i])
    
for i in part4:
    trainingdfold3 = trainingdfold3.append(articledf[i-1:i])
    
for i in part5:
    trainingdfold3 = trainingdfold3.append(articledf[i-1:i])
    
    
for i in part1:
    trainingdfold4 = trainingdfold4.append(articledf[i-1:i])

for i in part2:
    trainingdfold4 = trainingdfold4.append(articledf[i-1:i])
    
for i in part3:
    trainingdfold4 = trainingdfold4.append(articledf[i-1:i])
    
for i in part4:
    testingdfold4 = testingdfold4.append(articledf[i-1:i])
    
for i in part5:
    trainingdfold4 = trainingdfold4.append(articledf[i-1:i])
    
    
    
for i in part1:
    trainingdfold5 = trainingdfold5.append(articledf[i-1:i])

for i in part2:
    trainingdfold5 = trainingdfold5.append(articledf[i-1:i])
    
for i in part3:
    trainingdfold5 = trainingdfold5.append(articledf[i-1:i])
    
for i in part4:
    trainingdfold5 = trainingdfold5.append(articledf[i-1:i])
    
for i in part5:
    testingdfold5 = testingdfold5.append(articledf[i-1:i])


#kfold commented out and own (ineffecient) version implemented
#kf = cross_validation.KFold(articledf.shape[0], n_folds=5, random_state=1)

#scores = cross_validation.cross_val_score(alg, articledf[predictors], articledf["category index"],cv=kf)

#alg.fit(articledf[predictors], articledf["category index"])

alg1.fit(trainingdfold1[predictors], trainingdfold1["category index"])
    
#dont need to do every time
#dot_data = tree.export_graphviz(alg1, out_file=None)
#graph = pydotplus.graph_from_dot_data(dot_data)
#graph.write_pdf("tree.pdf")

prediction1 = alg1.predict(testingdfold1[predictors])

f1score1 = f1_score(testingdfold1["category index"], prediction1, average='macro')

alg2.fit(trainingdfold2[predictors], trainingdfold2["category index"])

prediction2 = alg2.predict(testingdfold2[predictors])

f1score2 = f1_score(testingdfold2["category index"], prediction2, average='macro')

alg3.fit(trainingdfold3[predictors], trainingdfold3["category index"])

prediction3 = alg3.predict(testingdfold3[predictors])

f1score3 = f1_score(testingdfold3["category index"], prediction3, average='macro')

alg4.fit(trainingdfold4[predictors], trainingdfold4["category index"])

prediction4 = alg4.predict(testingdfold4[predictors])

f1score4 = f1_score(testingdfold4["category index"], prediction4, average='macro')

alg5.fit(trainingdfold5[predictors], trainingdfold5["category index"])

prediction5 = alg5.predict(testingdfold5[predictors])

f1score5 = f1_score(testingdfold5["category index"], prediction5, average='macro')

alg12.fit(trainingdfold1[predictors], trainingdfold1["category index"])

prediction12 = alg12.predict(testingdfold1[predictors])

f1score12 = f1_score(testingdfold1["category index"], prediction12, average='macro')

alg22.fit(trainingdfold2[predictors], trainingdfold2["category index"])

prediction22 = alg22.predict(testingdfold2[predictors])

f1score22 = f1_score(testingdfold2["category index"], prediction22, average='macro')

alg32.fit(trainingdfold3[predictors], trainingdfold3["category index"])

prediction32 = alg32.predict(testingdfold3[predictors])

f1score32 = f1_score(testingdfold3["category index"], prediction32, average='macro')

alg42.fit(trainingdfold4[predictors], trainingdfold4["category index"])

prediction42 = alg42.predict(testingdfold4[predictors])

f1score42 = f1_score(testingdfold4["category index"], prediction42, average='macro')

alg52.fit(trainingdfold5[predictors], trainingdfold5["category index"])

prediction52 = alg52.predict(testingdfold5[predictors])

f1score52 = f1_score(testingdfold5["category index"], prediction52, average='macro')

result1 = prediction1 - testingdfold1["category index"]

result2 = prediction2 - testingdfold2["category index"]

result3 = prediction3 - testingdfold3["category index"]

result4 = prediction4 - testingdfold4["category index"]

result5 = prediction5 - testingdfold5["category index"]

result12 = prediction12 - testingdfold1["category index"]

result22 = prediction22 - testingdfold2["category index"]

result32 = prediction32 - testingdfold3["category index"]

result42 = prediction42 - testingdfold4["category index"]

result52 = prediction52 - testingdfold5["category index"]

scores = []
scores2 = []

right = 0

for x in result1:
    if x == 0:
        right+=1

scores.append(right/len(result1))

right = 0

for x in result2:
    if x == 0:
        right+=1

scores.append(right/len(result1))

right = 0

for x in result3:
    if x == 0:
        right+=1

scores.append(right/len(result1))


right = 0

for x in result4:
    if x == 0:
        right+=1

scores.append(right/len(result1))

right = 0

for x in result5:
    if x == 0:
        right+=1

scores.append(right/len(result1))

right = 0

for x in result12:
    if x == 0:
        right+=1

scores2.append(right/len(result1))

right = 0

for x in result22:
    if x == 0:
        right+=1

scores2.append(right/len(result1))

right = 0

for x in result32:
    if x == 0:
        right+=1

scores2.append(right/len(result1))


right = 0

for x in result42:
    if x == 0:
        right+=1

scores2.append(right/len(result1))

right = 0

for x in result52:
    if x == 0:
        right+=1

scores2.append(right/len(result1))
#predictions = alg.predict(articledf[predictors])

#Dec Tree results for accuracy
print(sum(scores)/len(scores))
#KNN results for accuracy
print(sum(scores2)/len(scores2))

treef1scores = []
treef1scores.append(f1score1)
treef1scores.append(f1score2)
treef1scores.append(f1score3)
treef1scores.append(f1score4)
treef1scores.append(f1score5)

knnf1scores = []
knnf1scores.append(f1score12)
knnf1scores.append(f1score22)
knnf1scores.append(f1score32)
knnf1scores.append(f1score42)
knnf1scores.append(f1score52)

#Dec Tree results for f score
print(sum(treef1scores)/len(treef1scores))
#KNN resutls for f score
print(sum(knnf1scores)/len(knnf1scores))


