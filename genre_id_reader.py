import pandas
from pandas import read_excel

def appendixgen():
	gdf = read_excel('genreidappendix.xlsx')
	grdict = gdf.to_dict('split')
	grdict = grdict['data']
	dict = {}
	for i in range(0,len(grdict)):
		dict[str(grdict[i][0])] = grdict[i][1]
	return dict

