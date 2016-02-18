# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField,  SubmitField, PasswordField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import  UserData


class LoginForm(Form):
	key = TextField('Key:')
	username = TextField('Username:')
	password = PasswordField('Password:')
	submit = SubmitField('OK')


class RegisterForm(Form):
	key = TextField('Key:')
	username = TextField('Username:')
	password = PasswordField('Password:')
	firstname = TextField('First name:')
	lastname = TextField('Last name:')
	tel = TextField('Tel. nr:')
	submit = SubmitField('OK')

class AddDataForm(Form):

	# firstname = TextField('Name:')
	# lastname = TextField('Last name:')
	# tel = TextField('Telephone:')
	key = TextField('Key:')
	secret = TextField('What is your secret?')
	photo = TextField('ID:')
	video = TextField('Other data:')
	submit = SubmitField('OK')



