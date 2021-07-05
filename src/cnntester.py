
import tensorflow as tf;
import numpy as np;
import cv2;
from sklearn.preprocessing import LabelEncoder
from skinDetector import skinDetector

# cv2.VideoCapture()
# pick up saved label encoder
encoder = LabelEncoder()
encoder.classes_ = np.load('files/classes.npy')

sk = skinDetector(1)

img = cv2.imread('/home/atreyab/Pictures/capt0000.jpg');
img = sk.segment(img)
cv2.imwrite('test.jpg',img)
img = cv2.resize(img,(100,100));
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgs = np.array([img]).reshape((-1,100,100,1));
model  = tf.keras.models.load_model('Saved/model');

predictions = model.predict(imgs);

print(predictions)
print(encoder.inverse_transform(np.array(list(range(0,35)))))
print(encoder.inverse_transform(np.array([24])))