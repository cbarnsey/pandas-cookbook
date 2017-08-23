import pandas as pd
import sqlite3
import MySQLdb #MySQL
import psycopg2 #PostgreSQL

con = sqlite3.connect("~/pandas-cookbook/data/weather_2012.sqlite")
df = pd.read_sql("SELECT * FROM weather_2012 LIMIT 3", con)

df = pd.read_sql("SELECT * FROM weather_2012 LIMIT 3", con, index_col='id')

## writing to a db

weather_df = pd.read_csv('~/pandas-cookbook/data/weather_2012.csv')
con = sqlite3.connect('~/pandas-cookbook/data/test_db.sqlite')
con.execute('DROP TABLE IF EXISTS weather_2012')
weather_df.to_sql('weather_2012', con)

##reading from created db
con = sqlite3.connect('~/pandas-cookbook/data/test_db.sqlite')
df = pd.read_sql("SELECT * FROM weather_2012 ORDER BY Weather LIMIT 3", con)

## postgres and MySQL connections, would replace with correct host and db names
con = MySQLdb.connect(host="localhost", db="test")
con = psycopg2.connect(host="localhost")
