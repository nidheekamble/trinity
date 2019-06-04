import os
import secrets
from trinity import app, db
from trinity.models import user
from trinity.forms import DetailsForm
from sqlalchemy import or_, and_
from flask import Flask, session, render_template, url_for, flash, redirect, request

@app.route("/")
@app.route("/home", methods = ['GET', 'POST'])
def home():
	form = DetailsForm()
	if form.validate_on_submit():
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('home.html')

