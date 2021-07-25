# -*- coding: utf-8 -*-
"""
Generates histogram for training data.
"""

# Importing the required libraries
import numpy as np
import cv2
import os
from sklearn.cluster import MiniBatchKMeans

from miscload import create_histogram,loadBySurf

n_classes=36 #36 is ideal but this is ok
clustering_factor=6


def minibatchkmeans(k, descriptors_list):
  kmeans=MiniBatchKMeans(n_clusters=k)
  print("MiniBatchKMeans Initialized!")
  kmeans.fit(descriptors_list)
  print("Clusters Created!")
  visual_words=kmeans.cluster_centers_
  return visual_words, kmeans



surfs = loadBySurf('data/split/train',n_classes)#loadandsurf()
#print(len(train_images))

#print(len(train_images['a'][0][0]))

#Extracting surf features from each image stored in train_images list

all_train_descriptors=surfs[0]
train_descriptors_by_class=surfs[1]
#print(len(surfs[0]))
#print(len(surfs[1]['0'][1]))

# Calling MiniBatchkmeans function and getting central points
visual_words,kmeans=minibatchkmeans(n_classes*clustering_factor,all_train_descriptors)


# Calling create_histogram and getting histogram for each image
bows_train=create_histogram(train_descriptors_by_class,kmeans,n_classes,clustering_factor)

#print((bows_train['a'][0][1]))

# Saving .csv file
import csv
loc='files/train.csv'
with open(loc,'w',newline='') as file:
  writer=csv.writer(file)
  header=[]
  for i in range (n_classes*clustering_factor):
    header.append(str('pixel')+str(i))
  header.append('Label')
  writer.writerow(header)
  count=0
  for label in bows_train:
     # print(len(bows_train[label]))
    for i in range(len(bows_train[label])):
      list=[]
      l = len(bows_train[label][i])
      for j in range(l):
        list.append(bows_train[label][i][j])
      list.append(label)
      writer.writerow(list)


# pickle the kmeans
np.save('files/clusters.npy',kmeans.cluster_centers_)
# for test

test_folder='data/split/test'


surf_test = loadBySurf(test_folder,n_classes);
#print(len(surf_test['a'][0]))

all_test_descriptors=surf_test[0]
test_descriptors_by_class=surf_test[1]


# Create histograms from extracted surf features
bows_test=create_histogram(test_descriptors_by_class,kmeans,n_classes,clustering_factor)

import csv
loc='files/test.csv'
with open(loc,'w',newline='') as file:
  writer=csv.writer(file)
  header=[]
  for i in range (1,n_classes*clustering_factor+1):
    header.append(str('pixel')+str(i))
  header.append('Label')
  writer.writerow(header)
  count=0
  for label in bows_test:
    #print(len(bows_test[label]))
    for i in range(len(bows_test[label])):
      list=[]
      for j in range(l):
        list.append(bows_test[label][i][j])
      list.append(label)
      writer.writerow(list)


