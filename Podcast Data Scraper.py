import pattern3.web as web
from bs4 import BeautifulSoup
import re

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

# test - Jon
