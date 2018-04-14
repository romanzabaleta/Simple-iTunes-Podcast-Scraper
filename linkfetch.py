import pattern3.web as web
from bs4 import BeautifulSoup
import re

#iTunes##################################################################

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
def recognize_pattern(link, pattern):
    recognized_links = []
    for l in link:
        if re.search(pattern, l):
            recognized_links.append(l)
    return recognized_links
def find_links(page, pattern, pattern2):
    x = scrape_links(page)
    y = recognize_pattern(x, pattern)
    podcast_links = []
    for i in y:
        all_links = scrape_links(i)
        podcast_links.extend(recognize_pattern(all_links, pattern2))
    return podcast_links

