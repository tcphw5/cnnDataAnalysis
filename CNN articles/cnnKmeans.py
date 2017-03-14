#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CNN k-means 

Created on Tue Mar  7 21:28:25 2017

@author: tp-mate
"""

import numpy as np
import pandas as pd
from nltk import cluster
from nltk.cluster import euclidean_distance
from nltk.cluster import cosine_distance
from sklearn.neighbors.dist_metrics import JaccardDistance
from nltk.metrics.distance import jaccard_distance
import matplotlib.pylab as plt
import matplotlib as mpl
from sklearn.manifold import MDS
from scipy import spatial



datamat = np.load('datamatrix.npy')
cosmat = np.load('COSmatrix.npy')
jacmat = np.load('JACmatrix.npy')
#need to remove index for computing k means
datamat2 = np.delete(datamat,0,1)

#categoriesIndex.txt has an extra 1 after index name
#not sure why it is needed but value is not actually
#used. just needed to push down values to right spot
#once added to articledf
categories = pd.read_csv('categoriesIndex.txt')

fileIN = 'Output2.txt'

featwords = np.genfromtxt(fileIN, dtype='U300', converters={0:lambda x: x.decode()})

articledf = pd.DataFrame(data=datamat[:,1:], index=datamat[:,0], columns=featwords[1:])

clusterer = cluster.KMeansClusterer(6, euclidean_distance, repeats=1)
results = clusterer.cluster(datamat2, True)
means1 = clusterer.means()

clusterer2 = cluster.KMeansClusterer(6, cosine_distance, repeats=1)
results2 = clusterer2.cluster(datamat2, True)
means2 = clusterer2.means()


clusterer3 = cluster.KMeansClusterer(6, spatial.distance.jaccard, repeats=1, avoid_empty_clusters=True, conv_test=1)
results3 = clusterer3.cluster(datamat2, True)
means3 = clusterer3.means()

kmeanSums1 = [0,0,0,0,0,0]
kmeanSums2 = [0,0,0,0,0,0]
kmeanSums3 = [0,0,0,0,0,0]

for kmean in range(6):
    for x in range(len(datamat2)):
        if results[x] == kmean:
            kmeanSums1[kmean] += euclidean_distance(datamat2[x], means1[kmean]) ** 2
            
for kmean in range(6):
    for x in range(len(datamat2)):
        if results2[x] == kmean:
            kmeanSums2[kmean] += cosine_distance(datamat2[x], means2[kmean]) ** 2

for kmean in range(6):
    for x in range(len(datamat2)):
        if results3[x] == kmean:
            kmeanSums3[kmean] += spatial.distance.jaccard(datamat2[x], means3[kmean]) ** 2
                      
print(sum(kmeanSums1))
print(sum(kmeanSums2))
print(sum(kmeanSums3))


MDS()

mds = MDS(n_components=2, dissimilarity="euclidean", random_state=1)

#mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)



pos = mds.fit_transform(datamat2)
#pos = mds.fit_transform(cosmat)
#pos = mds.fit_transform(jacmat)

xs, ys = pos[:, 0], pos[:, 1]

cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e', 5: '#9e1b42'}
cluster_names = {0: '0', 
                 1: '1', 
                 2: '2', 
                 3: '3', 
                 4: '4',
                 5: '5'}

indexes = [x+1 for x in range(105)]

df = pd.DataFrame(dict(x=xs, y=ys, label=results, title=indexes))

groups = df.groupby('label')

fig, ax = plt.subplots(figsize=(17,9))
ax.margins(0.05)

for name, group in groups:
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, 
            label=cluster_names[name], color=cluster_colors[name], 
            mec='none')
    ax.set_aspect('auto')
    ax.tick_params(\
        axis= 'x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelbottom='off')
    ax.tick_params(\
        axis= 'y',         # changes apply to the y-axis
        which='both',      # both major and minor ticks are affected
        left='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelleft='off')
    
ax.legend(numpoints=1)  #show legend with only 1 point

#add label in x,y position with the label as the film title
for i in range(len(df)):
    ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['title'], size=8)  

    
    
#plt.show() #show the plot

plt.savefig('clusters_small_noaxes.png', dpi=200)