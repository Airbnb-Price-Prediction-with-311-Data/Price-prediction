import pandas as pd
import numpy as np

##This file was run 3 times to get top 5, 10 and 15 values per complaint type 
def forward_selection_top5_percomplaint():
    chosen_complaints = []
    airbnb_complaints = pd.read_csv('../../dataset/Airbnb_Service_complaints_merged.csv')
    linear_reg = pd.read_csv("../results/linear_reg_error.csv")
    top = linear_reg.sort_values('Error').head(15)
    for i in top.Complaint_type:
        chosen_complaints.append(i)

    xgboost = pd.read_csv("../results/xgboost_regressor_error.csv")
    top = xgboost.sort_values('Error').head(15)
    for i in top.Complaint_type:
        chosen_complaints.append(i)

    ensemble_boost = pd.read_csv("../results/ensembleboosting_regressor_error.csv")
    top = ensemble_boost.sort_values('Error').head(15)
    for i in top.Complaint_type:
        chosen_complaints.append(i)

    random_forest = pd.read_csv("../results/Random_forest_error.csv")
    top = random_forest.sort_values('Error').head(15)
    for i in top.Complaint_type:
        chosen_complaints.append(i)

    airbnb_features = ['id', 'name', 'host_id', 'host_name', 'neighbourhood_group','neighbourhood', 'latitude', 'longitude', 'room_type', 'price',
    'minimum_nights', 'number_of_reviews', 'last_review','reviews_per_month', 'calculated_host_listings_count','availability_365'] 
    chosen_complaints.extend(airbnb_features)
    print (chosen_complaints)
    relevant_set = set(chosen_complaints)
    for x in airbnb_complaints.columns:
        if(x not in relevant_set):
            airbnb_complaints.drop([x],axis=1,inplace=True)
    #airbnb_complaints.to_csv('results/wrapper_topfromeach_top5.csv')
    airbnb_complaints.to_csv('../results/forward_selection_top15_v1.csv')

forward_selection_top5_percomplaint()