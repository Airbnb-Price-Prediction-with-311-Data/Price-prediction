import pandas as pd
import numpy as np
from uszipcode import SearchEngine, SimpleZipcode, Zipcode
from get_zip_codes import get_zip

def remove_na(airbnb):
    airbnb['name'].fillna("$",inplace=True)
    airbnb['host_name'].fillna("#",inplace=True)
    airbnb['reviews_per_month'].fillna(0,inplace = True)
    #filling last_review NaN with oldest val and converting format 
    airbnb['last_review'] = pd.to_datetime(airbnb['last_review'],infer_datetime_format=True)
    earliest = min(airbnb['last_review'])
    airbnb['last_review'] = airbnb['last_review'].fillna(earliest)
    airbnb['last_review'] = airbnb['last_review'].apply(lambda x: x.toordinal() - earliest.toordinal())

def format_values(airbnb):
    airbnb = airbnb[np.log1p(airbnb['price']) < 8]
    airbnb = airbnb[np.log1p(airbnb['price']) > 3]
    airbnb['price'] = np.log1p(airbnb['price'])
    airbnb['minimum_nights'] = np.log1p(airbnb['minimum_nights'])

def drop_redundant_columns_rows(airbnb):
    airbnb = airbnb.drop(['host_id', 'id'], axis=1)
    airbnb['reviews_per_month'] = airbnb[airbnb['reviews_per_month'] < 19]['reviews_per_month']

def add_columns(airbnb):
    airbnb['all_year_avail'] = airbnb['availability_365']>353
    airbnb['low_avail'] = airbnb['availability_365']< 12
    airbnb['no_reviews'] = airbnb['reviews_per_month']==0



airbnb = pd.read_csv("../Data/AB_NYC_2019.csv")
remove_na(airbnb)
drop_redundant_columns_rows(airbnb)
airbnb["zipcode"] = get_zip(airbnb)
format_values(airbnb)
add_columns(airbnb)
airbnb.to_csv('../Data/Airbnb_processed.csv', index = False)
