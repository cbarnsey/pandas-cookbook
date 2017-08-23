import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15,3)
plt.rcParams['font.family'] = 'sans-serif'

weather_2012 = pd.read_csv('~/pandas-cookbook/data/weather_2012.csv', parse_dates=True, index_col ='Date/Time')


weather_description = weather_2012['Weather']
is_snowing = weather_description.str.contains('Snow')
##does this work the same way?
is_snowing = weather_2012['Weather'].str.contains('Snow')
##print(is_snowing[:5])
## it does!

##using resampling to get the median temp by month and then plot
weather_2012['Temp (C)'].resample('M').apply(np.median).plot(kind='bar')

# now using resampling to find the percentage of time it was snowing each month
# by changing true/false to 1/0, then medianizing each month
is_snowing.astype(float).resample('M').apply(np.mean)

#do the same statistical analysis for temp, then combine temp and snowiness together
temperature = weather_2012['Temp (C)'].resample('M').apply(np.median)
snowiness = is_snowing.astype(float).apply(np.mean)

temperature.name = 'Temperature'
snowiness.name = 'Snowiness'

stats = pd.concat([temperature,snowiness], axis=1)
#print(stats[:5])

#plot on two different plots:
stats.plot(kind='bar', subplots=True, figsize = (15,10))
