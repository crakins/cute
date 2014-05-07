from flask import render_template, flash, redirect
from app import app
from scrape import get_urls

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Ryan' } # fake user
	images = get_urls("kitty")
	return render_template('index.html', 
		title = 'Home', 
		user = user,
		images = images)
