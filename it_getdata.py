from bs4 import BeautifulSoup
import pandas as pd
#from progressbar import ProgressBar
import pattern3.web as web
import re
import genre_id_reader as gen 


def get_data(webp, df_podcast, columns):
    url = web.URL(webp)
    bs = BeautifulSoup(url.download(cached = False), "lxml")

    try:
    ##############################################################
        titles = bs.find('div', id='title')
        ratingvolumes = bs.find_all('span', {'class' : 'rating-count'})
        ratingvalue = bs.find_all('span', {'itemprop' : 'ratingValue'})
        genreraw = bs.find_all('li', {'class' : 'genre'})
        print(genreraw)
        print(ratingvalue)
    ##############################################################

        if titles is not None:
            title = titles.find('h1').getText()
        else:
            title = 'Not Found'

        if ratingvolumes is not None:
            ratingvolumes = str(ratingvolumes[0])
            ratingvolume = int(''.join(i for i in ratingvolumes if i.isdigit()))
        else:
            ratingvolume = 'Not Found'

        if ratingvalue is not None:
            ratingvalue = str(ratingvalue[0])
            rating = float(''.join(i for i in ratingvalue if i.isdigit() or i == "."))
        else:
            rating = 'Not Found'

        if genreraw is not None:
            genreraw = str(genreraw[0])
            genreid = re.findall(r"id\d\d\d\d", genreraw)
            genrenum = re.findall(r'\d\d\d\d', genreid[0])
            genre = str(gen.appendixgen()[str(genrenum[0])])
        else:
            genre = 'Not Found'

        my_row = [title, ratingvolume, rating, genre]
        my_row_pd = pd.DataFrame([my_row], columns = columns)

        df_podcast = df_podcast.append(my_row_pd, ignore_index=True)
        return df_podcast

    except ValueError:
        return "Error"
