import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
import seaborn as sbn

data=pd.read_csv('files/train.csv',low_memory=False)
data.head()

test=pd.read_csv('files/test.csv',low_memory=False)
test.head()

x=data.iloc[:,0:-1]
y=data.iloc[:,-1]

# load saved classes
le=LabelEncoder()
le.classes_ = np.load('files/classes.npy')
y=le.transform(y)

x_test=test.iloc[:,0:-1]
y_test=test.iloc[:,-1]

y_test=le.transform(y_test)

# Choosing a K value
start_range:int =3
use:int = 7
outer_range:int = 20
accuracy_rate=[]
for i in range(3,outer_range,2):
  print('For i=',i)
  knn=KNeighborsClassifier(n_neighbors=i)
  score=cross_val_score(knn,x,y,cv=10)
  accuracy_rate.append(score.mean())

# Plotting accuracy with different values of k

plt.figure(figsize=(10,6))
plt.plot(range(start_range,outer_range,2),accuracy_rate,color='blue',linestyle='dashed',marker='o',markerfacecolor='red',markersize=10)
plt.title("Accuracy_score vs K value")
plt.show()


print('Running for 3NN')
knn=KNeighborsClassifier(n_neighbors=use)

knn.fit(x,y)


import pickle
file_name='Saved/knn/knn.pkl'
outfile=open(file_name,'wb')
pickle.dump(knn,outfile)
outfile.close()

y_pred=knn.predict(x_test)

print(accuracy_score(y_test,y_pred))

c_m=confusion_matrix(y_test,y_pred)

print(classification_report(y_test,y_pred))

plt.figure(figsize=(20,17))
plt.title("Confusion Matrix for K Nearest Neighbour")
df_cm=pd.DataFrame(c_m)
sbn.heatmap(df_cm,annot=True);plt.show()

