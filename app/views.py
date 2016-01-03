from flask import render_template, flash, redirect, request
from app import app
# from scrape import get_urls
from pix import get_urls, get_all_urls_file, get_keyword_urls_file
import random
from processImages import storeImages

@app.route('/')
@app.route('/index')
def index():
    search_query = request.args.get('q')
    if search_query:
       searchTerm = "cute %s" % search_query
    else:
        searchTerm = "cute animals"
    user = { 'nickname': 'Ryan' } # fake user
    # images = get_urls(searchTerm) # must change this, got locked out of API
    # maybe read
    images = get_all_urls_file()
    maxNumber = len(images)
    if maxNumber > 0:
        randUrl = random.randint(0, maxNumber-1)
        return render_template('index.html', 
            title = 'Home', 
            user = user,
            searchTerm = searchTerm,
            search = search_query,
            images = images[randUrl],
            randUrl = randUrl)
    else:
        return render_template('index.html',
            title = 'Home',
            user = user,
            searchTerm = searchTerm,
            search = search_query,
            images = 'Sorry no pictures')

@app.route('/<animal>')
def indexAnimal(animal):
	user = { 'nickname': 'Ryan' } # fake user
	searchTerm = "cute " + animal
	# images = get_urls(searchTerm) # must change this, got locked out of API
	images = get_keyword_urls_file(searchTerm)
	maxNumber = len(images)
	if maxNumber > 0:
	    randUrl = random.randint(0, maxNumber-1)
	    return render_template('index.html', 
		    title = 'Home', 
		    user = user,
		    searchTerm = searchTerm,
		    images = images[randUrl],
		    randUrl = randUrl)
	else:
	    return render_template('index.html',
	        title = 'Home',
	        user = user,
	        searchTerm = searchTerm,
	        images = 'Sorry no pictures')

@app.route('/process/<keyword>')
def process(keyword):
	storeImages(keyword)
	flash('keyword: ' + keyword + ' processed')
	return redirect('/index')
	
