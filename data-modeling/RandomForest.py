import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import mean_squared_error
import csv
from allcolumns import columns

airbnb_service_complaints = pd.read_csv("../dataset/Airbnb_Service_complaints.csv")


def airbnb_allservices():
    numerical_features =  airbnb_service_complaints.select_dtypes(exclude=['object'])
    categorical_features = airbnb_service_complaints.select_dtypes(include=['object'])
    categorical_features_one_hot = pd.get_dummies(categorical_features)
    X = np.concatenate((numerical_features, categorical_features_one_hot), axis=1)
    y = numerical_features.price
    numerical_features.drop(['price'], axis=1, inplace=True)
    #numerical_features.drop(['count'], axis=1, inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    regr = RandomForestRegressor(max_depth=2, random_state=0)
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_test)
    print ("RANDOM FOREST ON ENTIRE DATASET")
    print ("ERROR")
    print (mean_squared_error(y_test, y_pred))
    print ("ACCURACY")
    print (1- mean_squared_error(y_test, y_pred))

def airbnb_perservice():
    fields = ['Complaint_type','Error','Accuracy']
    rows = []
    filename = "Random_forest_error.csv"
    model = RandomForestRegressor(max_depth=2, random_state=0)
    complaints = {}
    airbnb_subset = airbnb_service_complaints.copy()
    for col in columns:
        airbnb_subset.drop([col], axis=1, inplace=True)
    y = airbnb_service_complaints.price
    airbnb_subset.drop(['total_count', 'price'], axis=1, inplace=True)
    
    for col in columns:
        row = []
        complaint = airbnb_service_complaints[col]
        airbnb_subset[col] = complaint
        numerical_features = airbnb_subset.select_dtypes(exclude=['object'])
        X_train, X_test, y_train, y_test = train_test_split(numerical_features, y, test_size=0.2)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        airbnb_subset.drop([col], axis=1, inplace=True)
        complaints[col] = mean_squared_error(y_test, y_pred)
        row.append(col)
        row.append(mean_squared_error(y_test, y_pred))
        row.append(1-mean_squared_error(y_test, y_pred))
        rows.append(row)
    complaints = {k: v for k, v in sorted(complaints.items(), key=lambda item: item[1])}
    print (complaints)  

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows) 

airbnb_allservices()
#airbnb_perservice()