import pandas as pd 
from clean import three11


def get_311_counts_per_complaint():
    zipcode = three11.groupby(['Incident_Zip','Complaint_Type'])
    count = zipcode[['Incident_Zip','Complaint_Type']].size().reset_index(name="count")
    count = count.replace(' ', '_', regex=True)
    count.to_csv('../../dataset/count_by_incident_zip_complaint_type_2010_to_2019.csv', index=False)


get_311_counts_per_complaint()

