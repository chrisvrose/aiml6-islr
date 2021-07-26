# -*- coding: utf-8 -*-
"""
Generates histogram for testing data using KMeans from them.
"""

# Importing the required libraries
"""
1. resized/cropped
2. skin mask
3. features ext
4. create a bow
5. 
"""
import numpy as np
import cv2
import os
import pickle
import sys
from scipy import ndimage
from scipy.spatial import distance
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import LabelEncoder

from skinDetector import skinDetector;

from miscload import loadBySurf,create_histogram

# config
n_classes=36
clustering_factor=6
# skin detector
skd = skinDetector(1);

# label encoder
le=LabelEncoder()
le.classes_ = np.load('files/classes.npy')


# kaze imgdetector
kaze = cv2.KAZE_create()

# models
with open('Saved/svm/svm.pkl', 'rb') as f1,open('Saved/nbc/nbc.pkl', 'rb') as f2,open('Saved/knn/knn.pkl','rb') as f3:
  svm = pickle.load(f1)
  nbc = pickle.load(f2)
  knn = pickle.load(f3)
# km
kmeans=MiniBatchKMeans(n_clusters=n_classes*clustering_factor)
kmeans.cluster_centers_ = np.load('files/clusters.npy')
# test_folder='data/split/test'

# Loading Test images
# test_images=load_images_by_category('data/split/test')
# camera = cv2.VideoCapture(2)

# k,img = camera.read()
def inference(img):
  # img = 
  img = skd.segment(img)
  img = cv2.resize(img, (128, 128));
  kp = kaze.detect(img,None);
  # cv2.imshow('0',img)
  # cv2.waitKey(1000)
  # compute the descriptors with surf
  print(kp)
  kp, desc = kaze.compute(img, kp)
  if desc is None:
    return le.inverse_transform([[23],[23],[23]]).tolist()
  
  raw_words = kmeans.predict(desc.astype(np.float))
  hist = np.array(np.bincount(raw_words,minlength=n_classes*clustering_factor))

  # print(kp)

  hist = np.reshape(hist,(1,-1))


  #Extract SURF features from the image
  # surf_test=surf_features(test_images)[1]
  # surf_test = loadBySurf(test_folder,n_classes);
  # print(len(surf_test[0]))

  # load saved classes
  
  # print('loaded label encodings')

  res = np.array( svm.predict(hist))
  res = np.append(res,
    nbc.predict(hist)
  )
  res = np.append(res,
    knn.predict(hist)

  )

  res = res.reshape(3,1)
  res2 = le.inverse_transform(res)
  print(res);
  return res2.tolist();

# Create histograms from extracted surf features
# bows_test=create_histogram(surf_test,kmeans,n_classes,clustering_factor)
if __name__=='__main__':
  inference(cv2.imread('20210725_225733.jpg'))

# import csv
# loc='cnn files/test.csv'
# with open(loc,'w',newline='') as file:
#   writer=csv.writer(file)
#   header=[]
#   for i in range (1,n_classes*clustering_factor+1):
#     header.append(str('pixel')+str(i))
#   header.append('Label')
#   writer.writerow(header)
#   count=0
#   for label in bows_test:
#     #print(len(bows_test[label]))
#     for i in range(len(bows_test[label])):
#       list=[]
#       for j in range(150):
#         list.append(bows_test[label][i][j])
#       list.append(label)
#       writer.writerow(list)
