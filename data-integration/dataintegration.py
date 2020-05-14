import numpy as np
import pandas as pd


def merge_datasets():
      airbnb_complaints = pd.read_csv('../dataset/Airbnb_processed_try_1.csv')
      df_complaint_types = pd.read_csv("../dataset/complaint_type.csv")
      for index, row in df_complaint_types.iterrows():
            df_complaint_types.at[index, 'Incident_Zip'] = str(row['Incident_Zip']).zfill(5)
      df_complaint_types.drop(['Unnamed: 0'], axis=1, inplace=True)
      df_complaint_types.rename(columns = {'Incident_Zip':'zipcode'}, inplace = True) 

      df_merge_complaint_types = pd.merge(airbnb_complaints, df_complaint_types, on='zipcode', how='inner')
      df_merge_complaint_types.to_csv(r'../dataset/Airbnb_Service_complaints_merged.csv', index = False)

merge_datasets()