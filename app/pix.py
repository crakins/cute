from urllib2 import Request, urlopen, URLError
import urllib
import json

# https://pixabay.com API_KEY

API_KEY = '1838068-18ce42d18bb425f5d9e026c14'
# iType = 'photo'

def get_urls(searchTerm):

    query = 'cute %s' % searchTerm
    
    # params = {'key' : API_KEY, 'q' : query, 'image_type' : iType}
    params = {'key' : API_KEY, 'q' : query}
    url = 'https://pixabay.com/api/?' + urllib.urlencode(params)
    request = Request('https://pixabay.com/api/?' + urllib.urlencode(params))

    try:
        data = json.load(urlopen(request))
        hits = data.get('hits')
        
        i = 0
        urls = []
        while i < len(hits):
            # print hits[i]['webformatURL'] # prints to screen
            urls.append(hits[i]['webformatURL'] + "\n")
            i = i + 1
        
        # write to file        
        f = open('images.txt', 'a')
        f.writelines(urls)
        f.close()
        
        # return url list
        return urls
        
    except URLError, e:
        return 'No images available'
        
def get_all_urls_file():
    # open images.txt file
    with open('images.txt', 'r') as f:
        urls = f.readlines()
    return urls

def get_keyword_urls_file(searchTerm):
    # open images.txt file
    with open('images.txt', 'r') as f:
        urls = f.readlines()
    return urls
