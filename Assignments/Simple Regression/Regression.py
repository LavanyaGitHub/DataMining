# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:57:15 2017

@author: Lavanya 
"""
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import dataset
dataset = pd.read_csv('Regression.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
#into training set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.1,random_state=0)
#fit simple linear regression to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
#predicting the Test set Results
y_pred = regressor.predict(X_test)
#Visualizing the training set results 
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Rate Vs Price(Training set)')
plt.xlabel('interest')
plt.ylabel('price')
plt.show()
#Visualizing the training set results 
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Rate Vs Price(Test set)')
plt.xlabel('interest')
plt.ylabel('price')
plt.show()
