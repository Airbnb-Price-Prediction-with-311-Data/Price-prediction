import keras
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error 
import pandas as pd
import numpy as np
import warnings 
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', category=DeprecationWarning)

airbnb_service_complaints = pd.read_csv("Airbnb_Service_complaints.csv")

columns = ['Bus Stop Shelter Complaint', 'Bus Stop Shelter Placement', 'City Vehicle Placard Complaint', 'Collection Truck Noise',
 'Construction', 'Construction Lead Dust', 'Construction Safety Enforcement', 'Consumer Complaint', 'Cranes and Derricks', 'Curb Condition',
 'DOF Property - Payment Issue', 'DOOR/WINDOW', 'DPR Internal', 'DRIE', 'Damaged Tree', 'Day Care', 'Dead Tree', 'Dead/Dying Tree',
 'Derelict Bicycle']
numerical_features =  airbnb_service_complaints.select_dtypes(exclude=['object'])
y = numerical_features.price

#NN_model = Sequential()

# The Input Layer :
#NN_model.add(Dense(128, kernel_initializer='normal',input_dim = numerical_features.shape[1], activation='relu'))

# The Hidden Layers :
#NN_model.add(Dense(256, kernel_initializer='normal',activation='relu'))
#NN_model.add(Dense(256, kernel_initializer='normal',activation='relu'))
#NN_model.add(Dense(256, kernel_initializer='normal',activation='relu'))

# The Output Layer :
#NN_model.add(Dense(1, kernel_initializer='normal',activation='linear'))

# Compile the network :
#NN_model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])
#NN_model.summary()

#NN_model.fit(numerical_features, y, epochs=25, batch_size=32, validation_split = 0.2)
complaints = {}
airbnb_subset = airbnb_service_complaints.copy()
for col in columns:
    airbnb_subset.drop([col], axis=1, inplace=True)
airbnb_subset.drop(['latitude', 'longitude', 'count', 'total_count'], axis=1, inplace=True)
for col in columns:
    print (col)
    complaint = airbnb_service_complaints[col]
    airbnb_subset[col] = complaint
    numerical_features = airbnb_subset.select_dtypes(exclude=['object'])
    NN_model = Sequential()
    NN_model.add(Dense(128, kernel_initializer='normal',input_dim = numerical_features.shape[1], activation='relu'))
    # The Hidden Layers :
    NN_model.add(Dense(256, kernel_initializer='normal',activation='relu'))
    NN_model.add(Dense(256, kernel_initializer='normal',activation='relu'))
    NN_model.add(Dense(256, kernel_initializer='normal',activation='relu'))
    # The Output Layer :
    NN_model.add(Dense(1, kernel_initializer='normal',activation='linear'))
    # Compile the network :
    NN_model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])
    #NN_model.summary()
    NN_model.fit(numerical_features, y, epochs=25, batch_size=32, validation_split = 0.2)