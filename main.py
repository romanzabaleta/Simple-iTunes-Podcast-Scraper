import linkfetch
import it_getdata as get 
import pandas as pd
import genre_id_reader as gen 
import podatabase

print('running...')

itunesl = ['https://itunes.apple.com/us/genre/podcasts/id26?mt=2',
      'https://itunes.apple.com/us/genre/podcasts-',
      'https://itunes.apple.com/us/podcast/']

itunes_links = linkfetch.find_links(itunesl[0],itunesl[1], itunesl[2])
print(len(itunes_links))
num =len(itunes_links)-1
print(itunes_links[num])

columns = ['Name', 'Rating Volume', 'Rating', 'Genre', 'Description']
podcast_df = pd.DataFrame(columns=columns)

for i in range(1000,1050):
	ok = get.get_data(itunes_links[i], podcast_df, columns)
	podcast_df = podcast_df.append(ok)
	print(i)
	print(itunes_links[i])

podatabase.podb(podcast_df)