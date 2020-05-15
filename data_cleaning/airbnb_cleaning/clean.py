import pandas as pd
import numpy as np
import uszipcode
from uszipcode import SearchEngine, SimpleZipcode, Zipcode
from data_cleaning.airbnb_cleaning.get_zip_codes import get_zip

def airbnb_clean():
    airbnb = pd.read_csv("dataset/AB_NYC_2019.csv")
    airbnb['name'].fillna("$", inplace=True)
    airbnb['host_name'].fillna("#", inplace=True)
    #airbnb['reviews_per_month'].fillna(0, inplace=True)
    airbnb['last_review'] = pd.to_datetime(airbnb['last_review'],infer_datetime_format=True)
    earliest = min(airbnb['last_review'])
    airbnb['last_review'] = airbnb['last_review'].fillna(earliest)
    airbnb['last_review'] = airbnb['last_review'].apply(lambda x: x.toordinal() - earliest.toordinal())
    airbnb.drop(['host_id', 'id'], axis=1, inplace=True)
    airbnb['reviews_per_month'] = airbnb[airbnb['reviews_per_month'] < 19]['reviews_per_month']
    airbnb['reviews_per_month'].fillna(0, inplace=True)
    airbnb["zipcode"] = get_zip(airbnb)
    airbnb = airbnb[np.log1p(airbnb['price']) < 8]
    airbnb = airbnb[np.log1p(airbnb['price']) > 3]
    airbnb['price'] = np.log1p(airbnb['price'])
    airbnb['minimum_nights'] = np.log1p(airbnb['minimum_nights'])
    airbnb['all_year_avail'] = airbnb['availability_365']>353
    airbnb['low_avail'] = airbnb['availability_365']< 12
    airbnb['no_reviews'] = airbnb['reviews_per_month']==0
    airbnb.to_csv('dataset/Airbnb_processed.csv', index = False)

#airbnb_clean()
