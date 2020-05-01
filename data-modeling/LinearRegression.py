import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score
import csv


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
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_test)
    #model=xgb.XGBClassifier(random_state=1,learning_rate=0.01)
    #model.fit(X_train, y_train)
    #y_pred = model.predict(X_test)
    #print (model.score(X_test, y_test))
    print ("LINEAR REGRESSION ON ENTIRE DATASET")
    print ("ERROR")
    #f.write("ERROR")
    print (mean_squared_error(y_test, y_pred))
    #f.write(mean_squared_error(y_test, y_pred))
    print ("ACCURACY")
    #f.write("ACCURACY")
    print (1- mean_squared_error(y_test, y_pred))
    #f.write(1- mean_squared_error(y_test, y_pred))
    #print (r2_score(y_test, y_pred))
    #f.close()

def airbnb_perservice():
    with open('linear_reg_error.csv', mode='w') as error_file:
	employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    model = linear_model.LinearRegression()
    complaints = {}
    airbnb_subset = airbnb_service_complaints.copy()
    for col in columns:
        airbnb_subset.drop([col], axis=1, inplace=True)
    airbnb_subset.drop(['latitude', 'longitude', 'count', 'total_count'], axis=1, inplace=True)
    #print (airbnb_subset.columns)
    y = airbnb_service_complaints.price
    for col in columns:
        complaint = airbnb_service_complaints[col]
        airbnb_subset[col] = complaint
        numerical_features = airbnb_subset.select_dtypes(exclude=['object'])
        X_train, X_test, y_train, y_test = train_test_split(numerical_features, y, test_size=0.2)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        airbnb_subset.drop([col], axis=1, inplace=True)
        complaints[col] = mean_squared_error(y_test, y_pred)
	employee_writer.writerow([col,mean_squared_error(y_test, y_pred), 1-mean_squared_error(y_test, y_pred)])
    print (complaints)   

airbnb_allservices()
airbnb_perservice()
