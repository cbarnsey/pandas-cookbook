import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15,3)
plt.rcParams['font.family'] = 'sans-serif'

weather_2012_final = pd.read_csv('~/pandas-cookbook/data/weather_2012.csv', index_col = 'Date/Time')

##setting up a URL template, then feeding that to the read_csv
# see the month and year hooks in there? that's where the formatting will go
url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"

url = url_template.format(month = 3, year = 2012)

#create the DF, skipping the first 15 rows of metadata, accounting for a header
weather_mar2012 = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, encoding='latin1', header=True)

##plotting.. the xc/xb stuff prints the degree character
#weather_mar2012[u"Temp (\xc2\xb0C)"].plot(figsize=(15,5))

weather_mar2012.columns = [
	u'Year',u'Month',u'Day',u'Time',u'Data Quality',u'Temp (C)',u'Temp Flag',u'Dew Point Temp (C)',
	u'Dew Point Temp Flag',u'Rel Hum (%)',u'Rel Hum Flag',u'Wind Dir (10s deg)',u'Wind Dir Flag',
	u'Wind Spd (km/h)',u'Wind Spd Flag',u'Visibility (km)',u'Visibility Flag',
	u'Stn Press (kPa)',u'Stn Press Flag',u'Hmdx',u'Hmdx Flag',u'Wind Chill',u'Wind Chill Flag',
	u'Weather']

## dropping columns with an NULL values
# axis 1 change it to drop columns instead of rows, any means ANY null value in the column
weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')

## dropping the redundant date columns (they're already in the Date/Time index)
# axis=1 here again switches to dropping columns instead of rows
weather_mar2012 = weather_mar2012.drop(['Year','Month','Date','Time','Data Quality'], axis=1)

## making a copy of the DF, including only the Temp column, then adding a column for the Hour
# this is prepping for plotting the temperature by the hour of day
temperatures = weather_mar2012[[u'Temp (C)']].copy()
print(temperaturs.head)
temperatures.loc[:,'Hour'] = weather_mar2012.index.hour
##group the temperatures by the hour, get the median per hour using agg, then plot it
temperatures.groupby('Hour').aggregate(np.median).plot()

## now write a function that does the above, so we can run it over and over for an entire year

def download_weather_month(year,month):
	if month == 1:
		year += 1
	url = url_template.format(year=year,month=month)
	weather_data = pd.read_csv(url,skiprows=15,index_col='Date/Time',parse_dates=True,header=True)
	weather_data = weather_data.dropna(axis=1)
	weather_data.columns = [col.replace('\xb0','') for col in weather_data.columns]
	weather_data = weather_data.drop(['Year','Day','Month','Time','Data Quality'], axis=1)
	return weather_data

##now get all the data by month
data_by_month = [ download_weather_month(2012,i) for i in range(1,13)]

##mash all the DFs together
weather_2012 = pd.concat(data_by_month)

## optionally, save the giant 2012 weather DF to a .csv so as to not have to download every time
weather_2012.to_csv('~/pandas-cookbook/data/weather_2012_test.csv')

