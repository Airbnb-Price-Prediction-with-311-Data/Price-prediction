import numpy as np
import pandas as pd 

def get_subset():
    count_by_complaint_type_and_zip = pd.read_csv('dataset/count_by_incident_zip_complaint_type_2010.csv')
    count_by_complaint_type_and_zip.replace('-', '', regex=True)
    count_by_complaint_type = count_by_complaint_type_and_zip.groupby('Complaint_Type').Complaint_Type.count().reset_index(name="count")
    selected = count_by_complaint_type[count_by_complaint_type['count'] < 100]
    count_by_complaint_type_and_zip = count_by_complaint_type_and_zip[~count_by_complaint_type_and_zip['Complaint_Type'].isin(selected.Complaint_Type)]
    return count_by_complaint_type_and_zip

def get_one_hot():
    total = count_by_complaint_type_and_zip.groupby('Incident_Zip')['count'].sum()
    one_hot = pd.pivot_table(count_by_complaint_type_and_zip,index='Incident_Zip',columns=['Complaint_Type'],values='count',aggfunc=np.sum,fill_value=0)
    one_hot['total_count']=total
    one_hot = one_hot.reset_index()
    return one_hot


def write_to_file(one_hot):
    one_hot = one_hot.astype({"Incident_Zip": int})
    one_hot = one_hot.astype({'Incident_Zip': str})
    for index, row in one_hot.iterrows():
        one_hot.at[index, 'Incident_Zip'] = str(row['Incident_Zip']).zfill(5) 
    one_hot.to_csv('dataset/complaint_type.csv', index=True)


count_by_complaint_type_and_zip = get_subset()
one_hot = get_one_hot()
write_to_file(one_hot)
