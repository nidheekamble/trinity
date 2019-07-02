from trinity import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
	
@login_manager.user_loader
def load_org(org_id):
	return Organizer.query.get(int(org_id))

class User(db.Model, UserMixin):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(30), nullable = False)
	email = db.Column(db.String(50), unique = True, nullable = False)
	dateUser = db.Column(db.String(20), unique = False)
	venueUser = db.Column(db.Integer, unique = False)
	type= db.Column(db.String(20), nullable=False)

	def __repr__(self):
		return f"User('{self.id}', {self.email}', '{self.type}', '{self.dateUser}', '{self.venueUser}')"

class Organizer(db.Model, UserMixin):
	__tablename__ = 'organizer'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(30), nullable = False)
	email = db.Column(db.String(30), unique = True, nullable = False)
	kind = db.Column(db.String(30), unique = False, nullable=False)
	type = db.Column(db.String(20), nullable=False)
	about = db.Column(db.String(120), unique = False, nullable = False)
	dateOrg = db.Column(db.String(10), unique = False, nullable = False)
	venueOrg = db.Column(db.String(20), unique = False, nullable = False)
	photo1 = db.Column(db.String(20), unique = False, default = 'default.jpg' , nullable= True )
	photo2 = db.Column(db.String(20), unique = False, default = 'default.jpg' , nullable= True )
	photo3 = db.Column(db.String(20), unique = False, default = 'default.jpg' , nullable= True )
	password = db.Column(db.String(128), unique = False, nullable = False)

	def __repr__(self):
		return f"Organizer('{self.id}', '{self.email}', '{self.kind}', '{self.type}', '{self.dateOrg}', '{self.venueOrg}')"