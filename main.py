import linkfetch
import it_getdata as get 
import pandas as pd
 
print('running...')

itunesl = ['https://itunes.apple.com/us/genre/podcasts/id26?mt=2',
      'https://itunes.apple.com/us/genre/podcasts-',
      'https://itunes.apple.com/us/podcast/',
      'https://itunes.apple.com/us/podcast/marketplace-with-kai-ryssdal/id201853034?mt=2']


#itunes_links = linkfetch.find_links(itunesl[0],itunesl[1], itunesl[2])
#print(len(itunes_links))


columns =   ['Name']
podcast_df = pd.DataFrame([[0]], columns = columns)


podcast_df = get.get_data(itunesl[3],podcast_df)

print(podcast_df)
