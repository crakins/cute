from flask import render_template, flash, redirect, request
from app import app
# from scrape import get_urls
from pix import get_urls, get_all_urls_file, get_keyword_urls_file
import random
from processImages import storeImages
from pix_test import *
from .forms import LoginForm

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
    # images = get_all_urls_file()
    directory = '/home/crakins/dev/cute/app/static/images/animals/'
    images = get_list_of_images_files(directory)
    maxNumber = len(images)
    if maxNumber > 0:
        randUrl = random.randint(0, maxNumber-1)
        return render_template('index.html', 
            title = 'Home', 
            user = user,
            searchTerm = searchTerm,
            search = search_query,
            images = '/static/images/animals/' + images[randUrl],
            randUrl = randUrl,
            countImages = len(images))
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='sign in',
                            form=form)
	
