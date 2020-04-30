#%pip install uszipcode
from uszipcode import SearchEngine, SimpleZipcode, Zipcode

def get_zip(airbnb):
    search = SearchEngine()
    zips = []
    for row in airbnb.iterrows():
        zipcode = search.by_coordinates(row["latitude"], row["longitude"], radius=2, returns=1)
        if (len(zipcode)>0):
          zips.append(zipcode[0].zipcode)
        else:
          zips.append("-1")
    return zips