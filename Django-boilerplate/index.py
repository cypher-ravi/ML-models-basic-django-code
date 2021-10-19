import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import LeaveOneOut

loo = LeaveOneOut()
df=pd. read_csv(r'C:\Users\Dell\Desktop\EMG-data.csv')
df=df.drop(columns=["time"])
Class = df["class"]
index_numbers_1=df[df["class"]==0].index 
index_numbers_1.shape
index_numbers_2=df[df["class"]==7].index
df.drop(index_numbers_1,inplace=True)
df.drop(index_numbers_2,inplace=True)
df=df.groupby(['label','class'])
def rms(data): ##root mean square
      return  np.sqrt(np.mean(data**2,axis=0))  

def SSI(data): ##Simple Square Integral
    return np.sum(data**2,axis=0)

def abs_diffs_signal(data): ##absolute differential signal
    return np.sum(np.abs(np.diff(data,axis=0)),axis=0)


def print_estimator_name(estimator):
    return estimator.__class__.__name__
df=df.agg(['min','max',rms,SSI,abs_diffs_signal,np.ptp])
df=df.reset_index()
temp2=df
svc=SVC(C=100,kernel='poly',gamma=0.01,decision_function_shape='ovo')
features=df.drop(columns=["label","class"])
labels=df["class"]
X_train, X_test,y_train,y_test= train_test_split(features,labels,test_size=0.30, random_state=0)
mean = X_train.mean(axis=0)
std = X_train.std(axis=0)
X_train -= mean
X_train /= std
X_test -= mean
X_test /= std
svc.fit(X_train,y_train)
# output
y_test_pred=svc.predict(X_test)





# def output():
#     with open('templates/index.csv', 'r') as file:

#     predict_data = svc.predict(data)
#     return predict_data