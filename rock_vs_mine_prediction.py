 # -*- coding: utf-8 -*-
"""Rock vs Mine  Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WyaZV0wl6A2QBcnWQN52tU2ocUgATxLE

Importing Dependecies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data collection and loading data"""

#loading the dataset to a pandas Dataframe
sonar_data = pd.read_csv('./data/sonar data - Copy of sonar data.csv', header=None)

sonar_data.head()

# Number of rows and columns
sonar_data.shape

sonar_data.describe() # describe ---> stastical measures of the data

sonar_data[60].value_counts() # Numbers of values per label Rock and Mine - IMPORTANT to have almost equal values between labels

# Separate data and Label

X  = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

print(X)
print(Y)

"""Training and Test Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.1, stratify=Y, random_state =1)
# test_size = 0.1 ---> 10% of data to be test data

X_train = X_train.apply(pd.to_numeric, errors='coerce')
X_test = X_test.apply(pd.to_numeric, errors='coerce')

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

print(X.shape, X_train.shape, X_test.shape)

print(X_train)
print(Y_train)

"""Model Training --> Logistic Regression"""

model = LogisticRegression()

# Training the Logistic regression Model with training Data

model.fit(X_train, Y_train)

"""Model Evaluation"""

# Accurancy on the training data
X_train_prediction = model.predict(X_train)
training_data_accurancy = accuracy_score(X_train_prediction, Y_train)
print(training_data_accurancy)

# Accurancy on the test data

X_test_prediction = model.predict(X_test)
test_data_accurancy = accuracy_score(X_test_prediction, Y_test)
print(test_data_accurancy)

"""Making a predict system"""

input_data = (0.0307,0.0523,0.0653,0.0521,0.0611,0.0577,0.0665,0.0664,0.1460,0.2792,0.3877,0.4992,0.4981,0.4972,0.5607,0.7339,0.8230,0.9173,0.9975,0.9911,0.8240,0.6498,0.5980,0.4862,0.3150,0.1543,0.0989,0.0284,0.1008,0.2636,0.2694,0.2930,0.2925,0.3998,0.3660,0.3172,0.4609,0.4374,0.1820,0.3376,0.6202,0.4448,0.1863,0.1420,0.0589,0.0576,0.0672,0.0269,0.0245,0.0190,0.0063,0.0321,0.0189,0.0137,0.0277,0.0152,0.0052,0.0121,0.0124,0.0055)
# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the np array as we are predicting for one instance
input_data_as_numpy_array = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_as_numpy_array)
print(prediction)

if (prediction[0] == 'R'):
    print('The object is a Rock')
else:
   print('The Object is a Main')