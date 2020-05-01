import pandas as pd
import numpy as np
import sklearn
import csv
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score
from allcolumns import columns
airbnb_service_complaints = pd.read_csv("Airbnb_Service_complaints.csv")


def airbnb_allservices():
    numerical_features =  airbnb_service_complaints.select_dtypes(exclude=['object'])
    #categorical_features = airbnb_service_complaints.select_dtypes(include=['object'])
    y = numerical_features.price
    numerical_features.drop(['price'], axis=1, inplace=True)
    numerical_features.drop(['count'], axis=1, inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(numerical_features, y, test_size=0.2)
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_test)
    print ("LINEAR REGRESSION ON ENTIRE DATASET")
    print ("ERROR")
    print (mean_squared_error(y_test, y_pred))
    print ("ACCURACY")
    print (1- mean_squared_error(y_test, y_pred))

def airbnb_perservice():
    fields = ['Complaint_type','Error','Accuracy']
    rows = []
    filename = "linear_reg_error.csv"
    model = linear_model.LinearRegression()
    complaints = {}
    airbnb_subset = airbnb_service_complaints.copy()
    for col in columns:
        airbnb_subset.drop([col], axis=1, inplace=True)
    y = airbnb_service_complaints.price
    airbnb_subset.drop(['latitude', 'longitude', 'count', 'total_count', 'price'], axis=1, inplace=True)
    
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
    print (complaints)   

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


airbnb_allservices()
airbnb_perservice()
