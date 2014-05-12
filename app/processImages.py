from app import db
from scrape import get_urls
import sys
from app import models
from models import Image

def storeImages(searchTerm):
	images = get_urls(searchTerm)

	for i in images:
		print i
		img = Image(url = i, ban = 0, cutes = 0)
		db.session.add(img)
		db.session.commit()
