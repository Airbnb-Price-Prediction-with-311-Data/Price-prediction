import pandas as pd
import numpy as np
import sklearn
import csv
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score
from allcolumns import columns

airbnb_service_complaints = pd.read_csv("../dataset/Airbnb_Service_complaints.csv")
f=open("results/errors.csv", "a+")

def airbnb_allservices(airbnb_service_complaints, model ,ft_sel_name, model_name):
    numerical_features =  airbnb_service_complaints.select_dtypes(exclude=['object'])
    y = numerical_features.price
    numerical_features.drop(['price'], axis=1, inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(numerical_features, y, test_size=0.2)
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_test)
    # print ("LINEAR REGRESSION ON ENTIRE DATASET")
    # print ("ERROR")
    f.writelines(ft_sel_name+","+model_name+","+str(mean_squared_error(y_test, y_pred))+"\n")


#airbnb_allservices()
#Feature Selection - NONE
ft_sel_name = 'None'
model_name = 'Linear Regression'
# call fn 

ft_sel_name = 'None'
model_name = 'Ensemble'


ft_sel_name = 'None'
model_name = 'XgBoost'


ft_sel_name = 'None'
model_name = 'Knn'


ft_sel_name = 'None'
model_name = 'Random Forest' 







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
 



#Feature Selection - RFE
ft_sel_name = 'Recursive Feature Elimination'
model_name = 'Linear Regression'
# call fn 

ft_sel_name = 'Recursive Feature Elimination'
model_name = 'Ensemble'


ft_sel_name = 'Recursive Feature Elimination'
model_name = 'XgBoost'


ft_sel_name = 'Recursive Feature Elimination'
model_name = 'Knn'


ft_sel_name = 'Recursive Feature Elimination'
model_name = 'Random Forest' 


#Feature Selection - Corr

ft_sel_name = 'Filtering-Pearson Correlation'
model_name = 'Linear Regression'
# call fn 

ft_sel_name = 'Filtering-Pearson Correlation'
model_name = 'Ensemble'


ft_sel_name = 'Filtering-Pearson Correlation'
model_name = 'XgBoost'


ft_sel_name = 'Filtering-Pearson Correlation'
model_name = 'Knn'


ft_sel_name = 'Filtering-Pearson Correlation'
model_name = 'Random Forest' 



#Feature Selection - Fwd sel
ft_sel_name = 'Forward Selection'
model_name = 'Linear Regression'
# call fn 

ft_sel_name = 'Forward Selection'
model_name = 'Ensemble'


ft_sel_name = 'Forward Selection'
model_name = 'XgBoost'


ft_sel_name = 'Forward Selection'
model_name = 'Knn'


ft_sel_name = 'Forward Selection'
model_name = 'Random Forest' 




#Feature Selection - hand picking 

ft_sel_name = 'Hand-picking'
model_name = 'Linear Regression'
# call fn 

ft_sel_name = 'Hand-picking'
model_name = 'Ensemble'


ft_sel_name = 'Hand-picking'
model_name = 'XgBoost'


ft_sel_name = 'Hand-picking'
model_name = 'Knn'


ft_sel_name = 'Hand-picking'
model_name = 'Random Forest' 




