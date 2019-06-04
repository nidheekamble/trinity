from flask_wtf import FlaskForm
from flask_wtf.file import FlaskField
from flask_login import current_user
from wtforms import StringField, IntegerField, RadioField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Required, NumberRange, ValidationError
from trinity.models import ##########3

class DetailsForm(FlaskForm):
	name = StringField('Name', validators = [DataRequired(), Length(max = 30)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	submit = SubmitField('Done')

	def validateEmail(self, Email):
		######
		if user:
			raise ValidationError('Email taken, enter a different one')
