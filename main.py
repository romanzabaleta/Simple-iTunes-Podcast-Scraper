import linkfetch
import it_getdata as get 
import pandas as pd
import genre_id_reader as gen 
import podatabase
import csv

print('running...')

#itunesl = ['https://itunes.apple.com/us/genre/podcasts/id26?mt=2',
#      'https://itunes.apple.com/us/genre/podcasts-',
#      'https://itunes.apple.com/us/podcast/']

#itunes_links = linkfetch.find_links(itunesl[0],itunesl[1], itunesl[2])
with open('csvfile.csv', 'r') as output:
    reader = csv.reader(output, delimiter='\n')
    itunes_links = list(reader)

print(len(itunes_links))
#dfcsv = pd.read_csv('csvfile.csv', delimiter='\n')
#itunes_links = dfcsv.to_dict().values()
#print(len(itunes_links))

columns = ['Name', 'Rating_Volume', 'Rating', 'Genre', 'Description']
podcast_df = pd.DataFrame(columns=columns)

for i in range(13800,13803):
	try:
		ok = get.get_data(itunes_links[i][0], podcast_df, columns)
		podcast_df = podcast_df.append(ok)
		print(i)
		print(itunes_links[i][0])
	except:
		pass

podatabase.updatepodb(podcast_df)
#podatabase.newpodb(podcast_df)

#with open('csvfile.txt', "w") as output:
#    writer = csv.writer(output, lineterminator='\n')
#    for val in itunes_links:
#        writer.writerow([val])