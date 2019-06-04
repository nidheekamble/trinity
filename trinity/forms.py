from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask_login import current_user
from wtforms import StringField, IntegerField, RadioField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Required, NumberRange, ValidationError
from trinity.models import User

class UserForm(FlaskForm):
	name = StringField('Name', validators = [DataRequired(), Length(max = 30)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	submit = SubmitField('Done')

	def validateEmail(self, Email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email taken, enter a different one')

class OrgForm(FlaskForm):
	name = StringField('Name', validators = [DataRequired(), Length(max=30)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	types = [('0','Parties'), ('1', 'Wedding'), ('2', 'Corporate')]
	kind = SelectField('Type', choices = types, validators = [Required()])
	submit = SubmitField('Make Me Discoverable')

	def validateEmail(self, Email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email taken, enter a different one')

