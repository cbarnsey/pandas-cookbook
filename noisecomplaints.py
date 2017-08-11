import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (20,5)

#not necessary in pandas 0.13
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

complaints = pd.read_csv('./data/311-service-requests.csv')

# print complaints[:10]

#print complaints['Complaint Type']

noise_complaints = complaints[complaints['Complaint Type'] == "Noise - Street/Sidewalk"]
#print noise_complaints[:3]

## create boolean array for filtering, then apply this in the [] to filter the entire DataFrame
complaints['Complaint Type'] == "Noise - Street/Sidewalk"

is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
in_brooklyn = complaints['Borough'] == "BROOKLYN"
#print complaints[is_noise & in_brooklyn][:10]

#print specific columns
# print complaints[is_noise & in_brooklyn][['Complaint Type'],['Borough'],['Created Date'],['Descriptor']][:20]

## which borough has the highest noise copmlaints?
# get boolean array to use for filtering the df
is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
#create a filtered DF from the original DF, using the filtering boolean array
noise_complaints = complaints[is_noise]
#print the grouped values from the filtered DF, using the Borough column as the grouping object
#print noise_complaints['Borough'].value_counts()

## divide the borough counts by the total number of counts to get percentages
noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()
#these don't work for some reason... different "shaped" arrays?
percentages = noise_complaint_counts[:] / noise_complaints[:]
#print percentages['Borough'].values()

#same error as precentages prevents this from working
(noise_complaint_counts[:] / noise_complaints[:]).plot(kind='bar')
