# -*- coding: utf-8 -*-
"""Horse_speed_predictor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uEcApLua4l0WxCatM3cUPMBruKvuOU1k
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

ds = pd.read_csv('run_race.csv')
ds.head()

ds.isnull().any()

ds.shape

ds = ds.dropna()
ds.shape

pred_speed = ds[['horse_type','config','horse_age','horse_weight','rider_weight','surface','average_speed']]
pred_speed.head()

#ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0,1])], remainder='passthrough')
#X = np.array(ct.fit_transform(X))

htype = LabelEncoder()
pred_speed['horse_type'] = htype.fit_transform(pred_speed['horse_type'])
pred_speed['horse_type'].unique()

config = LabelEncoder()
pred_speed['config'] = config.fit_transform(pred_speed['config'])
pred_speed['config'].unique()

pred_speed.head()

X = pred_speed.iloc[:,0:6].values
Y = pred_speed.iloc[:, -1].values

#from sklearn.model_selection import train_test_split
#X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size = 0.01, random_state=0)

from sklearn.linear_model import LinearRegression
linearReg = LinearRegression()
linearReg.fit(X,Y)

Y_pred = linearReg.predict(X)
np.set_printoptions(precision=5)
print(np.concatenate((Y_pred.reshape(len(Y_pred),1),Y.reshape(len(Y),1)),1))

print("Accuracy: {}".format(linearReg.score(X,Y)))

linearReg.predict([[2,3,3,1018.0, 128.0, 0]])

X = np.array([["Gelding","A",8,1156,141,0]])
X

X[:,0] = htype.transform(X[:,0])
X[:,1] = config.transform(X[:,1])
X = X.astype(float)
X

Y_pred = linearReg.predict(X)
Y_pred

data = {"model" : linearReg, "horse_type" : htype, "config" : config} #Dictionary
with open('speed_predictor.pkl', 'wb') as file:
  pickle.dump(data,file)

with open('speed_predictor.pkl', 'rb') as file:
  pickle.load(file)

linearReg_loaded = data["model"]
htype = data["horse_type"]
config = data["config"]

Y_pred = linearReg_loaded.predict(X)
Y_pred