import pandas as pd
import numpy as np
import sklearn
import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor
import csv
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn import ensemble
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score
from feature_selection.allcolumns import columns



def airbnb_perservice(model , filename):
    fields = ['Complaint_type','Error','Accuracy']
    rows = []
    #filename = "linear_reg_error.csv"
    #model = linear_model.LinearRegression()
    complaints = {}
    airbnb_subset = airbnb_service_complaints.copy()
    for col in columns:
        airbnb_subset.drop([col], axis=1, inplace=True)

    #print (airbnb_subset.columns)
    y = airbnb_subset.price
    airbnb_subset.drop(['price', 'zipcode', 'total_count', 'name', 'host_name'], axis=1, inplace=True)
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
        # print (mean_squared_error(y_test, y_pred))
        # print ("ERROR")
    # print (complaints)   

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)



def forward_selection_main():
    

    #Linear regression
    filename = "feature_selection/results/linear_reg_error.csv"
    model = linear_model.LinearRegression()
    airbnb_perservice(model,filename)

    #Ensemble Boosting
    filename = "feature_selection/results/ensembleboosting_regressor_error.csv"
    model =  ensemble.GradientBoostingRegressor()
    airbnb_perservice(model,filename)

    #XGBoosting
    filename = "feature_selection/results/xgboost_regressor_error.csv"
    model = xgb.XGBRegressor() 
    airbnb_perservice(model,filename)

    #Random Forest
    filename = "feature_selection/results/Random_forest_error.csv"
    model = RandomForestRegressor(max_depth=2, random_state=0)
    airbnb_perservice(model,filename)

    #Knn pending 
    # filename = "results/linear_reg_error.csv"
    # model = linear_model.LinearRegression()
    # airbnb_perservice(model,filename)


airbnb_service_complaints = pd.read_csv("dataset/Airbnb_Service_complaints_merged.csv")
