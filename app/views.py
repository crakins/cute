from flask import render_template, flash, redirect
from app import app
from scrape import get_urls
import random

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Ryan' } # fake user
	searchTerm = "cute puppy"
	images = get_urls(searchTerm)
	maxNumber = len(images)
	randUrl = random.randint(0, maxNumber)
	return render_template('index.html', 
		title = 'Home', 
		user = user,
		searchTerm = searchTerm,
		images = images[randUrl])
