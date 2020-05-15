import pandas as pd
import numpy as np

def make_subset():
    airbnb_complaints = pd.read_csv('dataset/Airbnb_Service_complaints_merged.csv')
    cor = airbnb_complaints.corr()
    cor_target = abs(cor["price"])
    relevant_features = cor_target[cor_target>0.283]
    relevant_set = set(relevant_features.index)
    relevant_set.add('price')
    for x in airbnb_complaints.columns:
        if(x not in relevant_set):
            airbnb_complaints.drop([x],axis=1,inplace=True)
    #airbnb_complaints.to_csv('results/wrapper_topfromeach_top5.csv')
    airbnb_complaints.to_csv('feature_selection/results/feature_selection_correlation.csv')
    
#make_subset()