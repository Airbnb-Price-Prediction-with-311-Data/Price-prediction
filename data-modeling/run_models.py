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
from allcolumns import columns

#airbnb_service_complaints = pd.read_csv("../dataset/Airbnb_Service_complaints.csv")
f=open("results/errors.csv", "a+")
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

#Feature Selection - None
filename = "../dataset/Airbnb_processed_try_1.csv"
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
filename = "../feature-selection/results/feature_selection_handpicking_v1.csv"
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
filename = "../feature-selection/results/feature_selection_correlation_v1.csv"
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
filename = "../feature-selection/results/reduced_data_rfe_v1.csv"
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
filename = "../feature-selection/results/forward_selection_intersection_v1.csv"
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
filename = "../feature-selection/results/forward_selection_top5_v1.csv"
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
filename = "../feature-selection/results/forward_selection_top10_v1.csv"
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
filename = "../feature-selection/results/forward_selection_top15_v1.csv"
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


'''
'None',
'Random Forest',  0.3542529602630437],
'Hand-picking', 'Linear Regression', 0.32840295063492975],
'Hand-picking', 'Ensemble',  0.2879174248843924],
'Hand-picking', 'XgBoost', 0.26716510577877184],
'Hand-picking', 'Knn', 0.3502145678340426],
'Hand-picking', 'Random Forest',0.3454682291378386],
'Filtering-Pearson Correlation', 'Linear Regression', 0.34407488516971496],
'Filtering-Pearson Correlation', 'Ensemble',  0.31453265423990917],
'Filtering-Pearson Correlation', 'XgBoost', 0.3189341080740337],
'Filtering-Pearson Correlation', 'Knn', 0.36908935549907823],
'Filtering-Pearson Correlation', 'Random Forest', 0.34487450246348667],
'Recursive Feature Elimination', 'Linear Regression', 0.32445242176847816],
'Recursive Feature Elimination', 'Ensemble',  0.2866705382171408],
'Recursive Feature Elimination', 'XgBoost', 0.27889186411391176],
'Recursive Feature Elimination', 'Knn', 0.35582669478689205],
'Recursive Feature Elimination', 'Random Forest', 0.3439807657381468],
'Forward Selection', 'Linear Regression', 0.3531028136181348],
'Forward Selection', 'Ensemble',  0.2852983178404548],
'Forward Selection', 'XgBoost', 0.27508785316309353],
'Forward Selection', 'Knn', 0.3434047632654581],
'Forward Selection', 'Random Forest', 0.3518038106524232],
'''


