from app import db

# User Roles
ROLE_USER = 0
ROLE_ADMIN = 1

# Image Status
BANNED = -1
OKAY = 0
REPORTED = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Image(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	url = db.Column(db.String(500), index = True, unique = True)
	ban = db.Column(db.SmallInteger, default = OKAY)
	cutes = db.Column(db.Integer, default = 0)
	file_name = db.Column(db.String(500), index = True, unique = True)
	test = db.Column(db.Integer, default = 0)

class Category(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), index = True, unique = True)
