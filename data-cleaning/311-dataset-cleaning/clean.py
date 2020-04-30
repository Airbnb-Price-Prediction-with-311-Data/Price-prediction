import pandas as pd 

def clean_311():
    three11 = pd.read_csv('../Data/311_Service_Requests_from_2010_to_Present.csv')
    three11.columns = [c.replace(' ', '_') for c in three11.columns]
    three11.dropna(subset=['Location'], inplace=True)
    three11.dropna(subset=['Incident_Zip'], inplace=True)
    return three11

three11 = clean_311()










