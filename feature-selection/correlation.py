import pandas as pd
import numpy as np

def make_subset():
    airbnb_complaints = pd.read_csv('../dataset/Airbnb_Service_complaints.csv')
    cor = airbnb_complaints.corr()
    cor_target = abs(cor["price"])
    relevant_features = cor_target[cor_target>0.283]
    relevant_set = set(relevant_features.index)
    for x in airbnb_complaints.columns:
        if(x not in relevant_set):
            airbnb_complaints.drop([x],axis=1,inplace=True)
    airbnb_complaints.to_csv('../dataset/reduced_data.csv')



make_subset()