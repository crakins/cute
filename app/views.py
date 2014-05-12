from flask import render_template, flash, redirect
from app import app
from scrape import get_urls
import random

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Ryan' } # fake user
	searchTerm = "super cute"
	images = get_urls(searchTerm)
	maxNumber = len(images)
	randUrl = random.randint(0, maxNumber-1)
	return render_template('index.html', 
		title = 'Home', 
		user = user,
		searchTerm = searchTerm,
		images = images[randUrl],
		randUrl = randUrl)

@app.route('/<animal>')
def indexAnimal(animal):
	user = { 'nickname': 'Ryan' } # fake user
	searchTerm = "cute " + animal
	images = get_urls(searchTerm)
	maxNumber = len(images)
	randUrl = random.randint(0, maxNumber-1)
	return render_template('index.html', 
		title = 'Home', 
		user = user,
		searchTerm = searchTerm,
		images = images[randUrl],
		randUrl = randUrl)
