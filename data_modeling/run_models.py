import pandas as pd
import numpy as np
import sklearn
import csv
import xgboost as xgb
from sklearn import ensemble
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score
from data_modeling.allcolumns import columns

#airbnb_service_complaints = pd.read_csv("../dataset/Airbnb_Service_complaints.csv")
f=open("data_modeling/results/errors.csv", "a+")
f.writelines("Method"+","+"model_name"+","+"RMSE"+"\n")

def airbnb_allservices(filename, model ,ft_sel_name, model_name):
    airbnb_service_complaints = pd.read_csv(filename)
    numerical_features = airbnb_service_complaints.select_dtypes(exclude=['object'])
    y = numerical_features.price
    numerical_features.drop(['price'], axis=1, inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(numerical_features, y, test_size=0.2)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    f.writelines(ft_sel_name+","+model_name+","+str(mean_squared_error(y_test, y_pred))+"\n")


def run_models_main():
#Feature Selection - None
    filename = "dataset/Airbnb_processed.csv"
    ft_sel_name = 'None'

    model_name = 'Linear Regression'
    model = linear_model.LinearRegression()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Ensemble'
    model = ensemble.GradientBoostingRegressor()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'XgBoost'
    model = xgb.XGBRegressor() 
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Random Forest'
    model = RandomForestRegressor(max_depth=2, random_state=0)
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    #Feature Selection - Hand Picking
    filename = "feature_selection/results/feature_selection_handpicking.csv"
    ft_sel_name = 'Hand-Picking'

    model_name = 'Linear Regression'
    model = linear_model.LinearRegression()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Ensemble'
    model = ensemble.GradientBoostingRegressor()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'XgBoost'
    model = xgb.XGBRegressor() 
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Random Forest'
    model = RandomForestRegressor(max_depth=2, random_state=0)
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    #Feature Selection - Pearson Correlation
    filename = "feature_selection/results/feature_selection_correlation.csv"
    ft_sel_name = 'Filtering-Pearson Correlation'

    model_name = 'Linear Regression'
    model = linear_model.LinearRegression()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Ensemble'
    model = ensemble.GradientBoostingRegressor()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'XgBoost'
    model = xgb.XGBRegressor() 
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Random Forest'
    model = RandomForestRegressor(max_depth=2, random_state=0)
    airbnb_allservices(filename, model, ft_sel_name, model_name)


    #Feature Selection - Recursive Feature Elimination
    filename = "feature_selection/results/reduced_data_rfe_v1.csv"
    ft_sel_name = 'Recursive Feature Elimination'

    model_name = 'Linear Regression'
    model = linear_model.LinearRegression()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Ensemble'
    model = ensemble.GradientBoostingRegressor()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'XgBoost'
    model = xgb.XGBRegressor() 
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Random Forest'
    model = RandomForestRegressor(max_depth=2, random_state=0)
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    #Feature Selection - Forward Selection Intersection
    filename = "feature_selection/results/forward_selection_intersection.csv"
    ft_sel_name = 'Forward Selection Intersection'

    model_name = 'Linear Regression'
    model = linear_model.LinearRegression()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Ensemble'
    model = ensemble.GradientBoostingRegressor()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'XgBoost'
    model = xgb.XGBRegressor() 
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Random Forest'
    model = RandomForestRegressor(max_depth=2, random_state=0)
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    #Feature Selection - Forward Selection lowest 5 per complaint
    filename = "feature_selection/results/forward_selection_top5.csv"
    ft_sel_name = 'Forward Selection(5)'

    model_name = 'Linear Regression'
    model = linear_model.LinearRegression()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Ensemble'
    model = ensemble.GradientBoostingRegressor()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'XgBoost'
    model = xgb.XGBRegressor() 
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Random Forest'
    model = RandomForestRegressor(max_depth=2, random_state=0)
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    #Feature Selection - Forward Selection lowest 10 per complaint
    filename = "feature_selection/results/forward_selection_top10.csv"
    ft_sel_name = 'Forward Selection(10)'

    model_name = 'Linear Regression'
    model = linear_model.LinearRegression()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Ensemble'
    model = ensemble.GradientBoostingRegressor()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'XgBoost'
    model = xgb.XGBRegressor() 
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Random Forest'
    model = RandomForestRegressor(max_depth=2, random_state=0)
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    #Feature Selection - Forward Selection lowest 15 per complaint
    filename = "feature_selection/results/forward_selection_top15.csv"
    ft_sel_name = 'Forward Selection(15)'

    model_name = 'Linear Regression'
    model = linear_model.LinearRegression()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Ensemble'
    model = ensemble.GradientBoostingRegressor()
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'XgBoost'
    model = xgb.XGBRegressor() 
    airbnb_allservices(filename, model, ft_sel_name, model_name)

    model_name = 'Random Forest'
    model = RandomForestRegressor(max_depth=2, random_state=0)
    airbnb_allservices(filename, model, ft_sel_name, model_name)



