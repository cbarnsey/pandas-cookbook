import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.mpl_style', 'default')
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15,5)

complaints = pd.read_csv('~/pandas-cookbook/data/311-service-requests.csv')

#print complaints

#print complaints['Complaint Type']

#print complaints[:5]

#print the first five rows of, restricting to the Complaint Type column
print complaints['Complaint Type'][:5]
print complaints[['Complaint Type', 'Borough']]
#need both square brackets, as the following will give a KeyError; ie, trying to refer
# to a key that's a tuple (Complaint Type, Borough)
#print	complaints['Complaint Type', 'Borough']

print complaints['Complaint Type'].value_counts()

#putting the complaint types into a new DF derived from the first
complaint_counts = complaints['Complaint Type'].value_counts()

complaint_counts[:10].plot(kind='bar')
