import linkfetch

pa = ['https://itunes.apple.com/us/genre/podcasts/id26?mt=2',
      'https://itunes.apple.com/us/genre/podcasts-',
      'https://itunes.apple.com/us/podcast/'
      ]


links = linkfetch.find_links(pa[0],pa[1], pa[2])
print(len(links))
