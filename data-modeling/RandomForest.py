import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import mean_squared_error
<<<<<<< HEAD
import csv
=======
>>>>>>> ef0d776de39377ad83967dcccbd63b9395764248

airbnb_service_complaints = pd.read_csv("Airbnb_Service_complaints.csv")
#f = open("Linear_Regression.txt", "x")
columns = ['APPLIANCE', 'Abandoned Vehicle', 'Adopt-A-Basket', 'Air Quality', 'Animal Abuse', 'Animal Facility - No Permit', 'Animal in a Park',
'Animal-Abuse', 'Asbestos', 'BEST/Site Safety', 'Beach/Pool/Sauna Complaint', 'Bike Rack Condition',
 'Bike/Roller/Skate Chronic', 'Blocked Driveway', 'Boilers', 'Borough Office', 'Broken Muni Meter', 'Broken Parking Meter', 'Building Marshals office',
 'Building/Use', 'Bus Stop Shelter Complaint', 'Bus Stop Shelter Placement', 'City Vehicle Placard Complaint', 'Collection Truck Noise',
 'Construction', 'Construction Lead Dust', 'Construction Safety Enforcement', 'Consumer Complaint', 'Cranes and Derricks', 'Curb Condition',
 'DOF Property - Payment Issue', 'DOOR/WINDOW', 'DPR Internal', 'DRIE', 'Damaged Tree', 'Day Care', 'Dead Tree', 'Dead/Dying Tree',
 'Derelict Bicycle', 'Derelict Vehicle', 'Derelict Vehicles', 'Dirty Conditions', 'Disorderly Youth', 'Drinking', 'Drinking Water',
 'Drug Activity','ELECTRIC','ELEVATOR','Electrical','Electronics Waste Appointment','Elevator','Emergency Response Team (ERT)','Executive Inspections',
 'FLOORING/STAIRS','Facades','Food Establishment', 'Food Poisoning', 'For Hire Vehicle Complaint', 'For Hire Vehicle Report', 'Found Property',
 'GENERAL','General','General Construction/Plumbing','Graffiti','HEAT/HOT WATER','Harboring Bees/Wasps','Hazardous Materials','Highway Condition',
 'Homeless Encampment','Homeless Person Assistance','Homeless Street Condition','Illegal Animal Kept as Pet','Illegal Animal Sold',
 'Illegal Fireworks','Illegal Parking','Illegal Tree Damage','Indoor Air Quality','Indoor Sewage','Industrial Waste','Investigations and Discipline (IAD)',
 'Lead','LinkNYC','Litter Basket / Request','Lost Property', 'Maintenance or Facility','Miscellaneous Categories', 'Missed Collection',
 'Missed Collection (All Materials)', 'Mobile Food Vendor','Mold','Mosquitoes','New Tree Request','Noise','Noise - Commercial','Noise - Helicopter',
 'Noise - House of Worship','Noise - Park','Noise - Residential','Noise - Street/Sidewalk','Noise - Vehicle',
 'Non-Emergency Police Matter','Non-Residential Heat', 'OUTSIDE BUILDING','Other Enforcement','Overflowing Litter Baskets','Overgrown Tree/Branches',
 'PAINT/PLASTER','PLUMBING','Panhandling','Pet Shop','Plumbing','Poison Ivy','Posting Advertisement','Public Payphone Complaint','Public Toilet',
 'Quality of Life',
 'Recycling Enforcement',
 'Request Large Bulky Item Collection',
 'Request Xmas Tree Collection',
 'Rodent',
 'Root/Sewer/Sidewalk Condition',
 'SAFETY',
 'Safety',
 'Sanitation Condition',
 'Scaffold Safety',
 'School Maintenance',
 'Senior Center Complaint',
 'Sewer',
 'Sidewalk Condition',
 'Smoking',
 'Snow',
 'Special Natural Area District (SNAD)',
 'Special Projects Inspection Team (SPIT)',
 'Standing Water',
 'Street Condition',
 'Street Light Condition',
 'Street Sign - Damaged',
 'Street Sign - Dangling',
 'Street Sign - Missing',
 'Sustainability Enforcement',
 'Sweeping/Inadequate',
 'Sweeping/Missed',
 'Tattooing',
 'Taxi Complaint',
 'Taxi Report',
 'Traffic',
 'Traffic Signal Condition',
 'UNSANITARY CONDITION',
 'Unleashed Dog',
 'Unsanitary Animal Facility',
 'Unsanitary Animal Pvt Property',
 'Unsanitary Condition',
 'Unsanitary Pigeon Condition',
 'Urinating in Public',
 'Vacant Lot',
 'Vending',
 'Violation of Park Rules',
 'WATER LEAK',
 'Water Conservation',
 'Water Quality',
 'Water System',
 'Window Guard']

def airbnb_allservices():
    numerical_features =  airbnb_service_complaints.select_dtypes(exclude=['object'])
    #categorical_features = airbnb_service_complaints.select_dtypes(include=['object'])
    y = numerical_features.price
    numerical_features.drop(['price'], axis=1, inplace=True)
    numerical_features.drop(['count'], axis=1, inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(numerical_features, y, test_size=0.2)
    regr = RandomForestRegressor(max_depth=2, random_state=0)
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_test)
    print ("RANDOM FOREST ON ENTIRE DATASET")
    print ("ERROR")
    print (mean_squared_error(y_test, y_pred))
    #f.write(mean_squared_error(y_test, y_pred))
    print ("ACCURACY")
    #f.write("ACCURACY")
    print (1- mean_squared_error(y_test, y_pred))

def airbnb_perservice():
    fields = ['Complaint_type','Error','Accuracy']
    rows = []
    filename = "linear_reg_error.csv"
    model = RandomForestRegressor(max_depth=2, random_state=0)
    complaints = {}
    airbnb_subset = airbnb_service_complaints.copy()
    for col in columns:
        airbnb_subset.drop([col], axis=1, inplace=True)
    y = airbnb_service_complaints.price
    airbnb_subset.drop(['latitude', 'longitude', 'count', 'total_count', 'price'], axis=1, inplace=True)
    #print (airbnb_subset.columns)
    
    for col in columns:
        row = []
        complaint = airbnb_service_complaints[col]
        airbnb_subset[col] = complaint
        numerical_features = airbnb_subset.select_dtypes(exclude=['object'])
        X_train, X_test, y_train, y_test = train_test_split(numerical_features, y, test_size=0.2)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        airbnb_subset.drop([col], axis=1, inplace=True)
        complaints[col] = mean_squared_error(y_test, y_pred)
        row.append(col)
        row.append(mean_squared_error(y_test, y_pred))
        row.append(1-mean_squared_error(y_test, y_pred))
        rows.append(row)
    complaints = {k: v for k, v in sorted(complaints.items(), key=lambda item: item[1])}
    print (complaints)   

airbnb_allservices()
airbnb_perservice()