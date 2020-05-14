import pandas as pd
import numpy as np

def make_subset():
    airbnb_complaints = pd.read_csv('../dataset/Airbnb_Service_complaints_merged.csv')
    cor = airbnb_complaints.corr()
    cor_target = abs(cor["price"])
    relevant_features = cor_target[cor_target>0.283]
    #print type(relevant_features)
    #relevant_features.index.append(airbnb_complaints['price'])
    #for i in relevant_features:
    #    print (i[0])
    #print (relevant_features.index)
    
#     relevant_features = ['APPLIANCE', 'Air Quality', 'Beach/Pool/Sauna Complaint',  'Blocked Driveway', 'Collection Truck Noise',
#     'Construction', 'Construction Lead Dust', 'Consumer Complaint', 'DOOR/WINDOW', 'Damaged Tree', 'Dead Tree', 'Dead/Dying Tree',
#     'Dirty Conditions', 'Disorderly Youth', 'Drinking', 'Drinking Water',
#     'Drug Activity','ELECTRIC','ELEVATOR','Electrical','Elevator','Emergency Response Team (ERT)','FLOORING/STAIRS','Food Establishment', 'Food Poisoning', 'GENERAL','General','General Construction/Plumbing','Graffiti','HEAT/HOT WATER','Harboring Bees/Wasps','Hazardous Materials','Highway Condition',
#     'Homeless Encampment','Homeless Street Condition','Illegal Fireworks','Indoor Air Quality','Indoor Sewage','Industrial Waste','Litter Basket / Request', 'Maintenance or Facility','Mobile Food Vendor','Mold','Mosquitoes','Noise','Noise - Commercial','Noise - Helicopter','Noise - House of Worship','Noise - Park','Noise - Residential','Noise - Street/Sidewalk','Noise - Vehicle',
# 'Non-Emergency Police Matter','Overflowing Litter Baskets','Overgrown Tree/Branches','PAINT/PLASTER','PLUMBING','Plumbing','Public Payphone Complaint','Public Toilet','Quality of Life','Rodent','Root/Sewer/Sidewalk Condition','SAFETY','Safety','Sanitation Condition','Scaffold Safety','Sewer','Sidewalk Condition','Smoking',
# 'Snow','Standing Water','Street Condition','Street Light Condition','Sweeping/Inadequate','Sweeping/Missed','Taxi Complaint','Taxi Report','Traffic','Traffic Signal Condition','UNSANITARY CONDITION','Unsanitary Condition','Unsanitary Pigeon Condition','Urinating in Public','WATER LEAK','Water Quality','Water System', 'id', 'name', 'host_id', 'host_name', 'neighbourhood_group',
#        'neighbourhood', 'latitude', 'longitude', 'room_type', 'price',
#        'minimum_nights', 'number_of_reviews', 'last_review',
#        'reviews_per_month', 'calculated_host_listings_count',
#        'availability_365']
#     relevant_features1 = ['FLOORING/STAIRS', 'APPLIANCE','WATER LEAK','ELECTRIC','GENERAL','Root/Sewer/Sidewalk Condition','Street Light Condition','Beach/Pool/Sauna Complaint',
# 'Senior Center Complaint','Water System','Borough Office','UNSANITARY CONDITION','Abandoned Vehicle',
# 'Mold','Highway Condition','Panhandling','Electrical','Special Projects Inspection Team (SPIT)','Missed Collection','UNSANITARY CONDITION','Noise - House of Worship','Illegal Parking' , 'Air Quality','Quality of Life',
# 'Urinating in Public', 'id', 'name', 'host_id', 'host_name', 'neighbourhood_group',
#        'neighbourhood', 'latitude', 'longitude', 'room_type', 'price',
#        'minimum_nights', 'number_of_reviews', 'last_review',
#        'reviews_per_month', 'calculated_host_listings_count',
#        'availability_365'] 

   
    relevant_set = set(relevant_features.index)
    relevant_set.add('price')
    #print (airbnb_complaints.columns)
    for x in airbnb_complaints.columns:
        if(x not in relevant_set):
            airbnb_complaints.drop([x],axis=1,inplace=True)
    #print (airbnb_complaints.columns)
    #airbnb_complaints.to_csv('results/wrapper_topfromeach_top5.csv')
    airbnb_complaints.to_csv('results/feature_selection_correlation_v1.csv')
    #print (airbnb_complaints.columns)


make_subset()