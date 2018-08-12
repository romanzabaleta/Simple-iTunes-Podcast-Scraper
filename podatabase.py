import sqlite3
from pandas.io import sql

def newpodb(poddf):
	conn = sqlite3.connect('itunes_podcast.db')
	c = conn.cursor()
	sql.to_sql(poddf, name='poddf', con=conn)
	p2 = sql.read_sql('select * from poddf', conn)
	conn.commit()
	conn.close()
	print(p2)

def updatepodb(poddf):
	conn = sqlite3.connect('itunes_podcast.db')
	c = conn.cursor()
	poddf.to_sql('poddf', conn, if_exists='append')
	p2 = sql.read_sql('select * from poddf', conn)
	conn.commit()
	conn.close()
	print(p2)

