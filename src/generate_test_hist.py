# -*- coding: utf-8 -*-
"""
Generates histogram for testing data using KMeans from them.
"""

# Importing the required libraries

import numpy as np
import cv2
import os
import pickle
import sys
from scipy import ndimage
from scipy.spatial import distance
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans

from miscload import  loadBySurf

n_classes=36
clustering_factor=6

test_folder='ISL Datasets/Train-Test/Test'

# Loading Test images
# test_images=load_images_by_category(test_folder)

# #Extract SURF features from the image
# surf_test=surf_features(test_images)[1]
surf_test = loadBySurf(test_folder,n_classes);
#print(len(surf_test['a'][0]))


def create_histogram(all_bows,kmeans):
  features_dict={}
  for key,value in all_bows.items():
    print(key," Started!")
    category=[]
    for desc in value:
      visual_words=kmeans.predict(desc)
      hist = np.array(np.bincount(visual_words,minlength=n_classes*clustering_factor))
      category.append(hist)
    features_dict[key]=category
    print(key," Completed!")
  return features_dict


# Create histograms from extracted surf features
bows_test=create_histogram(surf_test,kmeans,n_classes,clustering_factor)

import csv
loc='cnn files/test.csv'
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
      for j in range(150):
        list.append(bows_test[label][i][j])
      list.append(label)
      writer.writerow(list)