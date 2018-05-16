import sqlite3
from pandas.io import sql

def podb(poddf):
	podb = sqlite3.connect('itunes_podcast.db')
	c = podb.cursor()
	sql.to_sql(poddf, name='poddf', con=podb)
	p2 = sql.read_sql('select * from poddf', podb)
	podb.commit()
	podb.close()
	print(p2)