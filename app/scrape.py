import requests
import bs4

root_url = 'http://www.bing.com'
url_prefix_searchTerm = root_url + '/images/search?pq='
url_mid_searchTerm = '&sc=8-3&sp=-1&sk=&adlt=strict&adlt=strict&adlt=strict&q='
url_suffix_searchTerm = '&qft=+filterui:imagesize-medium+filterui:license-L2_L3_L4&FORM=R5IR38'

#class ImageUrls:
	#def __init__(self, searchTerm):
	#	self.searchTerm = searchTerm
		
def get_urls(searchTerm):
	#searchTerm = "kitty"
	index_url = url_prefix_searchTerm + searchTerm + url_mid_searchTerm + searchTerm + url_suffix_searchTerm
	response = requests.get(index_url)
	soup = bs4.BeautifulSoup(response.text)
	return [a.attrs.get('src2') for a in soup.select('img[src2]')]
