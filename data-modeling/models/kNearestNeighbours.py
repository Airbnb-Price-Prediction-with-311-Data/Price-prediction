import pandas as pd
import numpy as np
import sklearn
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score
from sklearn.neighbors import NearestNeighbors
import csv
from allcolums import columns


airbnb_service_complaints = pd.read_csv("Airbnb_Service_complaints.csv")

def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

def knn(airbnb_service_complaints): 
    numerical_features = airbnb_service_complaints.select_dtypes(exclude=[
                                                                 'object'])
    y = numerical_features.price
    numerical_features.drop(['price'], axis=1, inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(
        numerical_features, y, test_size=0.2)
    train = X_train.to_numpy()
    test = X_test.to_numpy()
    train_price = y_train.to_numpy()
    y_pred_np = []
    k = 5
    for test_datapoint in test:
        dist = []
        for train_datapoint in train:
            dist.append(euclidean_distance(test_datapoint , train_datapoint))
            
        idx = np.argpartition(dist,k)
        sum = 0 
        for i in range(k):
            sum += train_price[idx[i]]
        y_pred_np.append(sum/k)

    y_pred = pd.DataFrame(data = y_pred_np)
    return mean_squared_error(y_test, y_pred) , 1-mean_squared_error(y_test, y_pred)


def airbnb_perservice():

    fields = ['Complaint_type','Error','Accuracy']
    rows = []
    filename = "knn_error_trial.csv"
    complaints = {}
    airbnb_subset = airbnb_service_complaints.copy()
    for col in columns:
        airbnb_subset.drop([col], axis=1, inplace=True)
    airbnb_subset.drop(['total_count'], axis=1, inplace=True)
    y = airbnb_service_complaints.price
    for col in columns:
        row = []
        complaint = airbnb_service_complaints[col]
        airbnb_subset[col] = complaint
        error,accuracy = knn(airbnb_subset)
        row.append(col)
        row.append(error)
        row.append(accuracy)
        rows.append(row)
    print(complaints)

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


a,b = knn(airbnb_service_complaints)
airbnb_perservice()
