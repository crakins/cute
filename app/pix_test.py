from urllib2 import Request, urlopen, URLError
import urllib
import json
import requests

# https://pixabay.com API_KEY

# added for testing in console

def get_list_of_images_files(directory):
    import os
    files = os.listdir(directory)
    return files

def save_imgs_by_term(searchTerm):
    load_imports()
    urls = pb_url_list(searchTerm)
    
    for url in urls:
        save_url_file(url)

def save_to_db(url, searchTerm):
    # connect to database
    # save searchTerm as category, credit url, 
    # save 
    return ""

def load_imports():
    from urllib2 import Request, urlopen, URLError
    import urllib
    import json
    import requests
    import os
    
def pb_url_list(searchTerm):
    API_KEY = '1838068-18ce42d18bb425f5d9e026c14'
    # iType = 'photo'

    query = 'cute %s' % searchTerm
    
    # params = {'key' : API_KEY, 'q' : query, 'image_type' : iType}
    params = {'key' : API_KEY, 'q' : query}
    url = 'https://pixabay.com/api/?' + urllib.urlencode(params)
    request = Request('https://pixabay.com/api/?' + urllib.urlencode(params))
    
    data = json.load(urlopen(request))
    hits = data.get('hits')
    
    i = 0
    urls = [] # TODO: change to dictionary to store url, category (searchTerm), and credit url
    while i < len(hits):
        # print hits[i]['webformatURL'] # prints to screen
        urls.append(hits[i]['webformatURL'])
        i = i + 1
    return urls

def save_url_file(url):
    import os
    file_name = os.path.split(url)[1]
    r = requests.get(url)
    with open('static/images/animals/' + file_name, 'wb') as f:
        f.write(r.content)

def return_string(term):
    return term

def load_data(searchTerm):
    

    API_KEY = '1838068-18ce42d18bb425f5d9e026c14'
    # iType = 'photo'

    query = 'cute %s' % searchTerm
    
    # params = {'key' : API_KEY, 'q' : query, 'image_type' : iType}
    params = {'key' : API_KEY, 'q' : query}
    url = 'https://pixabay.com/api/?' + urllib.urlencode(params)
    request = Request('https://pixabay.com/api/?' + urllib.urlencode(params))
    

    try:
        data = json.load(urlopen(request))
        hits = data.get('hits')
        
        i = 0
        u = 0
        urls = []
        while i < len(hits):
            # print hits[i]['webformatURL'] # prints to screen
            urls.append(hits[i]['webformatURL'] + "\n")
            i = i + 1
            
            # save to file
            # does not work properly, need to fix
        u = 0
        for url in urls:
            # TODO: use regex to get unique filename
            r = requests.get(url)
            u = u + 1
            with open('static/images/animals/' + searchTerm + str(u) + '.jpg', 'wb') as f:
                f.write(r.content)
            print "wrote " + url + " to file."
        
        
        # write to file        
        #f = open('images.txt', 'a')
        #f.writelines(urls)
        #f.close()
        
        # return url list
        #return urls
        
    except URLError, e:
        return 'No images available'
