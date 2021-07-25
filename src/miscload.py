import cv2;
import os;
import numpy as np;

def loadBySurf(folder:str,n_classes:int):
  """
  Load and add surf features
  """
  features_dict={}
  orb_descriptors_class_by_class={}
  orb_descriptors_list=[]
  orb = cv2.KAZE_create()

  for (i,label) in enumerate(os.listdir(folder)):
    print(label," started",i,n_classes,end='\r')
    category=[]
    features=[]
    path=folder+'/'+label
    for image in os.listdir(path):
      img=cv2.imread(path+'/'+image)
      #new_img=cv2.resize(img,(128,128))
      if img is None:
        print("Skipping random ",image)
        continue;
      category.append(img);
    print(label, " feature")
    for (i,img) in enumerate(category):
      # hide for perf
      # print(label+str(i),end='\r')
      kp = orb.detect(img,None)
      # compute the descriptors with surf
      kp, desc = orb.compute(img, kp)
      if desc is None:
        print("Blank for",label,i,"!");
        desc = np.array([]).reshape(1,-1)
      else:
        orb_descriptors_list.extend(desc)
        features.append(desc)
    orb_descriptors_class_by_class[label]=features
  return [orb_descriptors_list,orb_descriptors_class_by_class]

def create_histogram(all_descs,kmeans,n_classes:int,clustering_factor:int):
  """
  Create histograms
  """
  features_dict={}
  for key,value in all_descs.items():
    print(key," Started!")
    category=[]
    for desc in value:
      raw_words=kmeans.predict(desc.astype(np.float))#desc)
      hist = np.array(np.bincount(raw_words,minlength=n_classes*clustering_factor))
      category.append(hist)
    features_dict[key]=category
    print(key," Completed!")
  return features_dict


