from bs4 import BeautifulSoup
import pandas as pd
from progressbar import ProgressBar

columns =   ['Name']
podcast_df = pd.DataFrame([[0]], columns = columns)

def get_data(webp):
   try:
       url = web.URL(webp)
       bs = BeautifulSoup(url.download(cached = False))
       titles = bs.find('div', id='title')
       if titles is not None:
           title = titles.find('hi').getText()

       my_row = [title]
       my_row_pd = pd.DataFrame([my_row], columns = columns)  
       df_podcast = df_podcast.append(my_row_pd, ignore_index=True)
       return df_podcast

   except: 
   		return None 
