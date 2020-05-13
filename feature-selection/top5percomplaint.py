import pandas as pd
import numpy as np

def make_subset():
    airbnb_complaints = pd.read_csv('../dataset/Airbnb_Service_complaints.csv')
    
    relevant_features = ['FLOORING/STAIRS', 'APPLIANCE','WATER LEAK','ELECTRIC','GENERAL','Root/Sewer/Sidewalk Condition','Street Light Condition','Beach/Pool/Sauna Complaint',
    'Senior Center Complaint','Water System','Borough Office','UNSANITARY CONDITION','Abandoned Vehicle', 'Mold','Highway Condition','Panhandling','Electrical',
    'Special Projects Inspection Team (SPIT)','Missed Collection','UNSANITARY CONDITION','Noise - House of Worship','Illegal Parking' , 'Air Quality','Quality of Life',
    'Urinating in Public', 'id', 'name', 'host_id', 'host_name', 'neighbourhood_group','neighbourhood', 'latitude', 'longitude', 'room_type', 'price',
    'minimum_nights', 'number_of_reviews', 'last_review','reviews_per_month', 'calculated_host_listings_count','availability_365'] 

   
    relevant_set = set(relevant_features)
    for x in airbnb_complaints.columns:
        if(x not in relevant_set):
            airbnb_complaints.drop([x],axis=1,inplace=True)
    #airbnb_complaints.to_csv('results/wrapper_topfromeach_top5.csv')
    airbnb_complaints.to_csv('results/wrapper_topfromeach_top5.csv')


make_subset()