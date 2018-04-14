import pattern3.web as web
from bs4 import BeautifulSoup
import re
import pandas as pd
from progressbar import ProgressBar

###Find links to genre pages with all podcast links
#URL page with all genres of podcasts
genres_page= 'https://itunes.apple.com/us/genre/podcasts/id26?mt=2'

#Function to find all links and add to list 'links_page'
def scrape_links(page):
    if page is not None:
        url = web.URL(page)
        bs = BeautifulSoup(url.download(cached = False), "lxml")
        page_link = []
        for link in bs.findAll('a', href=True):
            page_link.append(link['href'])
        return page_link
    else:
        pass
    
#List for genre links found in genre url page
raw_genre_links = scrape_links(genres_page)

#pattern of links we are looking for
pattern = 'https://itunes.apple.com/us/genre/podcasts-'

#recognize relevant links
def recognize_pattern(link, pattern):
    recognized_links = []
    for l in link:
            if re.search(pattern, l):
                recognized_links.append(l)
    return recognized_links

#list of genre links we are looking for
genre_links = recognize_pattern(raw_genre_links, pattern)

###Using Genre links, find all podcast links

pattern2 = 'https://itunes.apple.com/us/podcast/'

podcast_links = []

for genre_link in genre_links:
    all_links = scrape_links(genre_link)
    podcast_links.extend(recognize_pattern(all_links, pattern2))

columns= ['Name', 'Genre ID', 'Episode Count', 'Episode Durations','Rating Value', 'Rating Volume','Description', 'Release Dates']
podcast_df = pd.DataFrame([[0, 0, 0, 0, 0, 0, 0, 0]], columns = columns)
##
##def get_data(webp):
##    try:
##        url = web.URL(webp)
##        bs = BeautifulSoup(url.download(cached = False))
##        titles = bs.find('div', id='title')
##        if titles is not None:
##            title = titles.find('hi').getText()
##
##        my_row = [title, genreid, eount, edurations, rValue, rvolume, description, released]
##        my_row_pd = pd.DataFrame([my_row], columns = columns)  
##        df_podcast = df_podcast.append(my_row_pd, ignore_index=True)
##
##    except: 
##            return None 

print(len(podcast_links))

pbar = ProgressBar()
for link in pbar(podcast_links[360]):
    get_data(link)
print(podcast_df)


    













