import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso
from sklearn.metrics import mean_squared_error


def make_subset(): 
    airbnb_complaints = pd.read_csv('../dataset/Airbnb_Service_complaints_merged.csv')
    numerical_features = airbnb_complaints.select_dtypes(exclude=['object'])
    y = numerical_features.price
    numerical_features.drop(['price'], axis=1, inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(numerical_features, y, test_size=0.2)
    model = LinearRegression()
    #Initializing RFE model
    rfe = RFE(model, 28)
    #Transforming data using RFE
    X_rfe = rfe.fit_transform(X_train,y_train)  
    #Fitting the data to model
    model.fit(X_rfe,y_train)
    X_test = rfe.fit_transform(X_test,y_test)  
    i = 0
    list = []
    for e in rfe.support_:
        if (e):
            list.append(i)
        i+=1
    r = []
    for e in list:
        r.append(numerical_features.columns[e])
    r.append('price')
    relevant_set = set(r)
    airbnb_complaints.columns
    for x in airbnb_complaints.columns:
        if(x not in relevant_set):
            airbnb_complaints.drop([x],axis=1,inplace=True)
    airbnb_complaints.to_csv('results/reduced_data_rfe_v1.csv', index=False)



make_subset()