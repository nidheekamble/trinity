import os
import secrets
import requests
import hashlib
from trinity import app, db
from trinity.models import User, Organizer
from trinity.forms import UserForm, OrgForm, UpdateDetails, LoginForm, FilterForm
from sqlalchemy import or_, and_
from sqlalchemy.orm import Session
from flask import Flask, session, render_template, url_for, flash, redirect, request, send_from_directory
from flask_login import login_user, current_user, logout_user, login_required
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
from PIL import Image

@app.route("/")
@app.route("/home", methods = ['GET', 'POST'])
def home():
	return render_template('home.html', title='Home')

@app.route("/organizer", methods = ['GET', 'POST'])
def regOrg():
	form = OrgForm()
	if form.validate_on_submit():
		
		pw = (form.password.data)
		s = 0
		for char in pw:
			a = ord(char) #ASCII
			s = s+a #sum of ASCIIs acts as the salt
		hashed_password = (str)((hashlib.sha512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())
	
		organizer = Organizer(email=form.email.data, name=form.name.data, kind=form.kind.data, password = hashed_password)
		organizer.type = 'organizer'
		db.session.add(organizer)
		db.session.commit()
		print("before pic")

		if form.photo1.data:
			photo_file = save_photo(form.photo1.data)
			organizer.photo1 = photo_file
			photo1 = url_for('static', filename='organizer/' + organizer.photo1)
		if form.photo2.data:
			photo_file = save_photo(form.photo2.data)
			organizer.photo1 = photo_file
			photo2 = url_for('static', filename='organizer/' + organizer.photo2)
		if form.photo3.data:
			photo_file = save_photo(form.photo3.data)
			organizer.photo1 = photo_file
			photo3 = url_for('static', filename='organizer/' + organizer.photo3)

		db.session.add(organizer)
		db.session.commit()
		print(organizer)

		return redirect(url_for('login'))
	print('form not validated')
	print(form.errors)
	return render_template('organizer.html', title='Organizer', form=form)

def save_photo(form_photo):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_photo.filename)
	photo_fn = random_hex + f_ext
	## Don't use static\organizer, pass them as separate arguments
	photo_path = os.path.join(app.root_path, 'static','organizer', photo_fn)
	print('PHOTO TO BE SAVED:: ', photo_path)
	output_size = (125, 125)
	i = Image.open(form_photo)
	i.thumbnail(output_size)
	#this will fail if static/organizer folder doesn't exist
	i.save(photo_path)
	return photo_fn


@app.route("/user", methods = ['GET', 'POST'])
def regUser():
	form = UserForm()
	if form.validate_on_submit():
		user = User(email=form.email.data, name=form.name.data, date='')
		user.type = 'user'
		db.session.add(user)
		db.session.commit()
		print(user)

		return redirect(url_for('find'))
	return render_template('user.html', title='User', form=form)

@app.route("/login", methods = ['GET','POST'])
def login():
	form = LoginForm(request.form)

	if form.validate_on_submit():
		organizer = Organizer.query.filter_by(id=current_user.id).first()
		pw = (form.password.data)
		s = 0
		for char in pw:
			a = ord(char) #ASCII
			s = s+a #sum of ASCIIs acts as the salt
		now_hash = (str)((hashlib.sha512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())

		if (organizer and (organizer.password==now_hash)):
			login_user(organizer)
			print("hash correct")
			return redirect(url_for('account'))

		else:
			print('Nahin hua')
			flash('Login Unsuccessful. Please check email and password', 'danger')

	return render_template('login.html', title='Login', form=form)


@app.route("/find", methods = ['GET', 'POST'])
def find():
	form = FilterForm()
	if form.validate_on_submit():
		date = form.date.data
		#venue = form.venue.data
		print(date)
		return redirect(url_for('filter'))
	else:
		print('Not validated')

	return render_template('find.html', title='Find', form=form)

@app.route("/filter", methods = ['GET', 'POST'])
def filter():
	form = FilterForm()
	print('in filter')
	return render_template('home.html')

@app.route("/account", methods = ['GET', 'POST'])
@login_required
def account():
	form = UpdateDetails()
	organizer = Organizer.query.filter_by(id=current_user.id).first()
	if form.validate_on_submit():

		organizer = Organizer(email=form.email.data, name=form.name.data, kind=form.kind.data)
		organizer.type = 'organizer'

		if form.photo1.data:
			photo_file = save_photo(form.photo1.data)
			organizer.photo1 = photo_file
			photo1 = url_for('static', filename='organizer/' + organizer.photo1)
		if form.photo2.data:
			photo_file = save_photo(form.photo2.data)
			organizer.photo1 = photo_file
			photo2 = url_for('static', filename='organizer/' + organizer.photo2)
		if form.photo3.data:
			photo_file = save_photo(form.photo3.data)
			organizer.photo1 = photo_file
			photo3 = url_for('static', filename='organizer/' + organizer.photo3)

		db.session.add(organizer)
		db.session.commit()
		print(organizer)
		flash('Your account has been updated!', 'success')
	return render_template("account.html", title='account', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))