# from 'data/combined', resize and segment the images, then split to test and train -> creating the data/split folder

import os
import cv2
from skinDetector import skinDetector
import random
folder = 'data/combined'
newfolderTrain = 'data/split/train'
newfolderTest = 'data/split/test'

traincnt=0;
testcnt=0

train_data = []
# tried 2, picks out too much
skd = skinDetector(1);
for label in os.listdir(folder):
    print(label, " started")
    path = folder+'/'+label
    for imgname in os.listdir(path):
        if not imgname.endswith('.jpg'):
            continue;
        img = cv2.imread(path+'/'+imgname)
        # by shadowing we drop the older variable
        img = cv2.resize(img, (128, 128));
        img = skd.segment(img);
        rndImg = random.randint(0,9)
        pth = newfolderTrain if rndImg<8 else newfolderTest
        if rndImg<8:
            traincnt +=1;
        else:
            testcnt +=1;
        # new_img = cv2.resize(img, (100, 100))
        # print(newfolder+'/'+label+'/'+imgname)
        cv2.imwrite(pth+'/'+label+'/'+imgname,img)

    print(label, " done")
print("Stats",traincnt,testcnt)