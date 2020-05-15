import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import mean_squared_error
import csv
from allcolumns import columns

airbnb_service_complaints = pd.read_csv("../dataset/Airbnb_Service_complaints.csv")

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

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows) 

airbnb_perservice()