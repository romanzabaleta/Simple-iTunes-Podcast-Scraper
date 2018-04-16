from bs4 import BeautifulSoup
import pandas as pd
from progressbar import ProgressBar
import pattern3.web as web

#columns =  ['Name', 'Genre']
#podcast_df = pd.DataFrame(columns = columns)


def get_data(webp, df_podcast, columns):
  url = web.URL(webp)
  bs = BeautifulSoup(url.download(cached = False), "lxml") 
  try:
    ##################################################
   titles = bs.find('div', id='title')
   ratingvolumes = bs.find_all('span', {'class' : 'rating-count'})
    ##################################################
   if titles is not None:
    title = titles.find('h1').getText()
    if ratingvolumes is not None:
      ratingvolumes = str(ratingvolumes[0])
      ratingvolume= 'Does not work yet'
    else:
      ratingvolume = 'Not Found'
   else:
    title = 'Not Found'

   my_row = [title, ratingvolume]
   my_row_pd = pd.DataFrame([my_row], columns = columns) 

   df_podcast = df_podcast.append(my_row_pd, ignore_index=True)
   return df_podcast
  except:
   return 
