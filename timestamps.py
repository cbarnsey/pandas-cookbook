import pandas as pd

popcon = pd.read_csv('~/pandas-cookbook/data/popularity-contest', sep=' ', )[:-1]
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']

#print(popcon[:5])

#convert the dates to ints
popcon['atime'] = popcon['atime'].astype(int)
popcon['ctime'] = popcon['ctime'].astype(int)

popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')

#print(popcon['atime'].dtype)

#print(popcon[:5])

popcon = popcon[popcon['atime'] > '1970-01-01']

#getting rid of rows that contain references to libraries
nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]

