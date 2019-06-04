import os
import secrets
from trinity import app, db
from trinity.models import User, Organizer
from trinity.forms import UserForm, OrgForm
from sqlalchemy import or_, and_
from flask import Flask, session, render_template, url_for, flash, redirect, request

@app.route("/")
@app.route("/home", methods = ['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route("/organizer", methods = ['GET', 'POST'])
def regOrg():
	form = OrgForm()
	if form.validate_on_submit():
		organizer = Organizer(email=form.email.data, name=form.name.data, kind=form.kind.data)
		organizer.type = 'organizer'
		db.session.add(organizer)
		db.session.commit()
		return redirect(url_for('login'))
	return render_template('organizer.html', form=form)


@app.route("/user", methods = ['GET', 'POST'])
def regUser():
	form = UserForm()
	if form.validate_on_submit():
		user = User(email=form.email.data, name=form.name.data)
		user.type = 'user'
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('find'))
	return render_template('user.html', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
	return render_template('login.html', form=form)


@app.route("/find", methods = ['GET', 'POST'])
def find():
	return render_template('find.html)')

