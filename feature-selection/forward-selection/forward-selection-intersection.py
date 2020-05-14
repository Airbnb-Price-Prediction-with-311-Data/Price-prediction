import pandas as pd
import numpy as np

airbnb_complaints = pd.read_csv('../../dataset/Airbnb_Service_complaints_merged.csv')

def feature_selection_intersection():
#the values that are being compared with are baseline airbnb model values 
    #linear_reg = pd.read_csv("../../data-modeling/Results_per_complaint/linear_reg_error.csv")
    linear_reg = pd.read_csv("../results/linear_reg_error.csv")
    #linear_reg['above_threshold'] = linear_reg['Error'] >= 0.3823304837939663
    linear_reg['above_threshold'] = linear_reg['Error'] >= 0.3847448708692744
    linear_reg_services = []
    linear_reg_services = linear_reg.loc[linear_reg['above_threshold'] == False, 'Complaint_type']

    #xgboost = pd.read_csv("../../data-modeling/Results_per_complaint/xgboost_regressor_error.csv")
    xgboost = pd.read_csv("../results/xgboost_regressor_error.csv")
    #xgboost['above_threshold'] = xgboost['Error'] >= 0.3178847569568179 
    xgboost['above_threshold'] = xgboost['Error'] >= 0.27560312353588323
    xgboost_complaints = []
    xgboost_complaints = xgboost.loc[xgboost['above_threshold'] == False, 'Complaint_type']

    #ensemble_boost = pd.read_csv("../../data-modeling/Results_per_complaint/ensembleboosting_regressor_error.csv")
    ensemble_boost = pd.read_csv("../results/ensembleboosting_regressor_error.csv")
    #ensemble_boost['above_threshold'] = ensemble_boost['Error'] >= 0.2944261933977081
    ensemble_boost['above_threshold'] = ensemble_boost['Error'] >= 0.2928387356544043
    ensemble_boost_complaints = []
    ensemble_boost_complaints = ensemble_boost.loc[ensemble_boost['above_threshold'] == False, 'Complaint_type']

    #random_forest = pd.read_csv("../../data-modeling/Results_per_complaint/Random_forest_error.csv")
    random_forest = pd.read_csv("../results/Random_forest_error.csv")
    #random_forest['above_threshold'] = random_forest['Error'] >= 0.3542529602630437
    random_forest['above_threshold'] = random_forest['Error'] >= 0.358125324747934
    random_forest_complaints = []
    random_forest_complaints = random_forest.loc[random_forest['above_threshold'] == False, 'Complaint_type']

    # knn = pd.read_csv("../../data-modeling/Results_per_complaint/knn_error.csv")
    # knn['above_threshold'] = knn['Error'] >= 0.35103839840291173 
    # knn_complaints = []
    # knn_complaints = knn.loc[knn['above_threshold'] == False, 'Complaint_type']

    final_complaints = list(set(linear_reg_services) & set(xgboost_complaints) & set(random_forest_complaints) & set(ensemble_boost_complaints))
    airbnb_features = ['id', 'name', 'host_id', 'host_name', 'neighbourhood_group',
       'neighbourhood', 'latitude', 'longitude', 'room_type', 'price',
       'minimum_nights', 'number_of_reviews', 'last_review',
       'reviews_per_month', 'calculated_host_listings_count',
       'availability_365']
    final_complaints.extend(airbnb_features)
    print (final_complaints)
    relevant_features = set(final_complaints)
    for x in airbnb_complaints.columns:
        if(x not in relevant_features):
            airbnb_complaints.drop([x],axis=1,inplace=True)
    ##airbnb_complaints.to_csv('../dataset/wrapper_topfromeach_top5.csv')
    airbnb_complaints.to_csv('../results/forward_selection_intersection_v1.csv')


feature_selection_intersection()
