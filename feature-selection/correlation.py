import pandas as pd
import numpy as np

def make_subset():
    airbnb_complaints = pd.read_csv('../dataset/Airbnb_Service_complaints.csv')
    cor = airbnb_complaints.corr()
    cor_target = abs(cor["price"])
    #relevant_features = cor_target[cor_target>0.283]
    relevant_features =['Investigations and Discipline (IAD)',
    'Broken Parking Meter',
    'UNSANITARY CONDITION',
    'Lost Property',
    'Smoking',
    'Bike/Roller/Skate Chronic',
    'Unsanitary Animal Pvt Property',
    'Found Property',
    'Standing Water',
    'Noise - Street/Sidewalk',
    'Water Conservation',
    'Safety',
    'Traffic',
    'Building/Use',
    'Construction Lead Dust',
    'Derelict Bicycle',
    'Abandoned Vehicle',
    'WATER LEAK',
    'Noise', 'id', 'name', 'host_id', 'host_name', 'neighbourhood_group',
       'neighbourhood', 'latitude', 'longitude', 'room_type', 'price',
       'minimum_nights', 'number_of_reviews', 'last_review',
       'reviews_per_month', 'calculated_host_listings_count',
       'availability_365']
    relevant_set = set(relevant_features)
    #print (airbnb_complaints.columns)
    for x in airbnb_complaints.columns:
        if(x not in relevant_set):
            airbnb_complaints.drop([x],axis=1,inplace=True)
    airbnb_complaints.to_csv('../dataset/reduced_data_final.csv')
    print (airbnb_complaints.columns)


make_subset()