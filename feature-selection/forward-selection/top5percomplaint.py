import pandas as pd
import numpy as np

def forward_selection_top5_percomplaint():
    chosen_complaints = []
    airbnb_complaints = pd.read_csv('../../dataset/Airbnb_Service_complaints.csv')
    linear_reg = pd.read_csv("../../data-modeling/Results_per_complaint/linear_reg_error.csv")
    top = linear_reg.sort_values('Error').head(5)
    for i in top.Complaint_type:
        chosen_complaints.append(i)

    xgboost = pd.read_csv("../../data-modeling/Results_per_complaint/xgboost_regressor_error.csv")
    top = xgboost.sort_values('Error').head(5)
    for i in top.Complaint_type:
        chosen_complaints.append(i)

    ensemble_boost = pd.read_csv("../../data-modeling/Results_per_complaint/ensembleboosting_regressor_error.csv")
    top = ensemble_boost.sort_values('Error').head(5)
    for i in top.Complaint_type:
        chosen_complaints.append(i)

    random_forest = pd.read_csv("../../data-modeling/Results_per_complaint/Random_forest_error.csv")
    top = random_forest.sort_values('Error').head(5)
    for i in top.Complaint_type:
        chosen_complaints.append(i)

    knn = pd.read_csv("../../data-modeling/Results_per_complaint/knn_error.csv")
    top = knn.sort_values('Error').head(5)
    for i in top.Complaint_type:
        chosen_complaints.append(i)


    # relevant_features = ['FLOORING/STAIRS', 'APPLIANCE','WATER LEAK','ELECTRIC','GENERAL','Root/Sewer/Sidewalk Condition','Street Light Condition','Beach/Pool/Sauna Complaint',
    # 'Senior Center Complaint','Water System','Borough Office','UNSANITARY CONDITION','Abandoned Vehicle', 'Mold','Highway Condition','Panhandling','Electrical',
    # 'Special Projects Inspection Team (SPIT)','Missed Collection','UNSANITARY CONDITION','Noise - House of Worship','Illegal Parking' , 'Air Quality','Quality of Life',
    # 'Urinating in Public', 'id', 'name', 'host_id', 'host_name', 'neighbourhood_group','neighbourhood', 'latitude', 'longitude', 'room_type', 'price',
    # 'minimum_nights', 'number_of_reviews', 'last_review','reviews_per_month', 'calculated_host_listings_count','availability_365'] 
    airbnb_features = ['id', 'name', 'host_id', 'host_name', 'neighbourhood_group','neighbourhood', 'latitude', 'longitude', 'room_type', 'price',
    'minimum_nights', 'number_of_reviews', 'last_review','reviews_per_month', 'calculated_host_listings_count','availability_365'] 
    chosen_complaints.extend(airbnb_features)
    print (chosen_complaints)
    relevant_set = set(chosen_complaints)
    for x in airbnb_complaints.columns:
        if(x not in relevant_set):
            airbnb_complaints.drop([x],axis=1,inplace=True)
    #airbnb_complaints.to_csv('results/wrapper_topfromeach_top5.csv')
    airbnb_complaints.to_csv('../results/forward_selection_top5.csv')

forward_selection_top5_percomplaint()