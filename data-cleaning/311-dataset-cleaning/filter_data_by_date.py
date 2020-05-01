import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import seaborn as sns

def remove_2020():
    three11 = pd.read_csv('../Data/311_Service_Requests_from_2010_to_Present.csv')
    indexNames = three11[ three11['Created_Date'].str.contains('/2020') ].index
    three11.drop(indexNames , inplace=True)
    three11.to_csv('../Data/311_Service_Requests_from_2010_to_Present.csv', index=True)

remove_2020()
