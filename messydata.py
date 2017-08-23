import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15,5)
plt.rcParams['font.family'] = 'sans-serif'

pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

requests = pd.read_csv('~/pandas-cookbook/data/311-service-requests.csv')

#print(requests['Incident Zip'].unique())

## changing junk to NA, interpreting all data as a string
na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('~/pandas-cookbook/data/311-service-requests.csv', na_values=na_values, dtype={'Incident Zip': str})
#print(requests['Incident Zip'].unique())

#find how many rows have weird dashes in them
rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
#print(len(requests[rows_with_dashes]))

##long zip codes are valid, but we're still going to truncate them
long_zip_codes = requests['Incident Zip'].str.len() > 5
#print(requests['Incident Zip'][long_zip_codes].unique())
requests['Incident Zip'] = requests['Incident Zip'].str.slice(0,5)

##finding 00000 and setting to nan
zero_zips = requests['Incident Zip'] == '00000'
requests.loc[zero_zips, 'Incident Zip'] = np.nan

## how about we wrap all of this up into a function
def fix_zip_codes(zips):
	zips = zips.str.slice(0,5)

	zero_zips = zips == '00000'
	zips[zero_zips] = np.nan

	return zips

requests['Incident Zip'] = fix_zip_codes(requests['Incident Zip'])
#print(requests['Incident Zip'].unique())
