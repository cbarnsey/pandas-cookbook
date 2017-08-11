import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (20,5)

#not necessary in pandas 0.13
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

bikes = pd.read_csv('./data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
#bikes['Berri 1'].plot()

berri_bikes = bikes[['Berri 1']].copy()
#print berri_bikes[:5]

#print berri_bikes.index.day

#print berri_bikes.index.weekday

berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday
#print berri_bikes[:10]

weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
#print weekday_counts

weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#print weekday_counts

weekday_counts.plot(kind='bar')

##this gets everyything together in smaller form:
bikes = pd.read_csv('./data/bikes.csv', sep=';', encoding = 'latin1', parse_dates = ['Date'], dayfirst = True, index_col = 'Date')
berri_bikes = bikes[['Berri 1']].copy()

berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday

##add up number of cyclists, then plot
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts.plot(kind='bar')
