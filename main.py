import linkfetch

itunesl = ['https://itunes.apple.com/us/genre/podcasts/id26?mt=2',
      'https://itunes.apple.com/us/genre/podcasts-',
      'https://itunes.apple.com/us/podcast/'
      ]


itunes_links = linkfetch.find_links(itunesl[0],itunesl[1], itunesl[2])
print(len(itunes_links))

