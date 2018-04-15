from bs4 import BeautifulSoup
import pandas as pd
from progressbar import ProgressBar
import pattern3.web as web

columns =   ['Name']
podcast_df = pd.DataFrame([[0]], columns = columns)

def get_data(webp, df_podcast):
  url = web.URL(webp)
  bs = BeautifulSoup(url.download(cached = False), "lxml") 
  try:
   titles = bs.find('div', id='title')
   if titles is not None:
    title = titles.find('h1').getText()
   my_row = [title]
   my_row_pd = pd.DataFrame([my_row], columns = columns)  
   df_podcast = df_podcast.append(my_row_pd, ignore_index=True)
   return df_podcast
  except:
    return None
  



